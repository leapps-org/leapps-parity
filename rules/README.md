# Shared Claude Code rules and skills

Canonical copies of the context that is synced into the LEAPP repositories, so contributors
working with an AI coding agent inherit the same project context regardless of which repo
they cloned.

Two kinds of file are synced, and they load differently. **Rules** are context: they load at
session start, or when Claude touches a file matching their `paths:` frontmatter. **Skills**
are procedures: their body loads only when the skill is invoked, so a long one costs nothing
until it is needed. Anything multi-step belongs in a skill, not a rule.

## Four sets, two canonical homes

| set | canonical location | synced to | lands in |
| --- | --- | --- | --- |
| `rules/leapp/leapp-*.md` | **this repo** | the five extractors | `<repo>/.claude/rules/` |
| `skills/leapp-*/` | **this repo** | the five extractors | `<repo>/.claude/skills/` |
| `lava-*.md` | `.claude/rules/` in the **LAVA repo** | the five extractors | `<repo>/.claude/rules/` |
| `lava-*/` skills | `.claude/skills/` in the **LAVA repo** | the five extractors | `<repo>/.claude/skills/` |

`leapp-*` governs the artifact module architecture, so it goes to the five extractors only.
LAVA has no `scripts/artifacts/` and those rules do not apply to it.

`lava-*` covers the output contract between the extractors and the viewer. It is canonical
in LAVA because that is where the schema lives. LAVA keeps its own copy as the source and is
not a sync destination.

## Editing

**Edit the canonical copy, never a synced one.** Every synced file carries an HTML comment
saying so. A change made in a destination repo is silently reverted the next time the sync
runs.

Each repo may also carry its own `<repo>-*.md` rules and `<repo>-*` skills. Those are local,
are not synced, and are not touched by this tool. The prefix is what marks a file as
managed, so do not name a local file `leapp-` or `lava-`.

## Usage

The script assumes the repo checkouts are siblings of this one. Pass `--root` if they are
somewhere else.

```bash
python3 scanner/sync_shared.py --check          # report drift, exit 1 if any
python3 scanner/sync_shared.py --write          # push canonical copies out
python3 scanner/sync_shared.py --check --json   # machine-readable
```

`--check` compares content by hash and reports two states: `DRIFTED` for a destination whose
content differs, and `MISSING` for one that does not exist. It never fetches, so run it
against checkouts you have already updated or it will compare against a stale tree.

## Why not symlinks

`.claude/rules/` does support symlinks, but these repos are cloned by contributors. A
symlink pointing into a maintainer's home directory resolves for exactly one person and
breaks for everyone else, so the files are real copies kept in step by this script.
