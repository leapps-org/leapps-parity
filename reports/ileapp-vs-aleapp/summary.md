# LEAPP Parity Report

![Parity summary](parity.1792432387.svg)

## Scan metadata

- **Generated**: 2026-10-19T17:53:07.200725+00:00
- **Baseline**: `ileapp`
- **Comparison**: `aleapp`

- **ileapp**: `16f2bc480295` on `main` ([https://github.com/abrignoni/iLEAPP.git](https://github.com/abrignoni/iLEAPP.git))
- **aleapp**: `1eae6b9dcca1` on `main` ([https://github.com/abrignoni/aLEAPP.git](https://github.com/abrignoni/aLEAPP.git))

## Overall counts

| Metric | Count |
|---|---:|
| Files scanned (union) | 84 |
| Same | 41 |
| Changed (logic/file) | 14 |
| Missing from comparison | 3 |
| Extra in comparison | 7 |
| Expected repo-specific | 19 |
| Parse errors | 0 |
| Import dependency gaps | 4 |

## File-level summary

| Status | Count |
|---|---:|
| same | 41 |
| logic_changed | 14 |
| file_missing_from_comparison | 3 |
| file_extra_in_comparison | 7 |
| expected_repo_specific | 19 |

## Symbol-level summary

| Status | Count |
|---|---:|
| symbol_missing_from_comparison | 60 |
| symbol_extra_in_comparison | 27 |
| signature_changed | 4 |
| logic_changed | 28 |

## All compared files

84 file(s). See [details/file_list.md](details/file_list.md).

## Import dependency gaps

Baseline files that import modules missing from the comparison repo (for example `ilapfuncs.py` → `context.py`).

4 gap(s). See [details/import_dependency_gaps.md](details/import_dependency_gaps.md).

| Baseline file | Import | Missing in comparison |
|---|---|---|
| `main_entry.py` | `scripts.ios_keychain:report_supplied_keychain` | `scripts/ios_keychain.py` |
| `main_gui.py` | `scripts.tz_offset:tzvalues` | `scripts/tz_offset.py` |
| `scripts/ccl_leveldb.py` | `scripts.ccl_simplesnappy` | `scripts/ccl_simplesnappy.py` |
| `scripts/unifiedlogs.py` | `scripts.log_filter:accelerate_query` | `scripts/log_filter.py` |

## Top mismatches

| Logical path | Status | Baseline file | Comparison file |
|---|---|---|---|
| `main_entry.py` | logic_changed | `ileapp.py` | `aleapp.py` | (4 symbol diffs)
| `main_gui.py` | logic_changed | `ileappGUI.py` | `aleappGUI.py` | (10 symbol diffs)
| `packaging/build.py` | logic_changed | `packaging/build.py` | `packaging/build.py` | (10 symbol diffs)
| `packaging/entrypoint.py` | logic_changed | `packaging/entrypoint.py` | `packaging/entrypoint.py` | (1 symbol diffs)
| `scripts/alternate_artifacts/appInventory.py` | logic_changed | `scripts/alternate_artifacts/appInventory.py` | `scripts/alternate_artifacts/appInventory.py` | (17 symbol diffs)
| `scripts/artifact_report.py` | logic_changed | `scripts/artifact_report.py` | `scripts/artifact_report.py` | (12 symbol diffs)
| `scripts/context.py` | logic_changed | `scripts/context.py` | `scripts/context.py` | (7 symbol diffs)
| `scripts/html_parts.py` | logic_changed | `scripts/html_parts.py` | `scripts/html_parts.py` |
| `scripts/ilapfuncs.py` | logic_changed | `scripts/ilapfuncs.py` | `scripts/ilapfuncs.py` | (43 symbol diffs)
| `scripts/lavafuncs.py` | logic_changed | `scripts/lavafuncs.py` | `scripts/lavafuncs.py` | (1 symbol diffs)
| `scripts/modules_to_exclude.py` | logic_changed | `scripts/modules_to_exclude.py` | `scripts/modules_to_exclude.py` |
| `scripts/report.py` | logic_changed | `scripts/report.py` | `scripts/report.py` | (2 symbol diffs)
| `scripts/search_files.py` | logic_changed | `scripts/search_files.py` | `scripts/search_files.py` | (12 symbol diffs)
| `scripts/version_info.py` | logic_changed | `scripts/version_info.py` | `scripts/version_info.py` |
| `scripts/log_filter.py` | file_missing_from_comparison | `scripts/log_filter.py` | `—` |
| `scripts/webkit_helpers.py` | file_missing_from_comparison | `scripts/webkit_helpers.py` | `—` |
| `scripts/webkit_media_cache.py` | file_missing_from_comparison | `scripts/webkit_media_cache.py` | `—` |
| `scripts/ccl/ccl_android_fcm_queued_messages.py` | file_extra_in_comparison | `—` | `scripts/ccl/ccl_android_fcm_queued_messages.py` |
| `scripts/ccl/ccl_leveldb.py` | file_extra_in_comparison | `—` | `scripts/ccl/ccl_leveldb.py` |
| `scripts/ccl/ccl_protobuff.py` | file_extra_in_comparison | `—` | `scripts/ccl/ccl_protobuff.py` |

## Changed logic files

14 file(s). See [details/changed_logic.md](details/changed_logic.md).

<details>
<summary>Preview</summary>

### `main_entry.py`
- module-level logic changed
- logic changed: `main`
- logic changed: `validate_args`
- only in ileapp: `version_readers_first` — `def version_readers_first(plugins)`
### `main_gui.py`
- module-level logic changed
- logic changed: `ValidateInput`
- logic changed: `case_data`
- only in ileapp: `clear_keychain` — `def clear_keychain()`
- logic changed: `filter_modules`
- logic changed: `finish_crunch`
- logic changed: `open_settings_window`
- logic changed: `pickModules`
- logic changed: `process`
- only in ileapp: `select_keychain` — `def select_keychain()`
### `packaging/build.py`
- module-level logic changed
- only in aleapp: `_installed_msl_plugins` — `def _installed_msl_plugins() -> ...`
- only in ileapp: `_unifiedlog_binary` — `def _unifiedlog_binary() -> ...`
- logic changed: `appimage_desktop_entry`
- logic changed: `build_exe`
- only in ileapp: `bundle_binaries` — `def bundle_binaries() -> ...`
- logic changed: `bundle_datas`
- only in ileapp: `bundled_bin_dir` — `def bundled_bin_dir() -> ...`
- only in aleapp: `bundled_root` — `def bundled_root() -> ...`
- only in aleapp: `install_commands` — `def install_commands(python) -> ...`
- logic changed: `smoke`
### `packaging/entrypoint.py`
- module-level logic changed
- logic changed: `main`
### `scripts/alternate_artifacts/appInventory.py`
- module-level logic changed
- only in ileapp: `_build_guid_map` — `def _build_guid_map(seeker)`
- only in ileapp: `_container_type_from_path` — `def _container_type_from_path(path)`
- logic changed: `_format_utc`
- only in ileapp: `_guids_from_device_path` — `def _guids_from_device_path(device_path)`
- logic changed: `_iter_extraction_files`
- only in ileapp: `_map_path_to_app` — `def _map_path_to_app(path, guid_map)`
- only in aleapp: `_map_path_to_package` — `def _map_path_to_package(path)`

</details>

## Missing files

3 file(s). See [details/missing_files.md](details/missing_files.md).

<details>
<summary>Preview</summary>

- `scripts/log_filter.py` (baseline: `scripts/log_filter.py`)
- `scripts/webkit_helpers.py` (baseline: `scripts/webkit_helpers.py`)
- `scripts/webkit_media_cache.py` (baseline: `scripts/webkit_media_cache.py`)

</details>

## Extra files

7 file(s). See [details/extra_files.md](details/extra_files.md).

<details>
<summary>Preview</summary>

- `leapp_functions/parsers/apple_atx.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl/ccl_android_fcm_queued_messages.py` (comparison: `scripts/ccl/ccl_android_fcm_queued_messages.py`)
- `scripts/ccl/ccl_bplist.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl/ccl_leveldb.py` (comparison: `scripts/ccl/ccl_leveldb.py`)
- `scripts/ccl/ccl_protobuff.py` (comparison: `scripts/ccl/ccl_protobuff.py`)
- `scripts/ccl/ccl_segb1.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl/ccl_segb2.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl/ccl_simplesnappy.py` (comparison: `scripts/ccl/ccl_simplesnappy.py`)
- `scripts/ccl_leveldb.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl_segb/__init__.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl_segb/ccl_segb.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl_segb/ccl_segb1.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl_segb/ccl_segb2.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl_segb/ccl_segb_common.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl_simplesnappy.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/chat_rendering.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/chromium_sync_data.py` (comparison: `scripts/chromium_sync_data.py`)
- `scripts/geo_utils.py` _(expected repo-specific)_ (comparison: `scripts/geo_utils.py`)
- `scripts/ios_keychain.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ktx/ios_ktx2png.py` _(expected repo-specific)_ (comparison: `None`)

</details>

## Expected repo-specific files

19 file(s).

## Parse errors

0 file(s). See [details/parse_errors.md](details/parse_errors.md).

<details>
<summary>Preview</summary>

_None._

</details>

## Signature changes

4 symbol(s). See [details/signature_changes.md](details/signature_changes.md).
