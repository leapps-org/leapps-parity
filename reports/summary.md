# LEAPP Parity Report

![Parity summary](parity.1779299773.svg)

## Scan metadata

- **Generated**: 2026-05-20T17:56:13.083035+00:00
- **Baseline**: `ileapp`
- **Comparison**: `aleapp`

- **ileapp**: `fc78d9e0b03a` on `main` ([https://github.com/abrignoni/iLEAPP.git](https://github.com/abrignoni/iLEAPP.git))
- **aleapp**: `166233145694` on `main` ([https://github.com/abrignoni/aLEAPP.git](https://github.com/abrignoni/aLEAPP.git))

## Overall counts

| Metric | Count |
|---|---:|
| Files scanned (union) | 46 |
| Same | 14 |
| Changed (logic/file) | 11 |
| Missing from comparison | 15 |
| Extra in comparison | 6 |
| Expected repo-specific | 0 |
| Parse errors | 0 |
| Import dependency gaps | 6 |

## File-level summary

| Status | Count |
|---|---:|
| same | 14 |
| logic_changed | 11 |
| file_missing_from_comparison | 15 |
| file_extra_in_comparison | 6 |

## Symbol-level summary

| Status | Count |
|---|---:|
| symbol_missing_from_comparison | 40 |
| symbol_extra_in_comparison | 23 |
| signature_changed | 10 |
| logic_changed | 30 |

## All compared files

46 file(s). See [details/file_list.md](details/file_list.md).

## Import dependency gaps

Baseline files that import modules missing from the comparison repo (for example `ilapfuncs.py` → `context.py`).

6 gap(s). See [details/import_dependency_gaps.md](details/import_dependency_gaps.md).

| Baseline file | Import | Missing in comparison |
|---|---|---|
| `ileappGUI.py` | `scripts.context:Context` | `scripts/context.py` |
| `ileappGUI.py` | `scripts.tz_offset:tzvalues` | `scripts/tz_offset.py` |
| `main_entry.py` | `scripts.context:Context` | `scripts/context.py` |
| `scripts/ccl_leveldb.py` | `scripts.ccl_simplesnappy` | `scripts/ccl_simplesnappy.py` |
| `scripts/ilapfuncs.py` | `scripts.context:Context` | `scripts/context.py` |
| `scripts/lavafuncs.py` | `scripts.context:Context` | `scripts/context.py` |

## Top mismatches

| Logical path | Status | Baseline file | Comparison file |
|---|---|---|---|
| `main_entry.py` | logic_changed | `ileapp.py` | `aleapp.py` | (4 symbol diffs)
| `scripts/ilapfuncs.py` | logic_changed | `scripts/ilapfuncs.py` | `scripts/ilapfuncs.py` | (55 symbol diffs)
| `scripts/lavafuncs.py` | logic_changed | `scripts/lavafuncs.py` | `scripts/lavafuncs.py` | (7 symbol diffs)
| `scripts/artifact_report.py` | logic_changed | `scripts/artifact_report.py` | `scripts/artifact_report.py` | (13 symbol diffs)
| `scripts/html_parts.py` | logic_changed | `scripts/html_parts.py` | `scripts/html_parts.py` |
| `scripts/modules_to_exclude.py` | logic_changed | `scripts/modules_to_exclude.py` | `scripts/modules_to_exclude.py` |
| `scripts/plugin_loader.py` | logic_changed | `scripts/plugin_loader.py` | `scripts/plugin_loader.py` | (1 symbol diffs)
| `scripts/report.py` | logic_changed | `scripts/report.py` | `scripts/report.py` | (3 symbol diffs)
| `scripts/report_icons.py` | logic_changed | `scripts/report_icons.py` | `scripts/report_icons.py` |
| `scripts/search_files.py` | logic_changed | `scripts/search_files.py` | `scripts/search_files.py` | (20 symbol diffs)
| `scripts/version_info.py` | logic_changed | `scripts/version_info.py` | `scripts/version_info.py` |
| `ileappGUI.py` | file_missing_from_comparison | `ileappGUI.py` | `—` |
| `scripts/ccl_leveldb.py` | file_missing_from_comparison | `scripts/ccl_leveldb.py` | `—` |
| `scripts/ccl/ccl_bplist.py` | file_missing_from_comparison | `scripts/ccl/ccl_bplist.py` | `—` |
| `scripts/ccl/ccl_segb1.py` | file_missing_from_comparison | `scripts/ccl/ccl_segb1.py` | `—` |
| `scripts/ccl/ccl_segb2.py` | file_missing_from_comparison | `scripts/ccl/ccl_segb2.py` | `—` |
| `scripts/ccl_segb/__init__.py` | file_missing_from_comparison | `scripts/ccl_segb/__init__.py` | `—` |
| `scripts/ccl_segb/ccl_segb.py` | file_missing_from_comparison | `scripts/ccl_segb/ccl_segb.py` | `—` |
| `scripts/ccl_segb/ccl_segb1.py` | file_missing_from_comparison | `scripts/ccl_segb/ccl_segb1.py` | `—` |
| `scripts/ccl_segb/ccl_segb2.py` | file_missing_from_comparison | `scripts/ccl_segb/ccl_segb2.py` | `—` |

## Changed logic files

11 file(s). See [details/changed_logic.md](details/changed_logic.md).

<details>
<summary>Preview</summary>

### `main_entry.py`
- module-level logic changed
- logic changed: `create_profile`
- logic changed: `main`
- logic changed: `validate_args`
### `scripts/artifact_report.py`
- module-level logic changed
- only in aleapp: `ArtifactHtmlReport.add_chart` — `def add_chart(self, height=...)`
- only in aleapp: `ArtifactHtmlReport.add_chart_script` — `def add_chart_script(self, id, type, data, labels, title, xLabel, yLabel)`
- only in aleapp: `ArtifactHtmlReport.add_chat` — `def add_chat(self)`
- only in aleapp: `ArtifactHtmlReport.add_chat_invisble` — `def add_chat_invisble(self, id, text)`
- only in aleapp: `ArtifactHtmlReport.add_chat_window` — `def add_chat_window(self, head, body)`
- only in aleapp: `ArtifactHtmlReport.add_heat_map` — `def add_heat_map(self, json)`
- only in aleapp: `ArtifactHtmlReport.add_image_file` — `def add_image_file(self, param, param1, param2, secondImage=...)`
- only in aleapp: `ArtifactHtmlReport.add_json_to_artifact` — `def add_json_to_artifact(self, param, param1, hidden=..., idJ=..., gcm=...)`
- only in aleapp: `ArtifactHtmlReport.add_map` — `def add_map(self, param)`
- only in aleapp: `ArtifactHtmlReport.add_timeline` — `def add_timeline(self, id, dataDict)`
- only in aleapp: `ArtifactHtmlReport.add_timeline_script` — `def add_timeline_script(self)`
- only in aleapp: `ArtifactHtmlReport.filter_by_date` — `def filter_by_date(self, id, col1)`
- logic changed: `ArtifactHtmlReport.start_artifact_report`
### `scripts/html_parts.py`
- module-level logic changed
### `scripts/ilapfuncs.py`
- module-level logic changed
- logic changed: `MediaItem.__init__`
- logic changed: `MediaItem.set_values`
- logic changed: `MediaReferences.__init__`
- logic changed: `MediaReferences.set_values`
- logic changed: `OutputParameters.__init__`
- only in ileapp: `_check_in_media` — `def _check_in_media(media_id, source_path, is_embedded, name, media_data=..., converted_file_path=..., force_type=..., force_extension=..., force_creation_date=..., force_modification_date=...)`
- only in aleapp: `abxread` — `def abxread(in_path, multi_root)`
- logic changed: `artifact_processor`
- only in aleapp: `check_internet_connection` — `def check_internet_connection()`
- logic changed: `check_output_types`
- only in aleapp: `check_raw_fields` — `def check_raw_fields(latitude, longitude, c)`
- only in aleapp: `checkabx` — `def checkabx(in_path)`
- only in ileapp: `convert_bytes_to_unit` — `def convert_bytes_to_unit(size)`
- only in ileapp: `convert_cocoa_core_data_ts_to_utc` — `def convert_cocoa_core_data_ts_to_utc(cocoa_core_data_ts)`
- only in ileapp: `convert_log_ts_to_utc` — `def convert_log_ts_to_utc(str_dt)`
- only in ileapp: `convert_plist_date_to_timezone_offset` — `def convert_plist_date_to_timezone_offset(plist_date, timezone_offset)`

</details>

## Missing files

15 file(s). See [details/missing_files.md](details/missing_files.md).

<details>
<summary>Preview</summary>

- `ileappGUI.py` (baseline: `ileappGUI.py`)
- `scripts/ccl/ccl_bplist.py` (baseline: `scripts/ccl/ccl_bplist.py`)
- `scripts/ccl/ccl_segb1.py` (baseline: `scripts/ccl/ccl_segb1.py`)
- `scripts/ccl/ccl_segb2.py` (baseline: `scripts/ccl/ccl_segb2.py`)
- `scripts/ccl_leveldb.py` (baseline: `scripts/ccl_leveldb.py`)
- `scripts/ccl_segb/__init__.py` (baseline: `scripts/ccl_segb/__init__.py`)
- `scripts/ccl_segb/ccl_segb.py` (baseline: `scripts/ccl_segb/ccl_segb.py`)
- `scripts/ccl_segb/ccl_segb1.py` (baseline: `scripts/ccl_segb/ccl_segb1.py`)
- `scripts/ccl_segb/ccl_segb2.py` (baseline: `scripts/ccl_segb/ccl_segb2.py`)
- `scripts/ccl_segb/ccl_segb_common.py` (baseline: `scripts/ccl_segb/ccl_segb_common.py`)
- `scripts/ccl_simplesnappy.py` (baseline: `scripts/ccl_simplesnappy.py`)
- `scripts/chat_rendering.py` (baseline: `scripts/chat_rendering.py`)
- `scripts/context.py` (baseline: `scripts/context.py`)
- `scripts/ktx/ios_ktx2png.py` (baseline: `scripts/ktx/ios_ktx2png.py`)
- `scripts/tz_offset.py` (baseline: `scripts/tz_offset.py`)

</details>

## Extra files

6 file(s). See [details/extra_files.md](details/extra_files.md).

<details>
<summary>Preview</summary>

- `aleappGUI.py` (comparison: `aleappGUI.py`)
- `scripts/ccl/ccl_android_fcm_queued_messages.py` (comparison: `scripts/ccl/ccl_android_fcm_queued_messages.py`)
- `scripts/ccl/ccl_leveldb.py` (comparison: `scripts/ccl/ccl_leveldb.py`)
- `scripts/ccl/ccl_protobuff.py` (comparison: `scripts/ccl/ccl_protobuff.py`)
- `scripts/ccl/ccl_simplesnappy.py` (comparison: `scripts/ccl/ccl_simplesnappy.py`)
- `scripts/googleKeepNotes.py` (comparison: `scripts/googleKeepNotes.py`)

</details>

## Expected repo-specific files

0 file(s).

## Parse errors

0 file(s). See [details/parse_errors.md](details/parse_errors.md).

<details>
<summary>Preview</summary>

_None._

</details>

## Signature changes

10 symbol(s). See [details/signature_changes.md](details/signature_changes.md).
