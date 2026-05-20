"""Clone and update LEAPP repositories."""

from __future__ import annotations

import subprocess
from dataclasses import dataclass
from pathlib import Path

from scanner.config import RepoConfig


@dataclass(frozen=True)
class RepoCheckout:
    name: str
    path: Path
    branch: str
    commit: str
    url: str


def _run(cmd: list[str], cwd: Path | None = None) -> str:
    result = subprocess.run(
        cmd,
        cwd=cwd,
        check=True,
        capture_output=True,
        text=True,
    )
    return (result.stdout or "").strip()


def ensure_repo(
    repo: RepoConfig,
    work_root: Path,
    *,
    update: bool = True,
    verbose: bool = False,
) -> RepoCheckout:
    dest = work_root / repo.name
    dest.parent.mkdir(parents=True, exist_ok=True)

    if dest.exists() and (dest / ".git").is_dir():
        if update:
            if verbose:
                print(f"Updating {repo.name} at {dest}")
            _run(["git", "fetch", "--all", "--prune"], cwd=dest)
            _run(["git", "pull", "--ff-only"], cwd=dest)
        elif verbose:
            print(f"Skipping update for {repo.name} (--no-update)")
    else:
        if verbose:
            print(f"Cloning {repo.name} from {repo.url}")
        _run(["git", "clone", "--depth", "1", repo.url, str(dest)])

    branch = _run(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=dest)
    if branch == "HEAD":
        branch = "detached"
    commit = _run(["git", "rev-parse", "HEAD"], cwd=dest)

    return RepoCheckout(
        name=repo.name,
        path=dest,
        branch=branch,
        commit=commit,
        url=repo.url,
    )
