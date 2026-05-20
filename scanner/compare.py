"""Compare discovered files and Python modules between LEAPP repos."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any

from scanner.config import ScannerConfig
from scanner.files import FileRecord, discover_files
from scanner.git_ops import RepoCheckout
from scanner.python_ast import ModuleAnalysis, analyze_python


class Status(str, Enum):
    SAME = "same"
    FILE_MISSING_FROM_COMPARISON = "file_missing_from_comparison"
    FILE_EXTRA_IN_COMPARISON = "file_extra_in_comparison"
    EXPECTED_REPO_SPECIFIC = "expected_repo_specific"
    FILE_CHANGED = "file_changed"
    PYTHON_PARSE_ERROR = "python_parse_error"
    SYMBOL_MISSING_FROM_COMPARISON = "symbol_missing_from_comparison"
    SYMBOL_EXTRA_IN_COMPARISON = "symbol_extra_in_comparison"
    SIGNATURE_CHANGED = "signature_changed"
    LOGIC_CHANGED = "logic_changed"


@dataclass
class SymbolDiff:
    qualified_name: str
    status: Status
    baseline_signature: str | None = None
    comparison_signature: str | None = None


@dataclass
class ImportDependencyGap:
    """Baseline file imports a module whose file is missing from comparison."""

    source_logical_path: str
    source_physical: str
    import_statement: str
    missing_logical_path: str


@dataclass
class FileComparison:
    logical_path: str
    status: Status
    baseline_physical: str | None = None
    comparison_physical: str | None = None
    baseline_parse_error: str | None = None
    comparison_parse_error: str | None = None
    symbol_diffs: list[SymbolDiff] = field(default_factory=list)
    module_logic_changed: bool = False


@dataclass
class ScanResult:
    generated_at: str
    baseline: str
    comparison: str
    repos: dict[str, dict[str, str]]
    files: list[FileComparison] = field(default_factory=list)
    import_dependency_gaps: list[ImportDependencyGap] = field(default_factory=list)
    counts: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict[str, Any]:
        return {
            "generated_at": self.generated_at,
            "baseline": self.baseline,
            "comparison": self.comparison,
            "repos": self.repos,
            "counts": self.counts,
            "import_dependency_gaps": [
                {
                    "source_logical_path": g.source_logical_path,
                    "source_physical": g.source_physical,
                    "import_statement": g.import_statement,
                    "missing_logical_path": g.missing_logical_path,
                }
                for g in self.import_dependency_gaps
            ],
            "files": [
                {
                    "logical_path": f.logical_path,
                    "status": f.status.value,
                    "baseline_physical": f.baseline_physical,
                    "comparison_physical": f.comparison_physical,
                    "baseline_parse_error": f.baseline_parse_error,
                    "comparison_parse_error": f.comparison_parse_error,
                    "module_logic_changed": f.module_logic_changed,
                    "symbol_diffs": [
                        {
                            "qualified_name": s.qualified_name,
                            "status": s.status.value,
                            "baseline_signature": s.baseline_signature,
                            "comparison_signature": s.comparison_signature,
                        }
                        for s in f.symbol_diffs
                    ],
                }
                for f in self.files
            ],
        }


def _read_module(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def _compare_symbols(
    baseline: ModuleAnalysis,
    comparison: ModuleAnalysis,
) -> list[SymbolDiff]:
    diffs: list[SymbolDiff] = []
    all_names = set(baseline.symbols) | set(comparison.symbols)

    for name in sorted(all_names):
        b_sym = baseline.symbols.get(name)
        c_sym = comparison.symbols.get(name)

        if b_sym and not c_sym:
            diffs.append(
                SymbolDiff(
                    qualified_name=name,
                    status=Status.SYMBOL_MISSING_FROM_COMPARISON,
                    baseline_signature=b_sym.signature,
                )
            )
            continue
        if c_sym and not b_sym:
            diffs.append(
                SymbolDiff(
                    qualified_name=name,
                    status=Status.SYMBOL_EXTRA_IN_COMPARISON,
                    comparison_signature=c_sym.signature,
                )
            )
            continue

        assert b_sym and c_sym
        if b_sym.signature != c_sym.signature:
            diffs.append(
                SymbolDiff(
                    qualified_name=name,
                    status=Status.SIGNATURE_CHANGED,
                    baseline_signature=b_sym.signature,
                    comparison_signature=c_sym.signature,
                )
            )
            continue

        b_hash = b_sym.logic_hash
        c_hash = c_sym.logic_hash
        if b_hash and c_hash and b_hash != c_hash:
            diffs.append(
                SymbolDiff(
                    qualified_name=name,
                    status=Status.LOGIC_CHANGED,
                    baseline_signature=b_sym.signature,
                    comparison_signature=c_sym.signature,
                )
            )

    return diffs


def _compare_python_files(
    baseline_path: Path,
    comparison_path: Path,
    logical_path: str,
    config: ScannerConfig,
    baseline_physical: str,
    comparison_physical: str,
) -> FileComparison:
    b_source = _read_module(baseline_path)
    c_source = _read_module(comparison_path)

    b_mod = analyze_python(
        b_source, baseline_physical, token_rules=config.token_normalization
    )
    c_mod = analyze_python(
        c_source, comparison_physical, token_rules=config.token_normalization
    )

    fc = FileComparison(
        logical_path=logical_path,
        status=Status.SAME,
        baseline_physical=baseline_physical,
        comparison_physical=comparison_physical,
        baseline_parse_error=b_mod.parse_error,
        comparison_parse_error=c_mod.parse_error,
    )

    if b_mod.parse_error or c_mod.parse_error:
        fc.status = Status.PYTHON_PARSE_ERROR
        return fc

    fc.symbol_diffs = _compare_symbols(b_mod, c_mod)
    fc.module_logic_changed = (
        b_mod.module_logic_hash != c_mod.module_logic_hash
    )

    if fc.symbol_diffs or fc.module_logic_changed:
        has_logic = fc.module_logic_changed or any(
            d.status == Status.LOGIC_CHANGED for d in fc.symbol_diffs
        )
        fc.status = Status.LOGIC_CHANGED if has_logic else Status.FILE_CHANGED
    else:
        fc.status = Status.SAME

    return fc


def _import_module_name(import_key: str) -> str:
    return import_key.split(":", 1)[0]


def _module_to_logical_paths(module: str) -> list[str]:
    base = module.replace(".", "/")
    return [f"{base}.py", f"{base}/__init__.py"]


def _find_import_dependency_gaps(
    config: ScannerConfig,
    baseline_checkout: RepoCheckout,
    comparisons: list[FileComparison],
) -> list[ImportDependencyGap]:
    missing = {
        fc.logical_path
        for fc in comparisons
        if fc.status == Status.FILE_MISSING_FROM_COMPARISON
    }
    if not missing:
        return []

    gaps: list[ImportDependencyGap] = []
    seen: set[tuple[str, str, str]] = set()

    for fc in comparisons:
        if not fc.baseline_physical:
            continue
        b_path = baseline_checkout.path / fc.baseline_physical
        if b_path.suffix != ".py":
            continue

        mod = analyze_python(
            _read_module(b_path),
            fc.baseline_physical,
            token_rules=config.token_normalization,
        )
        if mod.parse_error:
            continue

        for imp in mod.imports:
            module = _import_module_name(imp)
            for candidate in _module_to_logical_paths(module):
                if candidate not in missing:
                    continue
                key = (fc.logical_path, candidate, imp)
                if key in seen:
                    continue
                seen.add(key)
                gaps.append(
                    ImportDependencyGap(
                        source_logical_path=fc.logical_path,
                        source_physical=fc.baseline_physical,
                        import_statement=imp,
                        missing_logical_path=candidate,
                    )
                )

    return sorted(
        gaps, key=lambda g: (g.source_logical_path, g.missing_logical_path)
    )


def _aggregate_counts(result: ScanResult) -> None:
    file_counts: dict[str, int] = {}
    symbol_counts: dict[str, int] = {}

    for fc in result.files:
        file_counts[fc.status.value] = file_counts.get(fc.status.value, 0) + 1
        for sd in fc.symbol_diffs:
            symbol_counts[sd.status.value] = (
                symbol_counts.get(sd.status.value, 0) + 1
            )

    result.counts = {
        "files_total": len(result.files),
        "import_dependency_gaps": len(result.import_dependency_gaps),
        **dict(sorted(file_counts.items())),
        **dict(sorted(symbol_counts.items())),
    }


def run_comparison(
    config: ScannerConfig,
    baseline_checkout: RepoCheckout,
    comparison_checkout: RepoCheckout,
) -> ScanResult:
    baseline_files = discover_files(
        baseline_checkout.path, baseline_checkout.name, config
    )
    comparison_files = discover_files(
        comparison_checkout.path, comparison_checkout.name, config
    )

    expected_specific = config.expected_specific_for(comparison_checkout.name)

    all_logical = sorted(set(baseline_files) | set(comparison_files))
    comparisons: list[FileComparison] = []

    for logical in all_logical:
        b_rec = baseline_files.get(logical)
        c_rec = comparison_files.get(logical)

        if b_rec and not c_rec:
            comparisons.append(
                FileComparison(
                    logical_path=logical,
                    status=Status.FILE_MISSING_FROM_COMPARISON,
                    baseline_physical=b_rec.physical_path,
                )
            )
            continue

        if c_rec and not b_rec:
            status = Status.FILE_EXTRA_IN_COMPARISON
            if c_rec.physical_path in expected_specific:
                status = Status.EXPECTED_REPO_SPECIFIC
            comparisons.append(
                FileComparison(
                    logical_path=logical,
                    status=status,
                    comparison_physical=c_rec.physical_path,
                )
            )
            continue

        assert b_rec and c_rec
        b_path = baseline_checkout.path / b_rec.physical_path
        c_path = comparison_checkout.path / c_rec.physical_path

        if b_path.suffix == ".py" and c_path.suffix == ".py":
            comparisons.append(
                _compare_python_files(
                    b_path,
                    c_path,
                    logical,
                    config,
                    b_rec.physical_path,
                    c_rec.physical_path,
                )
            )
        else:
            comparisons.append(
                FileComparison(
                    logical_path=logical,
                    status=Status.SAME,
                    baseline_physical=b_rec.physical_path,
                    comparison_physical=c_rec.physical_path,
                )
            )

    result = ScanResult(
        generated_at=datetime.now(timezone.utc).isoformat(),
        baseline=baseline_checkout.name,
        comparison=comparison_checkout.name,
        repos={
            baseline_checkout.name: {
                "url": baseline_checkout.url,
                "branch": baseline_checkout.branch,
                "commit": baseline_checkout.commit,
                "path": str(baseline_checkout.path),
            },
            comparison_checkout.name: {
                "url": comparison_checkout.url,
                "branch": comparison_checkout.branch,
                "commit": comparison_checkout.commit,
                "path": str(comparison_checkout.path),
            },
        },
        files=comparisons,
    )
    result.import_dependency_gaps = _find_import_dependency_gaps(
        config, baseline_checkout, comparisons
    )
    _aggregate_counts(result)
    return result
