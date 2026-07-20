# LEAPP Parity Report

![Parity summary](parity.1784555067.svg)

## Scan metadata

- **Generated**: 2026-07-20T13:44:27.326884+00:00
- **Baseline**: `ileapp`
- **Comparison**: `aleapp`

- **ileapp**: `04a359479446` on `main` ([https://github.com/abrignoni/iLEAPP.git](https://github.com/abrignoni/iLEAPP.git))
- **aleapp**: `07c5773ca3df` on `main` ([https://github.com/abrignoni/aLEAPP.git](https://github.com/abrignoni/aLEAPP.git))

## Overall counts

| Metric | Count |
|---|---:|
| Files scanned (union) | 59 |
| Same | 22 |
| Changed (logic/file) | 11 |
| Missing from comparison | 17 |
| Extra in comparison | 9 |
| Expected repo-specific | 0 |
| Parse errors | 0 |
| Import dependency gaps | 2 |

## File-level summary

| Status | Count |
|---|---:|
| same | 22 |
| logic_changed | 11 |
| file_missing_from_comparison | 17 |
| file_extra_in_comparison | 9 |

## Symbol-level summary

| Status | Count |
|---|---:|
| symbol_missing_from_comparison | 47 |
| symbol_extra_in_comparison | 26 |
| signature_changed | 3 |
| logic_changed | 28 |

## All compared files

59 file(s). See [details/file_list.md](details/file_list.md).

## Import dependency gaps

Baseline files that import modules missing from the comparison repo (for example `ilapfuncs.py` → `context.py`).

2 gap(s). See [details/import_dependency_gaps.md](details/import_dependency_gaps.md).

| Baseline file | Import | Missing in comparison |
|---|---|---|
| `ileappGUI.py` | `scripts.tz_offset:tzvalues` | `scripts/tz_offset.py` |
| `scripts/ccl_leveldb.py` | `scripts.ccl_simplesnappy` | `scripts/ccl_simplesnappy.py` |

## Top mismatches

| Logical path | Status | Baseline file | Comparison file |
|---|---|---|---|
| `main_entry.py` | logic_changed | `ileapp.py` | `aleapp.py` | (4 symbol diffs)
| `scripts/alternate_artifacts/appInventory.py` | logic_changed | `scripts/alternate_artifacts/appInventory.py` | `scripts/alternate_artifacts/appInventory.py` | (17 symbol diffs)
| `scripts/artifact_report.py` | logic_changed | `scripts/artifact_report.py` | `scripts/artifact_report.py` | (12 symbol diffs)
| `scripts/context.py` | logic_changed | `scripts/context.py` | `scripts/context.py` | (5 symbol diffs)
| `scripts/html_parts.py` | logic_changed | `scripts/html_parts.py` | `scripts/html_parts.py` |
| `scripts/ilapfuncs.py` | logic_changed | `scripts/ilapfuncs.py` | `scripts/ilapfuncs.py` | (40 symbol diffs)
| `scripts/lavafuncs.py` | logic_changed | `scripts/lavafuncs.py` | `scripts/lavafuncs.py` | (13 symbol diffs)
| `scripts/modules_to_exclude.py` | logic_changed | `scripts/modules_to_exclude.py` | `scripts/modules_to_exclude.py` |
| `scripts/report.py` | logic_changed | `scripts/report.py` | `scripts/report.py` | (3 symbol diffs)
| `scripts/search_files.py` | logic_changed | `scripts/search_files.py` | `scripts/search_files.py` | (10 symbol diffs)
| `scripts/version_info.py` | logic_changed | `scripts/version_info.py` | `scripts/version_info.py` |
| `ileappGUI.py` | file_missing_from_comparison | `ileappGUI.py` | `—` |
| `scripts/ccl_leveldb.py` | file_missing_from_comparison | `scripts/ccl_leveldb.py` | `—` |
| `leapp_functions/parsers/apple_atx.py` | file_missing_from_comparison | `leapp_functions/parsers/apple_atx.py` | `—` |
| `scripts/ccl/ccl_bplist.py` | file_missing_from_comparison | `scripts/ccl/ccl_bplist.py` | `—` |
| `scripts/ccl/ccl_segb1.py` | file_missing_from_comparison | `scripts/ccl/ccl_segb1.py` | `—` |
| `scripts/ccl/ccl_segb2.py` | file_missing_from_comparison | `scripts/ccl/ccl_segb2.py` | `—` |
| `scripts/ccl_segb/__init__.py` | file_missing_from_comparison | `scripts/ccl_segb/__init__.py` | `—` |
| `scripts/ccl_segb/ccl_segb.py` | file_missing_from_comparison | `scripts/ccl_segb/ccl_segb.py` | `—` |
| `scripts/ccl_segb/ccl_segb1.py` | file_missing_from_comparison | `scripts/ccl_segb/ccl_segb1.py` | `—` |

## Changed logic files

11 file(s). See [details/changed_logic.md](details/changed_logic.md).

<details>
<summary>Preview</summary>

### `main_entry.py`
- module-level logic changed
- logic changed: `create_profile`
- logic changed: `main`
- logic changed: `validate_args`
### `scripts/alternate_artifacts/appInventory.py`
- module-level logic changed
- only in ileapp: `_build_guid_map` — `def _build_guid_map(seeker)`
- only in ileapp: `_container_type_from_path` — `def _container_type_from_path(path)`
- logic changed: `_format_utc`
- only in ileapp: `_guids_from_device_path` — `def _guids_from_device_path(device_path)`
- logic changed: `_iter_extraction_files`
- only in ileapp: `_map_path_to_app` — `def _map_path_to_app(path, guid_map)`
- only in aleapp: `_map_path_to_package` — `def _map_path_to_package(path)`
- only in ileapp: `_parse_application_state` — `def _parse_application_state(db_path)`
- only in ileapp: `_parse_blob` — `def _parse_blob(appid, blob)`
- only in aleapp: `_parse_packages_xml` — `def _parse_packages_xml(file_path)`
- only in aleapp: `_read_build_prop` — `def _read_build_prop(file_path)`
- only in ileapp: `_read_container_metadata` — `def _read_container_metadata(plist_path)`
- only in aleapp: `_read_unix_time_ms` — `def _read_unix_time_ms(unix_time_ms)`
- logic changed: `_seeker_kind`
- logic changed: `appFileInventory`
- logic changed: `extractionInfo`
- logic changed: `installedAppInventory`
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
### `scripts/context.py`
- module-level logic changed

</details>

## Missing files

17 file(s). See [details/missing_files.md](details/missing_files.md).

<details>
<summary>Preview</summary>

- `ileappGUI.py` (baseline: `ileappGUI.py`)
- `leapp_functions/parsers/apple_atx.py` (baseline: `leapp_functions/parsers/apple_atx.py`)
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
- `scripts/ktx/ios_ktx2png.py` (baseline: `scripts/ktx/ios_ktx2png.py`)
- `scripts/test_artifacts/__init__.py` (baseline: `scripts/test_artifacts/__init__.py`)
- `scripts/test_artifacts/image_list.py` (baseline: `scripts/test_artifacts/image_list.py`)
- `scripts/tz_offset.py` (baseline: `scripts/tz_offset.py`)

</details>

## Extra files

9 file(s). See [details/extra_files.md](details/extra_files.md).

<details>
<summary>Preview</summary>

- `aleappGUI.py` (comparison: `aleappGUI.py`)
- `leapp_functions/__init__.py` (comparison: `leapp_functions/__init__.py`)
- `leapp_functions/app/__init__.py` (comparison: `leapp_functions/app/__init__.py`)
- `scripts/ccl/ccl_android_fcm_queued_messages.py` (comparison: `scripts/ccl/ccl_android_fcm_queued_messages.py`)
- `scripts/ccl/ccl_leveldb.py` (comparison: `scripts/ccl/ccl_leveldb.py`)
- `scripts/ccl/ccl_protobuff.py` (comparison: `scripts/ccl/ccl_protobuff.py`)
- `scripts/ccl/ccl_simplesnappy.py` (comparison: `scripts/ccl/ccl_simplesnappy.py`)
- `scripts/geo_utils.py` (comparison: `scripts/geo_utils.py`)
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

3 symbol(s). See [details/signature_changes.md](details/signature_changes.md).
