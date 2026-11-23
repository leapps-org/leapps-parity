# Changed logic files

### `leapp_functions/__init__.py`

- module-level logic changed
- only in ileapp: `load_config` — `def load_config()`

### `leapp_functions/app/history.py`

- module-level logic changed
- only in ileapp: `get_appearance` — `def get_appearance(leapp_id)`
- only in ileapp: `set_appearance` — `def set_appearance(leapp_id, appearance)`

### `leapp_functions/app/output.py`

- module-level logic changed
- logic changed: `default_output_folder_name`

### `leapp_functions/data_sources/json_files.py`

- module-level logic changed
- only in ileapp: `convert_json_file_to_namedtuple` — `def convert_json_file_to_namedtuple(json_file_path)`
- only in ileapp: `save_content_to_json_file` — `def save_content_to_json_file(file_path, data)`

### `main_entry.py`

- module-level logic changed
- logic changed: `create_casedata`
- logic changed: `create_profile`
- logic changed: `main`
- only in dleapp: `profile_file_name` — `def profile_file_name(name)`
- only in dleapp: `read_profile` — `def read_profile(filename)`
- only in dleapp: `resolve_supplied_secret` — `def resolve_supplied_secret(value, label)`
- logic changed: `validate_args`
- only in ileapp: `version_readers_first` — `def version_readers_first(plugins)`
- only in dleapp: `write_profile` — `def write_profile(filename, plugins)`

### `main_gui.py`

- module-level logic changed
- only in ileapp: `MainWindow` — `class MainWindow`
- only in ileapp: `MainWindow.__init__` — `def __init__(self, show=...)`
- only in ileapp: `MainWindow.activate_application` — `def activate_application(self)`
- only in ileapp: `MainWindow.build` — `def build(self)`
- only in ileapp: `MainWindow.close` — `def close(self)`
- only in ileapp: `MainWindow.colors` — `@@def colors(self)`
- only in ileapp: `MainWindow.destroy` — `def destroy(self)`
- only in ileapp: `MainWindow.fix_size` — `def fix_size(self)`
- only in ileapp: `MainWindow.focus_field` — `def focus_field(self, method)`
- only in ileapp: `MainWindow.go` — `def go(self, step)`
- only in ileapp: `MainWindow.go_back` — `def go_back(self)`
- only in ileapp: `MainWindow.go_next` — `def go_next(self)`
- only in ileapp: `MainWindow.on_focus` — `def on_focus(self, event)`
- only in ileapp: `MainWindow.on_touchpad` — `def on_touchpad(self, event)`
- only in ileapp: `MainWindow.on_wheel` — `def on_wheel(self, event)`
- only in ileapp: `MainWindow.redraw` — `def redraw(self)`
- only in ileapp: `MainWindow.refresh_steps` — `def refresh_steps(self)`
- only in ileapp: `MainWindow.show_screen` — `def show_screen(self)`
- only in ileapp: `MainWindow.watch_unlock` — `def watch_unlock(self)`
- only in dleapp: `OnFocusIn` — `def OnFocusIn(event)`
- only in dleapp: `ValidateInput` — `def ValidateInput()`
- only in dleapp: `_update_exodus_password_status` — `def _update_exodus_password_status(*_args)`
- only in dleapp: `_update_signal_key_status` — `def _update_signal_key_status(*_args)`
- only in dleapp: `_update_threema_password_status` — `def _update_threema_password_status(*_args)`
- only in dleapp: `_update_windows_user_password_status` — `def _update_windows_user_password_status(*_args)`
- only in dleapp: `allow_output_folder_name_chars` — `def allow_output_folder_name_chars(proposed)`
- only in dleapp: `case_data` — `def case_data()`
- only in dleapp: `center_main_window_macos` — `def center_main_window_macos(window, width, height)`
- only in dleapp: `close_main_window` — `def close_main_window()`
- only in ileapp: `crunch` — `def crunch(request)`
- only in dleapp: `deselect_all` — `def deselect_all()`
- only in dleapp: `explore_lava` — `def explore_lava()`
- only in dleapp: `filter_modules` — `def filter_modules(*args)`
- only in dleapp: `finish_crunch` — `def finish_crunch(crunch_successful, out_params)`
- only in dleapp: `geometry_offset` — `def geometry_offset(value)`
- only in dleapp: `get_selected_modules` — `def get_selected_modules()`
- only in dleapp: `input_paths` — `def input_paths()`
- only in dleapp: `load_profile` — `def load_profile()`
- only in dleapp: `module_matches_filter` — `def module_matches_filter(module_infos, filter_term=...)`
- only in dleapp: `open_exodus_password_dialog` — `def open_exodus_password_dialog()`
- only in dleapp: `open_folder` — `def open_folder(output_path)`
- only in dleapp: `open_lava` — `def open_lava(project_path, launcher)`
- only in dleapp: `open_report` — `def open_report(report_path)`
- only in dleapp: `open_settings_window` — `def open_settings_window()`
- only in dleapp: `open_signal_key_dialog` — `def open_signal_key_dialog()`
- only in dleapp: `open_threema_password_dialog` — `def open_threema_password_dialog()`
- only in dleapp: `open_website` — `def open_website(url)`
- only in dleapp: `open_windows_user_password_dialog` — `def open_windows_user_password_dialog()`
- only in dleapp: `pickModules` — `def pickModules()`
- only in dleapp: `poll_crunch` — `def poll_crunch(message_queue, out_params)`
- only in dleapp: `process` — `def process(casedata)`
- only in dleapp: `resource_path` — `def resource_path(filename)`
- only in dleapp: `run_crunch` — `def run_crunch(message_queue, selected_modules, extracttype, input_path, out_params, wrap_text, case_info, image_password=..., found_members=..., hash_files=...)`
- only in dleapp: `save_profile` — `def save_profile()`
- only in dleapp: `scroll` — `def scroll(event)`
- only in dleapp: `select_all` — `def select_all()`
- only in dleapp: `select_input` — `def select_input(button_type)`
- only in dleapp: `select_output` — `def select_output()`
- only in ileapp: `selfcheck` — `def selfcheck()`
- only in dleapp: `set_input_selection` — `def set_input_selection(paths)`
- only in dleapp: `show_history_menu` — `def show_history_menu(button, path_type)`

