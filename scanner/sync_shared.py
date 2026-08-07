#!/usr/bin/env python3
"""Sync shared Claude Code rules and skills across the LEAPP repositories.

Two canonical sources:

  leapp-*   canonical HERE   rules/leapp/*.md  and  skills/leapp-*/
            pushed to the five extractors only (they govern artifact modules)
  lava-*    canonical in the LAVA repo, .claude/rules/lava-*.md
            pushed to the five extractors; LAVA itself is the source

Destinations are <repo>/.claude/rules/ and <repo>/.claude/skills/.

Usage:
  sync_shared.py --check          report drift, exit 1 if any (for CI)
  sync_shared.py --write          overwrite destinations from canonical
  sync_shared.py --check --json   machine-readable drift report

Repos are assumed to be siblings of this one; pass --root otherwise. Nothing is
fetched, so run against checkouts you have already updated or you will compare
against a stale tree.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path

EXTRACTORS = ["iLEAPP", "ALEAPP", "RLEAPP", "VLEAPP", "DLEAPP"]
LAVA = "LAVA"
ALL_REPOS = EXTRACTORS + [LAVA]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sync_sets(root: Path, self_repo: Path):
    """(label, canonical_base, iterator of relative paths, dest_subdir, dest_repos)"""
    return [
        ("leapp-rules", self_repo / "rules" / "leapp",
         lambda b: sorted(p.relative_to(b) for p in b.glob("leapp-*.md") if p.is_file()),
         ".claude/rules", EXTRACTORS),
        ("lava-rules", root / LAVA / ".claude" / "rules",
         lambda b: sorted(p.relative_to(b) for p in b.glob("lava-*.md") if p.is_file()),
         ".claude/rules", EXTRACTORS),
        ("leapp-skills", self_repo / "skills",
         lambda b: sorted(p.relative_to(b) for d in b.glob("leapp-*")
                          if d.is_dir() for p in d.rglob("*") if p.is_file()),
         ".claude/skills", EXTRACTORS),
        ("lava-skills", root / LAVA / ".claude" / "skills",
         lambda b: sorted(p.relative_to(b) for d in b.glob("lava-*")
                          if d.is_dir() for p in d.rglob("*") if p.is_file()),
         ".claude/skills", EXTRACTORS),
    ]


def collect(root: Path, self_repo: Path, skip_repos: set[str] | None = None):
    skip_repos = skip_repos or set()
    for label, base, lister, dest_sub, dests in sync_sets(root, self_repo):
        # A set whose canonical source is in an unavailable repo cannot be checked at
        # all; one whose destination is unavailable is checked for the rest.
        if any(f"/{r}/" in f"{base}/" for r in skip_repos):
            continue
        dests = [d for d in dests if d not in skip_repos]
        if not dests:
            continue
        if not base.is_dir():
            yield label, base, None, "missing-canonical-dir"
            continue
        rels = lister(base)
        if not rels:
            yield label, base, None, "no-canonical-files"
            continue
        for rel in rels:
            src = base / rel
            for repo in dests:
                dst = root / repo / dest_sub / rel
                if not dst.exists():
                    state = "missing"
                elif sha(dst) != sha(src):
                    state = "drifted"
                else:
                    state = "ok"
                yield label, src, dst, state


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = ap.add_mutually_exclusive_group(required=True)
    mode.add_argument("--check", action="store_true",
                      help="report drift and exit nonzero if any is found")
    mode.add_argument("--write", action="store_true",
                      help="overwrite destinations from the canonical copies")
    ap.add_argument("--root", type=Path, default=None,
                    help="directory containing the repo checkouts "
                         "(default: the parent of this repo)")
    ap.add_argument("--json", action="store_true", help="machine-readable output")
    ap.add_argument("--skip-missing", action="store_true",
                    help="skip sets whose repo is not checked out instead of failing. "
                         "Skips are reported loudly and never counted as in sync")
    args = ap.parse_args()

    self_repo = Path(__file__).resolve().parent.parent
    root = (args.root or self_repo.parent).resolve()

    missing = [r for r in ALL_REPOS if not (root / r).is_dir()]
    if missing and not args.skip_missing:
        print(f"error: no checkout for {', '.join(missing)} under {root}", file=sys.stderr)
        print("hint: pass --root <dir containing the checkouts>, or --skip-missing",
              file=sys.stderr)
        return 2

    results = list(collect(root, self_repo, skip_repos=set(missing)))
    if missing:
        # Loud, because a check that silently covers less than it claims is worse
        # than no check at all.
        for repo in missing:
            print(f"SKIPPED  no {repo} checkout: any set canonical in or synced to "
                  f"it was NOT verified", file=sys.stderr)
    fatal = [r for r in results if r[3] in ("missing-canonical-dir", "no-canonical-files")]
    problems = [r for r in results if r[3] != "ok"]

    if args.json:
        print(json.dumps([{"set": s, "canonical": str(c),
                           "dest": str(d) if d else None, "state": st}
                          for s, c, d, st in results], indent=2))
    else:
        for label, src, dst, state in results:
            if dst is None:
                print(f"FATAL    [{label}] {state}: {src}")
            elif state != "ok":
                print(f"{state.upper():8} {dst.relative_to(root)}")
        print(f"\n{len(results) - len(problems)} in sync, "
              f"{len(problems)} needing attention")

    if fatal:
        return 2

    if args.write:
        wrote = 0
        for _, src, dst, state in results:
            if dst is None or state == "ok":
                continue
            dst.parent.mkdir(parents=True, exist_ok=True)
            dst.write_bytes(src.read_bytes())
            wrote += 1
        print(f"wrote {wrote} file(s)")
        return 0

    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
