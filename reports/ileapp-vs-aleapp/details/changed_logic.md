# Changed logic files

### `main_entry.py`

- module-level logic changed
- logic changed: `main`
- logic changed: `validate_args`

### `main_gui.py`

- module-level logic changed
- logic changed: `ValidateInput`
- logic changed: `case_data`
- only in ileapp: `clear_keychain` — `def clear_keychain()`
- logic changed: `filter_modules`
- logic changed: `pickModules`
- logic changed: `process`
- only in ileapp: `select_keychain` — `def select_keychain()`

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
- only in ileapp: `Context.get_apple_os_version` — `@@def get_apple_os_version(build, device_family=...)`
- only in ileapp: `Context.get_installed_os_version` — `@@def get_installed_os_version()`
- only in ileapp: `Context.get_keychain_path` — `@@def get_keychain_path()`
- only in ileapp: `Context.get_metadata` — `@@def get_metadata(collection)`
- only in ileapp: `Context.lookup_metadata` — `@@def lookup_metadata(collection, key, group=...)`
- only in ileapp: `Context.set_installed_os_version` — `@@def set_installed_os_version(os_version)`
- only in ileapp: `Context.set_keychain_path` — `@@def set_keychain_path(keychain_path)`

### `scripts/html_parts.py`

- module-level logic changed

### `scripts/ilapfuncs.py`

- module-level logic changed
- logic changed: `OutputParameters.__init__`
- only in ileapp: `_batched` — `def _batched(iterable, size)`
- only in ileapp: `_deserialize_nska` — `def _deserialize_nska(data)`
- only in aleapp: `abxread` — `def abxread(in_path, multi_root)`
- logic changed: `artifact_processor`
- only in ileapp: `artifact_processor_streaming` — `def artifact_processor_streaming(func)`
- only in aleapp: `checkabx` — `def checkabx(in_path)`
- only in ileapp: `convert_bytes_to_unit` — `def convert_bytes_to_unit(size)`
- only in ileapp: `convert_cocoa_core_data_ts_to_utc` — `def convert_cocoa_core_data_ts_to_utc(cocoa_core_data_ts)`
- only in ileapp: `convert_log_ts_to_utc` — `def convert_log_ts_to_utc(str_dt)`
- only in ileapp: `convert_plist_date_to_timezone_offset` — `def convert_plist_date_to_timezone_offset(plist_date, timezone_offset)`
- only in ileapp: `convert_plist_date_to_utc` — `def convert_plist_date_to_utc(plist_date)`
- only in ileapp: `convert_ts_human_to_timezone_offset` — `def convert_ts_human_to_timezone_offset(ts, timezone_offset)`
- only in ileapp: `convert_ts_int_to_timezone` — `def convert_ts_int_to_timezone(time, time_offset)`
- logic changed: `convert_unix_ts_in_seconds`
- only in ileapp: `convert_unix_ts_to_str` — `def convert_unix_ts_to_str(ts)`
- only in ileapp: `convert_unix_ts_to_timezone` — `def convert_unix_ts_to_timezone(ts, timezone_offset)`
- logic changed: `convert_unix_ts_to_utc`
- only in aleapp: `decode_protobuf` — `def decode_protobuf(data, typedef=...)`
- only in ileapp: `generate_hexdump` — `def generate_hexdump(data, char_per_row=...)`
- only in ileapp: `generate_thumbnail` — `def generate_thumbnail(imDirectory, imFilename, seeker, report_folder)`
- only in aleapp: `get_binary_file_content` — `def get_binary_file_content(file_path)`
- only in ileapp: `get_birthdate` — `def get_birthdate(date)`
- only in ileapp: `get_birthdate_from_unix_ts` — `def get_birthdate_from_unix_ts(date)`
- only in aleapp: `get_file_path_list_checking_uid` — `def get_file_path_list_checking_uid(files_found, filename, position, skip=...)`
- only in ileapp: `get_plist_content` — `def get_plist_content(data)`
- only in ileapp: `get_plist_file_content` — `def get_plist_file_content(file_path)`
- only in ileapp: `get_resolution_for_model_id` — `def get_resolution_for_model_id(model_id)`
- only in aleapp: `get_results_with_extra_sourcepath_if_needed` — `def get_results_with_extra_sourcepath_if_needed(path_list, query, data_headers)`
- logic changed: `get_sqlite_db_records`
- only in ileapp: `get_sqlite_multiple_db_records` — `def get_sqlite_multiple_db_records(path_list, query, data_headers)`
- only in ileapp: `iOS` — `class iOS`
- only in ileapp: `iOS.get_version` — `@@def get_version()`
- only in ileapp: `iOS.set_version` — `@@def set_version(os_version)`
- only in ileapp: `lava_only_info` — `def lava_only_info(category, artifact_name, table_name, records)`
- only in ileapp: `strings` — `def strings(data)`
- only in ileapp: `strings_raw` — `def strings_raw(data)`
- only in aleapp: `timestampsconv` — `def timestampsconv(webkittime)`
- logic changed: `tsv`
- only in ileapp: `webkit_timestampsconv` — `def webkit_timestampsconv(webkittime)`
- only in ileapp: `write_lava_only_log` — `def write_lava_only_log()`

### `scripts/lavafuncs.py`

- module-level logic changed
- logic changed: `lava_insert_sqlite_data`
- only in ileapp: `lava_update_record_count` — `def lava_update_record_count(category, tablename, record_count)`

### `scripts/modules_to_exclude.py`

- module-level logic changed

### `scripts/report.py`

- module-level logic changed

### `scripts/search_files.py`

- module-level logic changed
- only in ileapp: `FileSeekerItunes` — `class FileSeekerItunes`
- only in ileapp: `FileSeekerItunes.__init__` — `def __init__(self, directory, data_folder, backup_type, decryption_keys)`
- only in ileapp: `FileSeekerItunes.build_files_list_from_manifest_db` — `def build_files_list_from_manifest_db(self, manifest_path)`
- only in ileapp: `FileSeekerItunes.build_files_list_from_manifest_mbdb` — `def build_files_list_from_manifest_mbdb(self, manifest_path)`
- only in ileapp: `FileSeekerItunes.get_root_path_from_domain` — `def get_root_path_from_domain(self, domain)`
- only in ileapp: `FileSeekerItunes.search` — `def search(self, filepattern, return_on_first_hit=..., force=...)`
- only in ileapp: `check_itunes_backup_status` — `def check_itunes_backup_status(directory, backup_type)`
- only in ileapp: `decrypt_itunes_backup` — `def decrypt_itunes_backup(directory, passcode)`
- only in ileapp: `get_itunes_backup_encryption` — `def get_itunes_backup_encryption(directory)`
- only in ileapp: `get_itunes_backup_type` — `def get_itunes_backup_type(directory)`

### `scripts/version_info.py`

- module-level logic changed