### `packaging/build.py`

- module-level logic changed
- logic changed: `appimage_desktop_entry`
- logic changed: `build_exe`
- logic changed: `hidden_imports`
- only in ileapp: `read_config` — `def read_config(field) -> ...`
- logic changed: `read_version`

### `packaging/entrypoint.py`

- module-level logic changed
- logic changed: `main`

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
- logic changed: `GuiWindow.end_worker_run`
- logic changed: `OutputParameters.__init__`
- only in ileapp: `SqliteRecords` — `class SqliteRecords`
- only in ileapp: `SqliteRecords.__del__` — `def __del__(self)`
- only in ileapp: `SqliteRecords.__init__` — `def __init__(self, db, cursor)`
- only in ileapp: `SqliteRecords.__iter__` — `def __iter__(self)`
- only in ileapp: `SqliteRecords.__next__` — `def __next__(self)`
- only in ileapp: `SqliteRecords.close` — `def close(self)`
- only in dleapp: `_count_generator` — `def _count_generator(reader)`
- only in ileapp: `_deserialize_nska` — `def _deserialize_nska(data)`
- only in dleapp: `_get_line_count` — `def _get_line_count(file)`
- only in ileapp: `_is_appledouble` — `def _is_appledouble(path)`
- only in ileapp: `_is_unrepresentable_cocoa_year_one` — `def _is_unrepresentable_cocoa_year_one(seconds, helper)`
- only in ileapp: `_read_binary_plist_tolerantly` — `def _read_binary_plist_tolerantly(file_path)`
- logic changed: `artifact_processor`
- logic changed: `device_info`
- only in dleapp: `gather_hashes_in_file` — `def gather_hashes_in_file(file_found, regex)`
- logic changed: `generate_hexdump`
- logic changed: `generate_thumbnail`
- logic changed: `get_birthdate`
- logic changed: `get_plist_content`
- logic changed: `get_plist_file_content`
- logic changed: `get_resolution_for_model_id`
- logic changed: `get_sqlite_db_records`
- only in ileapp: `get_sysdiagnose_files` — `def get_sysdiagnose_files(files_found, target, text_mode=..., encoding=...)`
- only in dleapp: `html2csv` — `def html2csv(reportfolderbase)`
- only in ileapp: `iOS` — `class iOS`
- only in ileapp: `iOS.get_version` — `@@def get_version()`
- only in ileapp: `iOS.set_version` — `@@def set_version(os_version)`
- only in dleapp: `ipgen` — `def ipgen(report_folder, data_list_ipaddress)`
- only in ileapp: `is_sysdiagnose_archive` — `def is_sysdiagnose_archive(path)`
- only in dleapp: `logdevinfo` — `def logdevinfo(message=...)`
- logic changed: `tsv`
- only in dleapp: `usergen` — `def usergen(report_folder, data_list_usernames)`
- logic changed: `webkit_timestampsconv`
- logic changed: `write_device_info`

