# Parity reports

One directory per comparison, named `<baseline>-vs-<comparison>`. The scanner is
pairwise, so each directory is a separate run. CI compares iLEAPP against each of the
other four cores, because iLEAPP is where shared infrastructure lands first: that makes
"missing from the comparison" the direction worth reading.

Each directory holds `summary.md` (start here), `results.json`, a `details/` breakdown
and a parity SVG.

## Reading a report

**`logic_changed`** is the main signal. It means both repos have the file and the
normalized AST differs, after tool and platform tokens are neutralised. Some of it is
legitimate divergence; some of it is a fix that landed in one core and not the others.

**`import_dependency_gaps`** is the sharpest signal. It means a file the comparison
*does* have imports something it does *not* have. That is usually a real defect rather
than a difference of opinion.

**`expected_repo_specific`** is configured, not detected. Those files are known-correct
divergence: iOS-only parsers, the vendored protobuf that RLEAPP, VLEAPP and DLEAPP
dropped in the CVE cleanup, and each core's own app helpers. They are counted so the
suppression stays visible rather than silent. If a file in that list stops being correct
divergence, remove it from `config/repos.yml` rather than ignoring the report.

Note that a file suppressed as expected-baseline-only is still scanned for import gaps.
It being absent by design does not make it safe for shared code to import.

**`symbol_extra_in_comparison`** counts symbols inside *shared* files that only the
comparison defines. It is not about extra files. Classified by hand on 2026-08-07:

- ALEAPP's 28 are mostly legitimate: Android-only `ilapfuncs` helpers (ABX readers,
  protobuf decode) and `ArtifactHtmlReport` display methods (charts, maps, chat) that
  iLEAPP's report class never grew. One cluster was a live finding: an uncalled
  Nominatim geocoding group that contradicts the zero-remote-destinations policy.
- RLEAPP/VLEAPP/DLEAPP share a returns-parsing helper set (`usergen`, `ipgen`,
  `html2csv`, hash gathering) that iLEAPP has no use for; DLEAPP adds its Signal
  key-input plumbing. All legitimate.
- `insert_sidebar_code` appearing as extra in all four siblings was the inverted tell of
  real drift: iLEAPP had *replaced* it with a streaming version to fix a MemoryError on
  multi-GB pages (issue #1746), and no sibling got the fix. **Ported and closed
  2026-08-07**; the scan reports zero sidebar symbol diffs across all four pairs, which
  is what closing a finding should look like here.

The lesson generalises: a symbol extra in the comparison can mean the **baseline renamed
or replaced it**, so read the paired missing-symbol diff in the same file before
classifying anything as harmless divergence.

## What is not compared

`scripts/artifacts/**` is excluded. Artifact modules are expected to differ, and there
are hundreds of them. Cross-core artifact drift is a separate problem, handled by the
`leapp-cross-core` rule and the `leapp-sweep-siblings` skill rather than by this scanner.

Tests, docs, assets and build output are excluded too.
