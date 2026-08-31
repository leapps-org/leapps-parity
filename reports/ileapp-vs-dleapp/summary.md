# LEAPP Parity Report

![Parity summary](parity.1788200407.svg)

## Scan metadata

- **Generated**: 2026-08-31T18:20:07.530292+00:00
- **Baseline**: `ileapp`
- **Comparison**: `dleapp`

- **ileapp**: `899709e09960` on `main` ([https://github.com/abrignoni/iLEAPP.git](https://github.com/abrignoni/iLEAPP.git))
- **dleapp**: `5c99ed324e9b` on `main` ([https://github.com/abrignoni/DLEAPP.git](https://github.com/abrignoni/DLEAPP.git))

## Overall counts

| Metric | Count |
|---|---:|
| Files scanned (union) | 81 |
| Same | 22 |
| Changed (logic/file) | 11 |
| Missing from comparison | 1 |
| Extra in comparison | 14 |
| Expected repo-specific | 33 |
| Parse errors | 0 |
| Import dependency gaps | 11 |

## File-level summary

| Status | Count |
|---|---:|
| same | 22 |
| logic_changed | 11 |
| file_missing_from_comparison | 1 |
| file_extra_in_comparison | 14 |
| expected_repo_specific | 33 |

## Symbol-level summary

| Status | Count |
|---|---:|
| symbol_missing_from_comparison | 28 |
| symbol_extra_in_comparison | 12 |
| signature_changed | 1 |
| logic_changed | 34 |

## All compared files

81 file(s). See [details/file_list.md](details/file_list.md).

## Import dependency gaps

Baseline files that import modules missing from the comparison repo (for example `ilapfuncs.py` → `context.py`).

11 gap(s). See [details/import_dependency_gaps.md](details/import_dependency_gaps.md).

| Baseline file | Import | Missing in comparison |
|---|---|---|
| `main_entry.py` | `scripts.ios_keychain:report_supplied_keychain` | `scripts/ios_keychain.py` |
| `main_gui.py` | `scripts.tz_offset:tzvalues` | `scripts/tz_offset.py` |
| `scripts/blackboxprotobuf/__init__.py` | `scripts.blackboxprotobuf.lib.interface:*` | `scripts/blackboxprotobuf/lib/interface.py` |
| `scripts/blackboxprotobuf/lib/interface.py` | `scripts.blackboxprotobuf.lib.types.length_delim` | `scripts/blackboxprotobuf/lib/types/length_delim.py` |
| `scripts/blackboxprotobuf/lib/interface.py` | `scripts.blackboxprotobuf.lib.types.type_maps` | `scripts/blackboxprotobuf/lib/types/type_maps.py` |
| `scripts/blackboxprotobuf/lib/types/length_delim.py` | `scripts.blackboxprotobuf.lib.types` | `scripts/blackboxprotobuf/lib/types/__init__.py` |
| `scripts/blackboxprotobuf/lib/types/length_delim.py` | `scripts.blackboxprotobuf.lib.types:varint` | `scripts/blackboxprotobuf/lib/types/__init__.py` |
| `scripts/blackboxprotobuf/lib/types/type_maps.py` | `scripts.blackboxprotobuf.lib.types:fixed` | `scripts/blackboxprotobuf/lib/types/__init__.py` |
| `scripts/blackboxprotobuf/lib/types/type_maps.py` | `scripts.blackboxprotobuf.lib.types:length_delim` | `scripts/blackboxprotobuf/lib/types/__init__.py` |
| `scripts/blackboxprotobuf/lib/types/type_maps.py` | `scripts.blackboxprotobuf.lib.types:varint` | `scripts/blackboxprotobuf/lib/types/__init__.py` |
| `scripts/ccl_leveldb.py` | `scripts.ccl_simplesnappy` | `scripts/ccl_simplesnappy.py` |

## Top mismatches

| Logical path | Status | Baseline file | Comparison file |
|---|---|---|---|
| `main_entry.py` | logic_changed | `ileapp.py` | `dleapp.py` | (4 symbol diffs)
| `main_gui.py` | logic_changed | `ileappGUI.py` | `dleappGUI.py` | (7 symbol diffs)
| `scripts/artifact_report.py` | logic_changed | `scripts/artifact_report.py` | `scripts/artifact_report.py` | (1 symbol diffs)
| `scripts/context.py` | logic_changed | `scripts/context.py` | `scripts/context.py` | (9 symbol diffs)
| `scripts/html_parts.py` | logic_changed | `scripts/html_parts.py` | `scripts/html_parts.py` |
| `scripts/ilapfuncs.py` | logic_changed | `scripts/ilapfuncs.py` | `scripts/ilapfuncs.py` | (25 symbol diffs)
| `scripts/lavafuncs.py` | logic_changed | `scripts/lavafuncs.py` | `scripts/lavafuncs.py` | (15 symbol diffs)
| `scripts/modules_to_exclude.py` | logic_changed | `scripts/modules_to_exclude.py` | `scripts/modules_to_exclude.py` |
| `scripts/report.py` | logic_changed | `scripts/report.py` | `scripts/report.py` | (3 symbol diffs)
| `scripts/search_files.py` | logic_changed | `scripts/search_files.py` | `scripts/search_files.py` | (10 symbol diffs)
| `scripts/version_info.py` | logic_changed | `scripts/version_info.py` | `scripts/version_info.py` | (1 symbol diffs)
| `scripts/mmkv_parser.py` | file_missing_from_comparison | `scripts/mmkv_parser.py` | `—` |
| `scripts/ccl/__init__.py` | file_extra_in_comparison | `—` | `scripts/ccl/__init__.py` |
| `scripts/ccl/ccl_blink_value_deserializer.py` | file_extra_in_comparison | `—` | `scripts/ccl/ccl_blink_value_deserializer.py` |
| `scripts/ccl/ccl_chromium_indexeddb.py` | file_extra_in_comparison | `—` | `scripts/ccl/ccl_chromium_indexeddb.py` |
| `scripts/ccl/ccl_leveldb.py` | file_extra_in_comparison | `—` | `scripts/ccl/ccl_leveldb.py` |
| `scripts/ccl/ccl_simplesnappy.py` | file_extra_in_comparison | `—` | `scripts/ccl/ccl_simplesnappy.py` |
| `scripts/ccl/ccl_v8_value_deserializer.py` | file_extra_in_comparison | `—` | `scripts/ccl/ccl_v8_value_deserializer.py` |
| `scripts/ccl/indexeddb_to_json.py` | file_extra_in_comparison | `—` | `scripts/ccl/indexeddb_to_json.py` |
| `scripts/ccl/wire_assets.py` | file_extra_in_comparison | `—` | `scripts/ccl/wire_assets.py` |

## Changed logic files

11 file(s). See [details/changed_logic.md](details/changed_logic.md).

<details>
<summary>Preview</summary>

### `main_entry.py`
- module-level logic changed
- logic changed: `main`
- only in dleapp: `resolve_supplied_secret` — `def resolve_supplied_secret(value, label)`
- logic changed: `validate_args`
### `main_gui.py`
- module-level logic changed
- logic changed: `ValidateInput`
- only in dleapp: `_update_signal_key_status` — `def _update_signal_key_status(*_args)`
- only in ileapp: `clear_keychain` — `def clear_keychain()`
- only in dleapp: `open_signal_key_dialog` — `def open_signal_key_dialog()`
- logic changed: `pickModules`
- logic changed: `process`
- only in ileapp: `select_keychain` — `def select_keychain()`
### `scripts/artifact_report.py`
- module-level logic changed
- logic changed: `ArtifactHtmlReport.start_artifact_report`
### `scripts/context.py`
- module-level logic changed
- only in dleapp: `Context.get_app_secret` — `@@def get_app_secret(name)`
- only in ileapp: `Context.get_apple_os_version` — `@@def get_apple_os_version(build, device_family=...)`
- only in ileapp: `Context.get_installed_os_version` — `@@def get_installed_os_version()`
- only in ileapp: `Context.get_keychain_path` — `@@def get_keychain_path()`
- only in ileapp: `Context.get_metadata` — `@@def get_metadata(collection)`
- only in ileapp: `Context.lookup_metadata` — `@@def lookup_metadata(collection, key, group=...)`
- only in dleapp: `Context.set_app_secret` — `@@def set_app_secret(name, value)`
- only in ileapp: `Context.set_installed_os_version` — `@@def set_installed_os_version(os_version)`
- only in ileapp: `Context.set_keychain_path` — `@@def set_keychain_path(keychain_path)`
### `scripts/html_parts.py`
- module-level logic changed
### `scripts/ilapfuncs.py`
- module-level logic changed
- logic changed: `OutputParameters.__init__`
- only in ileapp: `_batched` — `def _batched(iterable, size)`
- only in dleapp: `_count_generator` — `def _count_generator(reader)`
- only in ileapp: `_deserialize_nska` — `def _deserialize_nska(data)`
- only in dleapp: `_get_line_count` — `def _get_line_count(file)`
- only in ileapp: `_read_binary_plist_tolerantly` — `def _read_binary_plist_tolerantly(file_path)`
- logic changed: `artifact_processor`
- only in ileapp: `artifact_processor_streaming` — `def artifact_processor_streaming(func)`

</details>

## Missing files

1 file(s). See [details/missing_files.md](details/missing_files.md).

<details>
<summary>Preview</summary>

- `scripts/mmkv_parser.py` (baseline: `scripts/mmkv_parser.py`)

</details>

## Extra files

14 file(s). See [details/extra_files.md](details/extra_files.md).

<details>
<summary>Preview</summary>

- `leapp_functions/parsers/apple_atx.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/alternate_artifacts/appInventory.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/blackboxprotobuf/__init__.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/blackboxprotobuf/lib/__init__.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/blackboxprotobuf/lib/interface.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/blackboxprotobuf/lib/types/__init__.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/blackboxprotobuf/lib/types/fixed.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/blackboxprotobuf/lib/types/length_delim.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/blackboxprotobuf/lib/types/type_maps.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/blackboxprotobuf/lib/types/varint.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl/__init__.py` (comparison: `scripts/ccl/__init__.py`)
- `scripts/ccl/ccl_blink_value_deserializer.py` (comparison: `scripts/ccl/ccl_blink_value_deserializer.py`)
- `scripts/ccl/ccl_bplist.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl/ccl_chromium_indexeddb.py` (comparison: `scripts/ccl/ccl_chromium_indexeddb.py`)
- `scripts/ccl/ccl_leveldb.py` (comparison: `scripts/ccl/ccl_leveldb.py`)
- `scripts/ccl/ccl_segb1.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl/ccl_segb2.py` _(expected repo-specific)_ (comparison: `None`)
- `scripts/ccl/ccl_simplesnappy.py` (comparison: `scripts/ccl/ccl_simplesnappy.py`)
- `scripts/ccl/ccl_v8_value_deserializer.py` (comparison: `scripts/ccl/ccl_v8_value_deserializer.py`)
- `scripts/ccl/indexeddb_to_json.py` (comparison: `scripts/ccl/indexeddb_to_json.py`)

</details>

## Expected repo-specific files

33 file(s).

## Parse errors

0 file(s). See [details/parse_errors.md](details/parse_errors.md).

<details>
<summary>Preview</summary>

_None._

</details>

## Signature changes

1 symbol(s). See [details/signature_changes.md](details/signature_changes.md).
