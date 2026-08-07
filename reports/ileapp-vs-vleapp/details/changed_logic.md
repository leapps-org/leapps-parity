# Changed logic files

### `main_entry.py`

- module-level logic changed
- logic changed: `main`
- logic changed: `validate_args`

### `main_gui.py`

- module-level logic changed
- logic changed: `ValidateInput`
- only in ileapp: `clear_keychain` — `def clear_keychain()`
- logic changed: `pickModules`
- logic changed: `process`
- only in ileapp: `select_keychain` — `def select_keychain()`

### `scripts/artifact_report.py`

- module-level logic changed
- logic changed: `ArtifactHtmlReport.start_artifact_report`

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
- only in ileapp: `_batched` — `def _batched(iterable, size)`
- only in vleapp: `_count_generator` — `def _count_generator(reader)`
- only in ileapp: `_deserialize_nska` — `def _deserialize_nska(data)`
- only in vleapp: `_get_line_count` — `def _get_line_count(file)`
- logic changed: `artifact_processor`
- only in ileapp: `artifact_processor_streaming` — `def artifact_processor_streaming(func)`
- logic changed: `device_info`
- only in vleapp: `gather_hashes_in_file` — `def gather_hashes_in_file(file_found, regex)`
- logic changed: `generate_hexdump`
- logic changed: `generate_thumbnail`
- logic changed: `get_plist_content`
- logic changed: `get_plist_file_content`
- logic changed: `get_resolution_for_model_id`
- only in vleapp: `html2csv` — `def html2csv(reportfolderbase)`
- only in ileapp: `iOS` — `class iOS`
- only in ileapp: `iOS.get_version` — `@@def get_version()`
- only in ileapp: `iOS.set_version` — `@@def set_version(os_version)`
- only in vleapp: `ipgen` — `def ipgen(report_folder, data_list_ipaddress)`
- logic changed: `tsv`
- only in vleapp: `usergen` — `def usergen(report_folder, data_list_usernames)`

### `scripts/lavafuncs.py`

- module-level logic changed
- logic changed: `initialize_lava`
- logic changed: `lava_add_module`
- logic changed: `lava_create_sqlite_table`
- logic changed: `lava_finalize_output`
- logic changed: `lava_get_full_media_info`
- logic changed: `lava_get_media_item`
- logic changed: `lava_get_media_references`
- logic changed: `lava_insert_sqlite_artifact_link_pattern_to_file`
- logic changed: `lava_insert_sqlite_artifact_search_pattern`
- logic changed: `lava_insert_sqlite_data`
- logic changed: `lava_insert_sqlite_file_path`
- logic changed: `lava_insert_sqlite_media_item`
- logic changed: `lava_insert_sqlite_media_references`
- logic changed: `lava_process_artifact`
- only in ileapp: `lava_update_record_count` — `def lava_update_record_count(category, tablename, record_count)`

### `scripts/modules_to_exclude.py`

- module-level logic changed

### `scripts/report.py`

- module-level logic changed
- logic changed: `create_index_html`

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
- only in ileapp: `check_runtime_dependencies` — `def check_runtime_dependencies()`
