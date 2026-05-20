# LEAPP Parity Scanner

Compare **core/framework Python code** across LEAPP forensic tool repositories. The scanner clones configured repos, maps equivalent paths (for example `ileapp.py` and `aleapp.py`), and reports structural and logic differences while ignoring comments, formatting, docstrings, and configurable tool/platform tokens.

## What it compares

- Shared Python under configured include paths (root `*.py`, `scripts/`, `admin/`, libraries)
- Missing or extra files (with logical path aliases)
- Top-level functions and classes, class methods, signatures, and normalized executable AST logic
- Expected repo-specific files (configured separately, not counted as failures)

## What it does **not** compare yet

- **Artifact modules** under `scripts/artifacts/` (explicitly excluded)
- Tests, docs, assets, build output
- Non-Python assets or runtime data

## Requirements

- Python 3.11+
- Git (to clone/update LEAPP repos)
- PyYAML (`pip install -r requirements.txt`)

## Local setup

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Local run

```bash
python -m scanner.run
```

The scanner loads `config/repos.yml` from the project root by default. Report output always goes to `reports/` (configured via `output_dir` in the YAML).

Useful options:

| Flag | Description |
|------|-------------|
| `--config PATH` | Override config file path |
| `--no-update` | Skip `git pull` on existing checkouts in `.work/repos/` |
| `--baseline ileapp` | Baseline repo name (default from config) |
| `--comparison aleapp` | Comparison repo name (default from config) |
| `--json-only` | Write `results.json` only |
| `--verbose` | Progress on stderr |

Repos are cloned into `.work/repos/{repo_name}/`.

## Output

Reports are written to `reports/`:

| File | Description |
|------|-------------|
| `results.json` | Machine-readable full scan results |
| `summary.md` | Human-readable overview (embeds versioned `parity.<timestamp>.svg`) |
| `parity.<timestamp>.svg` | Bar chart of file-level status counts (new file each run) |
| `details/*.md` | Drill-down lists (file list, changed logic, signatures, parse errors, etc.) |

## GitHub Actions

Workflow: [`.github/workflows/scan.yml`](.github/workflows/scan.yml)

- Runs **weekly** (Mondays 12:00 UTC) and on **manual** `workflow_dispatch`
- Installs Python 3.11 and dependencies
- Runs the scanner against configured repos
- **Commits** updated files under `reports/` when they change

Ensure the default `GITHUB_TOKEN` has permission to push (workflow sets `contents: write`).

## Configuration (`config/repos.yml`)

### Output

```yaml
output_dir: reports
```

Reports are always written under this directory (relative to the project root).

### Repos

```yaml
repos:
  ileapp:
    url: https://github.com/abrignoni/iLEAPP.git
    baseline: true
  aleapp:
    url: https://github.com/abrignoni/aLEAPP.git
```

### Include / exclude globs

Controls which Python files are discovered. Artifact paths are excluded by default.

### Path aliases

Maps repo-specific filenames to one logical path for comparison:

```yaml
path_aliases:
  ileapp.py: main_entry.py
  aleapp.py: main_entry.py
```

Reports show both the **logical** path and each repo’s **physical** filename.

### Expected repo-specific files

Files that should exist only in one repo (not parity gaps):

```yaml
expected_repo_specific:
  aleapp:
    - "scripts/binary_xml.py"
```

Use the real path as it appears in that repo (before aliasing). Status: `expected_repo_specific`.

### Token normalization

Replaces tool/platform strings in source before AST comparison:

```yaml
token_normalization:
  - pattern: "(?i)ileapp"
    replacement: "{TOOL_NAME}"
```

## Adding another LEAPP repo

1. Add a `repos:` entry with `url` and `baseline: false` (unless it becomes the new baseline).
2. Add any entry-file aliases under `path_aliases` (same pattern as `ileapp.py` / `aleapp.py`).
3. List `expected_repo_specific` paths for that repo if needed.
4. Run with `--baseline ileapp --comparison myrepo` (or set defaults in the YAML).

## Project layout

```
config/repos.yml
scanner/
  config.py      # YAML loading
  git_ops.py     # clone / pull
  files.py       # discovery, aliases, globs
  python_ast.py  # AST parse, normalize, hash
  compare.py     # diff engine
  report_markdown.py
  report_svg.py
  run.py         # CLI
reports/
.github/workflows/scan.yml
```

## License

Use and modify as needed for LEAPP maintenance workflows.
