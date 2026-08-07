# leapps-parity

Two jobs in one repo, both about keeping the LEAPP ecosystem consistent:

1. **A parity scanner** that compares core framework Python across the LEAPP repos and
   reports where they have drifted.
2. **The canonical home for shared Claude Code context**, synced out to the other six repos.

## Editing here changes six repositories

`rules/leapp/` and `skills/leapp-*/` are the **source of truth**, not copies. A change here
propagates to iLEAPP, ALEAPP, RLEAPP, VLEAPP and DLEAPP the next time the sync runs, and it
overwrites whatever is in those repos.

The reverse is also true and catches people out: editing `.claude/rules/leapp-ci.md` inside
iLEAPP looks like it worked and is silently reverted on the next sync. Every synced file
carries an HTML comment saying so.

`lava-*` rules and skills are canonical in the **LAVA** repo, not here, because that is
where the schema lives. This repo does not receive them.

See `rules/README.md` for the full arrangement, and run
`python3 scanner/sync_shared.py --check` before assuming anything is in sync.

## The scanner is pairwise

One baseline against one comparison per run. `config/repos.yml` is a registry of
addressable repos, **not** a scan set: adding a repo there does not cause it to be scanned.
CI loops iLEAPP against each of the other four, because iLEAPP is where shared
infrastructure lands first, which makes "missing from the comparison" the useful direction.

Each run writes to `reports/<baseline>-vs-<comparison>/`, so pairs do not overwrite each
other. `reports/README.md` explains how to read the output.

## Two config keys that are easy to confuse

- **`expected_repo_specific`** suppresses files that exist only in the **comparison**. It is
  keyed by the comparison repo name and never applies to missing files.
- **`expected_baseline_only`** suppresses files that exist only in the **baseline**. It is
  honoured only for a pair where the file is genuinely absent, so listing a file that some
  comparison does have has no effect on that pair.

Getting these backwards produces config that looks right and does nothing. Without
`expected_baseline_only` the scan reports about 30 known-correct divergences per pair,
mostly iOS-only parsers and the vendored protobuf that three cores dropped deliberately.

**Suppression never disables import-gap detection.** A file being absent by design does not
make it safe for shared code to import, so `_find_import_dependency_gaps` deliberately scans
suppressed baseline-only files too. Do not "simplify" that back to a single status check.

## Working here

`scripts/artifacts/**` is excluded from comparison on purpose. Artifact modules are expected
to differ and there are hundreds of them; cross-core artifact drift is handled by the
`leapp-cross-core` rule and the `leapp-sweep-siblings` skill instead.

There is no test suite. Verify a scanner change by running all four pairs and reading the
counts, not just by checking the run exits zero. `.work/` holds the clones the scanner
makes and is gitignored, as is `.venv/`.
