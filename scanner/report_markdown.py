"""Generate GitHub-friendly Markdown reports."""

from __future__ import annotations

from datetime import datetime
from pathlib import Path

from scanner.compare import FileComparison, ScanResult, Status


def versioned_parity_filename(generated_at: str) -> str:
    """Return a timestamped SVG filename for cache busting (Obsidian + GitHub friendly)."""
    dt = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
    return f"parity.{int(dt.timestamp())}.svg"


def cleanup_old_parity_svgs(out_dir: Path, keep_filename: str) -> None:
    """Remove prior versioned parity charts, keeping only the current run's file."""
    for path in out_dir.glob("parity.*.svg"):
        if path.name != keep_filename:
            path.unlink(missing_ok=True)
    legacy = out_dir / "parity.svg"
    if legacy.exists():
        legacy.unlink()


def _count_files(result: ScanResult, *statuses: Status) -> int:
    return sum(1 for f in result.files if f.status in statuses)


def _count_symbols(result: ScanResult, *statuses: Status) -> int:
    return sum(
        1
        for f in result.files
        for s in f.symbol_diffs
        if s.status in statuses
    )


def _file_rows(result: ScanResult) -> list[tuple[str, int]]:
    keys = [
        Status.SAME,
        Status.LOGIC_CHANGED,
        Status.FILE_CHANGED,
        Status.FILE_MISSING_FROM_COMPARISON,
        Status.FILE_EXTRA_IN_COMPARISON,
        Status.EXPECTED_REPO_SPECIFIC,
        Status.PYTHON_PARSE_ERROR,
    ]
    return [(s.value, _count_files(result, s)) for s in keys]


def _symbol_rows(result: ScanResult) -> list[tuple[str, int]]:
    keys = [
        Status.SYMBOL_MISSING_FROM_COMPARISON,
        Status.SYMBOL_EXTRA_IN_COMPARISON,
        Status.SIGNATURE_CHANGED,
        Status.LOGIC_CHANGED,
    ]
    return [(s.value, _count_symbols(result, s)) for s in keys]


def _mismatch_priority(fc: FileComparison, import_sources: set[str]) -> tuple[int, str]:
    """Lower sort key = higher priority in summary tables."""
    order = {
        Status.PYTHON_PARSE_ERROR: 0,
        Status.LOGIC_CHANGED: 1,
        Status.FILE_CHANGED: 2,
        Status.FILE_MISSING_FROM_COMPARISON: 3,
        Status.FILE_EXTRA_IN_COMPARISON: 4,
    }
    base = order.get(fc.status, 5)
    if fc.logical_path in import_sources:
        base -= 1
    return (base, fc.logical_path)


def _top_mismatches(result: ScanResult, limit: int = 20) -> list[str]:
    lines: list[str] = []
    import_sources = {g.source_logical_path for g in result.import_dependency_gaps}
    ranked = [
        f
        for f in result.files
        if f.status
        not in (Status.SAME, Status.EXPECTED_REPO_SPECIFIC)
    ]
    ranked.sort(key=lambda f: _mismatch_priority(f, import_sources))
    for fc in ranked[:limit]:
        b = fc.baseline_physical or "—"
        c = fc.comparison_physical or "—"
        sym_count = len(fc.symbol_diffs)
        extra = f" ({sym_count} symbol diffs)" if sym_count else ""
        lines.append(
            f"| `{fc.logical_path}` | {fc.status.value} | `{b}` | `{c}` |{extra}"
        )
    return lines


def _write_detail_list(
    path: Path,
    title: str,
    items: list[str],
    *,
    empty_message: str = "_None._",
) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    body = "\n".join(items) if items else empty_message
    path.write_text(f"# {title}\n\n{body}\n", encoding="utf-8")


def _build_file_list(result: ScanResult) -> str:
    status_order = {
        Status.PYTHON_PARSE_ERROR: 0,
        Status.LOGIC_CHANGED: 1,
        Status.FILE_CHANGED: 2,
        Status.FILE_MISSING_FROM_COMPARISON: 3,
        Status.FILE_EXTRA_IN_COMPARISON: 4,
        Status.EXPECTED_REPO_SPECIFIC: 5,
        Status.SAME: 6,
    }
    rows = sorted(
        result.files,
        key=lambda f: (status_order.get(f.status, 99), f.logical_path),
    )
    lines = [
        "# All compared files",
        "",
        f"**{result.baseline}** (baseline) vs **{result.comparison}** (comparison)",
        "",
        "| Logical path | Status | Baseline | Comparison |",
        "|---|---|---|---|",
    ]
    for fc in rows:
        b = fc.baseline_physical or "—"
        c = fc.comparison_physical or "—"
        lines.append(
            f"| `{fc.logical_path}` | {fc.status.value} | `{b}` | `{c}` |"
        )
    return "\n".join(lines) + "\n"


