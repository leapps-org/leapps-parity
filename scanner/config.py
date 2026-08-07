"""Load and validate scanner configuration from YAML."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml


@dataclass(frozen=True)
class RepoConfig:
    name: str
    url: str
    baseline: bool = False


@dataclass(frozen=True)
class TokenRule:
    pattern: str
    replacement: str


@dataclass
class ScannerConfig:
    repos: dict[str, RepoConfig]
    default_baseline: str
    default_comparison: str
    include: list[str]
    exclude: list[str]
    path_aliases: dict[str, str]
    expected_repo_specific: dict[str, list[str]]
    expected_baseline_only: dict[str, list[str]]
    token_normalization: list[TokenRule]
    config_path: Path
    project_root: Path
    output_dir: Path

    def repo(self, name: str) -> RepoConfig:
        if name not in self.repos:
            raise KeyError(f"Unknown repo: {name}")
        return self.repos[name]

    def expected_specific_for(self, repo_name: str) -> set[str]:
        paths = self.expected_repo_specific.get(repo_name, [])
        return {self._normalize_expected_path(p) for p in paths}

    def expected_baseline_only_for(self, repo_name: str) -> set[str]:
        """Files that legitimately exist only in this repo when it is the baseline.

        Applied to the file-missing-from-comparison branch, so an entry is only
        honoured for a pair where the file is genuinely absent. Listing a file that
        the comparison does have has no effect on that pair.
        """
        paths = self.expected_baseline_only.get(repo_name, [])
        return {self._normalize_expected_path(p) for p in paths}

    @staticmethod
    def _normalize_expected_path(path: str) -> str:
        return path.replace("\\", "/").lstrip("./")


def load_config(path: str | Path) -> ScannerConfig:
    config_path = Path(path).resolve()
    with config_path.open(encoding="utf-8") as f:
        raw: dict[str, Any] = yaml.safe_load(f) or {}

    repos: dict[str, RepoConfig] = {}
    for name, spec in (raw.get("repos") or {}).items():
        if not isinstance(spec, dict):
            raise ValueError(f"Invalid repo spec for {name}")
        repos[name] = RepoConfig(
            name=name,
            url=str(spec["url"]),
            baseline=bool(spec.get("baseline", False)),
        )

    token_rules = [
        TokenRule(pattern=str(r["pattern"]), replacement=str(r["replacement"]))
        for r in raw.get("token_normalization") or []
        if isinstance(r, dict) and "pattern" in r and "replacement" in r
    ]

    path_aliases = {
        str(k): str(v) for k, v in (raw.get("path_aliases") or {}).items()
    }

    expected: dict[str, list[str]] = {}
    for repo_name, paths in (raw.get("expected_repo_specific") or {}).items():
        expected[str(repo_name)] = [str(p) for p in paths or []]

    project_root = config_path.parent.parent
    output_name = str(raw.get("output_dir", "reports"))
    output_dir = Path(output_name)
    if not output_dir.is_absolute():
        output_dir = (project_root / output_dir).resolve()

    return ScannerConfig(
        repos=repos,
        default_baseline=str(raw.get("default_baseline", "ileapp")),
        default_comparison=str(raw.get("default_comparison", "aleapp")),
        include=[str(p) for p in raw.get("include") or ["*.py"]],
        exclude=[str(p) for p in raw.get("exclude") or []],
        path_aliases=path_aliases,
        expected_repo_specific=expected,
        expected_baseline_only={
            str(k): [str(p) for p in (v or [])]
            for k, v in (raw.get("expected_baseline_only") or {}).items()
        },
        token_normalization=token_rules,
        config_path=config_path,
        project_root=project_root,
        output_dir=output_dir,
    )