### `scripts/lavafuncs.py`

- module-level logic changed
- logic changed: `_prepare_datetime_value`
- logic changed: `initialize_lava`
- logic changed: `lava_add_module`
- logic changed: `lava_create_sqlite_table`
- logic changed: `lava_get_full_media_info`
- logic changed: `lava_get_media_item`
- logic changed: `lava_get_media_references`
- logic changed: `lava_insert_sqlite_artifact_link_pattern_to_file`
- logic changed: `lava_insert_sqlite_artifact_search_pattern`
- logic changed: `lava_insert_sqlite_file_path`
- logic changed: `lava_insert_sqlite_media_item`
- logic changed: `lava_insert_sqlite_media_references`
- logic changed: `lava_process_artifact`

### `scripts/modules_to_exclude.py`

- module-level logic changed

### `scripts/raw_image.py`

- module-level logic changed
- only in ileapp: `DialogAsker` — `class DialogAsker`
- only in ileapp: `DialogAsker.__init__` — `def __init__(self, parent, confirm=...)`
- only in ileapp: `DialogAsker.ask_file` — `def ask_file(self, title, filetypes)`
- only in ileapp: `DialogAsker.ask_secret` — `def ask_secret(self, title, prompt)`
- only in ileapp: `DialogAsker.confirm_members` — `def confirm_members(self, search)`
- only in ileapp: `DialogAsker.show_error` — `def show_error(self, title, message)`
- only in ileapp: `DialogAsker.show_info` — `def show_info(self, title, message)`
- only in dleapp: `_gui_image_key` — `def _gui_image_key(parent, path)`
- only in dleapp: `_gui_volume_keys` — `def _gui_volume_keys(parent, name, image, keys)`
- only in ileapp: `_image_key` — `def _image_key(asker, path)`
- only in ileapp: `_volume_keys` — `def _volume_keys(asker, name, image, keys)`
- logic changed: `ask_raw_input`
- only in ileapp: `unlock_raw_input` — `def unlock_raw_input(input_path, asker, look_beside=...)`

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
- only in ileapp: `_backup_file_plaintext` — `def _backup_file_plaintext(decrypted_contents, manifest_size, relative_path)`
- only in ileapp: `_manifest_times` — `def _manifest_times(metadata)`
- only in ileapp: `_without_cbc_padding` — `def _without_cbc_padding(decrypted_contents)`
- only in ileapp: `check_itunes_backup_status` — `def check_itunes_backup_status(directory, backup_type)`
- only in ileapp: `decrypt_itunes_backup` — `def decrypt_itunes_backup(directory, passcode)`
- only in ileapp: `get_itunes_backup_encryption` — `def get_itunes_backup_encryption(directory)`
- only in ileapp: `get_itunes_backup_type` — `def get_itunes_backup_type(directory)`

### `scripts/unifiedlogs.py`

- module-level logic changed
- only in dleapp: `_extends` — `def _extends(shorter, longer, chunk_size=...)`
- only in dleapp: `_pick_copy` — `def _pick_copy(paths, summary)`
- only in dleapp: `_without_data_volume` — `def _without_data_volume(components)`
- only in dleapp: `assemble_merged_archive` — `def assemble_merged_archive(diagnostics_dirs, uuidtext_dirs, workdir)`
- only in ileapp: `filtered_records` — `def filtered_records(source_path, query, batch_size=..., interval=..., clock=..., log=...)`
- only in dleapp: `store_copies` — `def store_copies(files_found, root)`

### `scripts/version_info.py`

- module-level logic changed
- only in ileapp: `check_runtime_dependencies` — `def check_runtime_dependencies()`