def _build_signature_changes(signature_items: list[tuple[str, str, str, str]]) -> str:
    """Build signature_changes.md with per-symbol headers and stacked signature rows."""
    if not signature_items:
        return "# Signature changes\n\n_None._\n"

    blocks = ["# Signature changes", ""]
    for logical_path, qname, baseline_sig, comparison_sig in signature_items:
        blocks.extend(
            [
                f"### `{logical_path}` — `{qname}`",
                "",
                "| | Signature |",
                "|:---|:---|",
                f"| Baseline | `{baseline_sig}` |",
                f"| Comparison | `{comparison_sig}` |",
                "",
            ]
        )
    return "\n".join(blocks)


def _build_changed_logic(result: ScanResult) -> str:
    """Build changed_logic.md with per-file bullets for logic and one-sided symbols."""
    entries: list[tuple[str, list[str]]] = []

    for fc in sorted(result.files, key=lambda f: f.logical_path):
        bullets: list[str] = []
        if fc.module_logic_changed:
            bullets.append("module-level logic changed")

        for sd in sorted(fc.symbol_diffs, key=lambda s: s.qualified_name):
            if sd.status == Status.LOGIC_CHANGED:
                bullets.append(f"logic changed: `{sd.qualified_name}`")
            elif sd.status == Status.SYMBOL_MISSING_FROM_COMPARISON:
                line = f"only in {result.baseline}: `{sd.qualified_name}`"
                if sd.baseline_signature:
                    line += f" — `{sd.baseline_signature}`"
                bullets.append(line)
            elif sd.status == Status.SYMBOL_EXTRA_IN_COMPARISON:
                line = f"only in {result.comparison}: `{sd.qualified_name}`"
                if sd.comparison_signature:
                    line += f" — `{sd.comparison_signature}`"
                bullets.append(line)

        if bullets:
            entries.append((fc.logical_path, bullets))

    if not entries:
        return "# Changed logic files\n\n_None._\n"

    blocks = ["# Changed logic files", ""]
    for logical_path, bullets in entries:
        blocks.append(f"### `{logical_path}`")
        blocks.append("")
        for bullet in bullets:
            blocks.append(f"- {bullet}")
        blocks.append("")
    return "\n".join(blocks).rstrip() + "\n"


