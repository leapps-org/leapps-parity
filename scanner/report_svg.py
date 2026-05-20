"""Generate parity.svg badge-style summary chart."""

from __future__ import annotations

from scanner.compare import ScanResult, Status


def _file_bucket_counts(result: ScanResult) -> dict[str, int]:
    buckets = {
        "same": 0,
        "changed": 0,
        "missing": 0,
        "extra": 0,
        "repo_specific": 0,
        "parse_errors": 0,
    }
    for fc in result.files:
        if fc.status == Status.SAME:
            buckets["same"] += 1
        elif fc.status in (Status.LOGIC_CHANGED, Status.FILE_CHANGED):
            buckets["changed"] += 1
        elif fc.status == Status.FILE_MISSING_FROM_COMPARISON:
            buckets["missing"] += 1
        elif fc.status == Status.FILE_EXTRA_IN_COMPARISON:
            buckets["extra"] += 1
        elif fc.status == Status.EXPECTED_REPO_SPECIFIC:
            buckets["repo_specific"] += 1
        elif fc.status == Status.PYTHON_PARSE_ERROR:
            buckets["parse_errors"] += 1
    return buckets


def render_parity_svg(result: ScanResult) -> str:
    counts = _file_bucket_counts(result)
    total = max(sum(counts.values()), 1)

    colors = {
        "same": "#2ea043",
        "changed": "#d29922",
        "missing": "#f85149",
        "extra": "#a371f7",
        "repo_specific": "#58a6ff",
        "parse_errors": "#8b949e",
    }
    labels = {
        "same": "Same",
        "changed": "Changed",
        "missing": "Missing",
        "extra": "Extra",
        "repo_specific": "Repo-specific",
        "parse_errors": "Parse errors",
    }

    width = 640
    bar_height = 28
    row_height = 36
    title_y = 24
    bar_y = 52  # gap below title (font-size 14 needs ~28px clearance)
    legend_y = bar_y + bar_height + 16
    height = legend_y + len(counts) * row_height + 16

    segments: list[str] = []
    x_offset = 16
    bar_width = width - 32

    for key in ("same", "changed", "missing", "extra", "repo_specific", "parse_errors"):
        value = counts[key]
        if value <= 0:
            continue
        seg_w = max(int(bar_width * value / total), 2)
        segments.append(
            f'<rect x="{x_offset}" y="{bar_y}" '
            f'width="{seg_w}" height="{bar_height}" fill="{colors[key]}" '
            f'rx="4"><title>{labels[key]}: {value}</title></rect>'
        )
        x_offset += seg_w

    rows: list[str] = []
    y = legend_y
    for key in ("same", "changed", "missing", "extra", "repo_specific", "parse_errors"):
        value = counts[key]
        rows.append(
            f'<g transform="translate(16,{y})">'
            f'<rect width="12" height="12" fill="{colors[key]}" rx="2"/>'
            f'<text x="20" y="11" font-family="system-ui,sans-serif" '
            f'font-size="13" fill="#e6edf3">{labels[key]}: {value}</text>'
            f"</g>"
        )
        y += row_height

    title = (
        f"LEAPP Parity — {result.baseline} vs {result.comparison} "
        f"({counts['same']}/{total} same)"
    )

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" viewBox="0 0 {width} {height}" role="img" aria-label="{title}">
  <rect width="100%" height="100%" fill="#0d1117" rx="8"/>
  <text x="16" y="{title_y}" font-family="system-ui,sans-serif" font-size="14" font-weight="600" fill="#e6edf3">{title}</text>
  {''.join(segments)}
  {''.join(rows)}
</svg>
"""
