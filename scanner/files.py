"""Discover and map Python files with include/exclude rules and path aliases."""

from __future__ import annotations

import fnmatch
from dataclasses import dataclass
from pathlib import Path

from scanner.config import ScannerConfig


@dataclass(frozen=True)
class FileRecord:
    repo_name: str
    physical_path: str
    logical_path: str


def _normalize_path(path: str) -> str:
    return path.replace("\\", "/").lstrip("./")


def _matches_pattern(rel_path: str, pattern: str) -> bool:
    pattern = _normalize_path(pattern)
    rel_path = _normalize_path(rel_path)

    if "**" in pattern:
        return fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(
            rel_path, pattern.replace("**/", "")
        )

    if pattern.endswith("/**"):
        prefix = pattern[:-3]
        return rel_path == prefix or rel_path.startswith(prefix + "/")

    if "/" not in pattern and "*" not in pattern:
        return rel_path == pattern or rel_path.endswith("/" + pattern)

    return fnmatch.fnmatch(rel_path, pattern) or fnmatch.fnmatch(
        Path(rel_path).name, pattern
    )


def _is_excluded(rel_path: str, exclude: list[str]) -> bool:
    return any(_matches_pattern(rel_path, pat) for pat in exclude)


def _is_included(rel_path: str, include: list[str]) -> bool:
    return any(_matches_pattern(rel_path, pat) for pat in include)


def to_logical_path(
    rel_path: str,
    repo_name: str,
    path_aliases: dict[str, str],
) -> str:
    rel_path = _normalize_path(rel_path)
    basename = Path(rel_path).name
    if basename in path_aliases:
        alias = path_aliases[basename]
        parent = str(Path(rel_path).parent)
        if parent in (".", ""):
            return alias
        return _normalize_path(f"{parent}/{alias}")
    return rel_path


def discover_files(
    repo_root: Path,
    repo_name: str,
    config: ScannerConfig,
) -> dict[str, FileRecord]:
    """Return logical_path -> FileRecord for all included Python files."""
    records: dict[str, FileRecord] = {}
    repo_root = repo_root.resolve()

    for path in sorted(repo_root.rglob("*.py")):
        if not path.is_file():
            continue
        try:
            rel = _normalize_path(str(path.relative_to(repo_root)))
        except ValueError:
            continue

        if _is_excluded(rel, config.exclude):
            continue
        if not _is_included(rel, config.include):
            continue

        logical = to_logical_path(rel, repo_name, config.path_aliases)
        records[logical] = FileRecord(
            repo_name=repo_name,
            physical_path=rel,
            logical_path=logical,
        )

    return records