def write_reports(
    result: ScanResult,
    out_dir: Path,
    *,
    parity_image: str,
) -> None:
    out_dir = out_dir.resolve()
    details_dir = out_dir / "details"
    details_dir.mkdir(parents=True, exist_ok=True)

    # Detail pages
    missing_files: list[str] = []
    extra_files: list[str] = []
    signature_items: list[tuple[str, str, str, str]] = []
    parse_errors: list[str] = []

    for fc in result.files:
        if fc.status == Status.FILE_MISSING_FROM_COMPARISON:
            missing_files.append(
                f"- `{fc.logical_path}` (baseline: `{fc.baseline_physical}`)"
            )
        if fc.status == Status.FILE_EXTRA_IN_COMPARISON:
            extra_files.append(
                f"- `{fc.logical_path}` (comparison: `{fc.comparison_physical}`)"
            )
        if fc.status == Status.EXPECTED_REPO_SPECIFIC:
            extra_files.append(
                f"- `{fc.logical_path}` _(expected repo-specific)_ "
                f"(comparison: `{fc.comparison_physical}`)"
            )
        if fc.status == Status.PYTHON_PARSE_ERROR:
            parse_errors.append(
                f"- `{fc.logical_path}` — baseline: {fc.baseline_parse_error or 'ok'}; "
                f"comparison: {fc.comparison_parse_error or 'ok'}"
            )
        for sd in fc.symbol_diffs:
            if sd.status == Status.SIGNATURE_CHANGED:
                signature_items.append(
                    (
                        fc.logical_path,
                        sd.qualified_name,
                        sd.baseline_signature or "",
                        sd.comparison_signature or "",
                    )
                )

    changed_logic_md = _build_changed_logic(result)
    (details_dir / "changed_logic.md").write_text(changed_logic_md, encoding="utf-8")
    changed_logic_preview = [
        line
        for line in changed_logic_md.splitlines()
        if line.startswith("### ") or line.startswith("- ")
    ][:40]
    _write_detail_list(details_dir / "missing_files.md", "Missing files", missing_files)
    _write_detail_list(details_dir / "extra_files.md", "Extra / repo-specific files", extra_files)
    (details_dir / "signature_changes.md").write_text(
        _build_signature_changes(signature_items),
        encoding="utf-8",
    )
    _write_detail_list(details_dir / "parse_errors.md", "Parse errors", parse_errors)
    (details_dir / "file_list.md").write_text(_build_file_list(result), encoding="utf-8")

    import_gaps: list[str] = []
    for gap in result.import_dependency_gaps:
        import_gaps.append(
            f"- `{gap.source_logical_path}` imports `{gap.import_statement}` "
            f"→ missing `{gap.missing_logical_path}`"
        )
    _write_detail_list(
        details_dir / "import_dependency_gaps.md",
        "Import dependency gaps",
        import_gaps,
    )

    import_gap_table = (
        "\n".join(
            [
                "| Baseline file | Import | Missing in comparison |",
                "|---|---|---|",
                *[
                    f"| `{g.source_logical_path}` | `{g.import_statement}` "
                    f"| `{g.missing_logical_path}` |"
                    for g in result.import_dependency_gaps
                ],
            ]
        )
        if result.import_dependency_gaps
        else "_None — no baseline imports reference missing files._"
    )

    file_table_rows = "\n".join(
        f"| {status} | {count} |" for status, count in _file_rows(result) if count
    )
    symbol_table_rows = "\n".join(
        f"| {status} | {count} |" for status, count in _symbol_rows(result) if count
    )

    top_rows = _top_mismatches(result)
    top_section = (
        "\n".join(
            [
                "| Logical path | Status | Baseline file | Comparison file |",
                "|---|---|---|---|",
                *top_rows,
            ]
        )
        if top_rows
        else "_No mismatches._"
    )

    repo_meta = []
    for name, info in result.repos.items():
        repo_meta.append(
            f"- **{name}**: `{info['commit'][:12]}` on `{info['branch']}` "
            f"([{info['url']}]({info['url']}))"
        )

    summary = f"""# LEAPP Parity Report

![Parity summary]({parity_image})

## Scan metadata

- **Generated**: {result.generated_at}
- **Baseline**: `{result.baseline}`
- **Comparison**: `{result.comparison}`

{chr(10).join(repo_meta)}

## Overall counts

| Metric | Count |
|---|---:|
| Files scanned (union) | {len(result.files)} |
| Same | {_count_files(result, Status.SAME)} |
| Changed (logic/file) | {_count_files(result, Status.LOGIC_CHANGED, Status.FILE_CHANGED)} |
| Missing from comparison | {_count_files(result, Status.FILE_MISSING_FROM_COMPARISON)} |
| Extra in comparison | {_count_files(result, Status.FILE_EXTRA_IN_COMPARISON)} |
| Expected repo-specific | {_count_files(result, Status.EXPECTED_REPO_SPECIFIC)} |
| Parse errors | {_count_files(result, Status.PYTHON_PARSE_ERROR)} |
| Import dependency gaps | {len(result.import_dependency_gaps)} |

## File-level summary

| Status | Count |
|---|---:|
{file_table_rows or "| — | 0 |"}

## Symbol-level summary

| Status | Count |
|---|---:|
{symbol_table_rows or "| — | 0 |"}

## All compared files

{len(result.files)} file(s). See [details/file_list.md](details/file_list.md).

## Import dependency gaps

Baseline files that import modules missing from the comparison repo (for example `ilapfuncs.py` → `context.py`).

{len(result.import_dependency_gaps)} gap(s). See [details/import_dependency_gaps.md](details/import_dependency_gaps.md).

{import_gap_table}

## Top mismatches

{top_section}

## Changed logic files

{_count_files(result, Status.LOGIC_CHANGED, Status.FILE_CHANGED)} file(s). See [details/changed_logic.md](details/changed_logic.md).

<details>
<summary>Preview</summary>

{chr(10).join(changed_logic_preview) or "_None._"}

</details>

## Missing files

{_count_files(result, Status.FILE_MISSING_FROM_COMPARISON)} file(s). See [details/missing_files.md](details/missing_files.md).

<details>
<summary>Preview</summary>

{chr(10).join(missing_files[:20]) or "_None._"}

</details>

## Extra files

{_count_files(result, Status.FILE_EXTRA_IN_COMPARISON)} file(s). See [details/extra_files.md](details/extra_files.md).

<details>
<summary>Preview</summary>

{chr(10).join(extra_files[:20]) or "_None._"}

</details>

## Expected repo-specific files

{_count_files(result, Status.EXPECTED_REPO_SPECIFIC)} file(s).

## Parse errors

{_count_files(result, Status.PYTHON_PARSE_ERROR)} file(s). See [details/parse_errors.md](details/parse_errors.md).

<details>
<summary>Preview</summary>

{chr(10).join(parse_errors[:20]) or "_None._"}

</details>

## Signature changes

{_count_symbols(result, Status.SIGNATURE_CHANGED)} symbol(s). See [details/signature_changes.md](details/signature_changes.md).
"""

    (out_dir / "summary.md").write_text(summary, encoding="utf-8")
