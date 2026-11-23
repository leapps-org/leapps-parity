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
- logic changed: `validate_args`
- only in ileapp: `version_readers_first` — `def version_readers_first(plugins)`

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
- only in vleapp: `OnFocusIn` — `def OnFocusIn(event)`
- only in vleapp: `ValidateInput` — `def ValidateInput()`
- only in vleapp: `allow_output_folder_name_chars` — `def allow_output_folder_name_chars(proposed)`
- only in vleapp: `case_data` — `def case_data()`
- only in vleapp: `center_main_window_macos` — `def center_main_window_macos(window, width, height)`
- only in vleapp: `close_main_window` — `def close_main_window()`
- only in ileapp: `crunch` — `def crunch(request)`
- only in vleapp: `deselect_all` — `def deselect_all()`
- only in vleapp: `explore_lava` — `def explore_lava()`
- only in vleapp: `filter_modules` — `def filter_modules(*args)`
- only in vleapp: `finish_crunch` — `def finish_crunch(crunch_successful, out_params)`
- only in vleapp: `geometry_offset` — `def geometry_offset(value)`
- only in vleapp: `get_selected_modules` — `def get_selected_modules()`
- only in vleapp: `input_paths` — `def input_paths()`
- only in vleapp: `load_profile` — `def load_profile()`
- only in vleapp: `module_matches_filter` — `def module_matches_filter(module_infos, filter_term=...)`
- only in vleapp: `open_folder` — `def open_folder(output_path)`
- only in vleapp: `open_lava` — `def open_lava(project_path, launcher)`
- only in vleapp: `open_report` — `def open_report(report_path)`
- only in vleapp: `open_settings_window` — `def open_settings_window()`
- only in vleapp: `open_website` — `def open_website(url)`
- only in vleapp: `pickModules` — `def pickModules()`
- only in vleapp: `poll_crunch` — `def poll_crunch(message_queue, out_params)`
- only in vleapp: `process` — `def process(casedata)`
- only in vleapp: `resource_path` — `def resource_path(filename)`
- only in vleapp: `run_crunch` — `def run_crunch(message_queue, selected_modules, extracttype, input_path, out_params, wrap_text, case_info, image_password=..., found_members=..., hash_files=...)`
- only in vleapp: `save_profile` — `def save_profile()`
- only in vleapp: `scroll` — `def scroll(event)`
- only in vleapp: `select_all` — `def select_all()`
- only in vleapp: `select_input` — `def select_input(button_type)`
- only in vleapp: `select_output` — `def select_output()`
- only in ileapp: `selfcheck` — `def selfcheck()`
- only in vleapp: `set_input_selection` — `def set_input_selection(paths)`
- only in vleapp: `show_history_menu` — `def show_history_menu(button, path_type)`

### `packaging/build.py`

- module-level logic changed
- only in ileapp: `_unifiedlog_binary` — `def _unifiedlog_binary() -> ...`
- logic changed: `appimage_desktop_entry`
- logic changed: `build_exe`
- only in ileapp: `bundle_binaries` — `def bundle_binaries() -> ...`
- logic changed: `bundle_datas`
- only in ileapp: `bundled_bin_dir` — `def bundled_bin_dir() -> ...`
- logic changed: `hidden_imports`
- only in ileapp: `read_config` — `def read_config(field) -> ...`
- logic changed: `read_version`
- logic changed: `smoke`

### `packaging/entrypoint.py`

- module-level logic changed
- logic changed: `main`

### `scripts/artifact_report.py`

- module-level logic changed
- logic changed: `ArtifactHtmlReport.start_artifact_report`
- only in ileapp: `cell_html` — `def cell_html(value, header, html_no_escape, html_multiline)`

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
- logic changed: `GuiWindow.end_worker_run`
- only in vleapp: `_count_generator` — `def _count_generator(reader)`
- only in ileapp: `_deserialize_nska` — `def _deserialize_nska(data)`
- only in vleapp: `_get_line_count` — `def _get_line_count(file)`
- only in ileapp: `_is_appledouble` — `def _is_appledouble(path)`
- only in ileapp: `_is_unrepresentable_cocoa_year_one` — `def _is_unrepresentable_cocoa_year_one(seconds, helper)`
- only in ileapp: `_read_binary_plist_tolerantly` — `def _read_binary_plist_tolerantly(file_path)`
- logic changed: `artifact_processor`
- logic changed: `device_info`
- only in vleapp: `gather_hashes_in_file` — `def gather_hashes_in_file(file_found, regex)`
- logic changed: `generate_hexdump`
- logic changed: `generate_thumbnail`
- logic changed: `get_birthdate`
- logic changed: `get_plist_content`
- logic changed: `get_plist_file_content`
- logic changed: `get_resolution_for_model_id`
- only in ileapp: `get_sysdiagnose_files` — `def get_sysdiagnose_files(files_found, target, text_mode=..., encoding=...)`
- only in vleapp: `html2csv` — `def html2csv(reportfolderbase)`
- only in ileapp: `iOS` — `class iOS`
- only in ileapp: `iOS.get_version` — `@@def get_version()`
- only in ileapp: `iOS.set_version` — `@@def set_version(os_version)`
- only in vleapp: `ipgen` — `def ipgen(report_folder, data_list_ipaddress)`
- only in ileapp: `is_sysdiagnose_archive` — `def is_sysdiagnose_archive(path)`
- only in vleapp: `logdevinfo` — `def logdevinfo(message=...)`
- logic changed: `tsv`
- only in vleapp: `usergen` — `def usergen(report_folder, data_list_usernames)`
- logic changed: `webkit_timestampsconv`

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
- only in vleapp: `_gui_image_key` — `def _gui_image_key(parent, path)`
- only in vleapp: `_gui_volume_keys` — `def _gui_volume_keys(parent, name, image, keys)`
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
- only in vleapp: `FileSeekerIva` — `class FileSeekerIva`
- only in vleapp: `FileSeekerIva.__init__` — `def __init__(self, iva_path, data_folder)`
- only in vleapp: `FileSeekerIva.cleanup` — `def cleanup(self)`
- only in vleapp: `FileSeekerIva.search` — `def search(self, filepattern, return_on_first_hit=..., force=...)`
- only in ileapp: `_backup_file_plaintext` — `def _backup_file_plaintext(decrypted_contents, manifest_size, relative_path)`
- only in ileapp: `_manifest_times` — `def _manifest_times(metadata)`
- only in ileapp: `_without_cbc_padding` — `def _without_cbc_padding(decrypted_contents)`
- only in ileapp: `check_itunes_backup_status` — `def check_itunes_backup_status(directory, backup_type)`
- only in ileapp: `decrypt_itunes_backup` — `def decrypt_itunes_backup(directory, passcode)`
- only in ileapp: `get_itunes_backup_encryption` — `def get_itunes_backup_encryption(directory)`
- only in ileapp: `get_itunes_backup_type` — `def get_itunes_backup_type(directory)`

### `scripts/version_info.py`

- module-level logic changed
- only in ileapp: `check_runtime_dependencies` — `def check_runtime_dependencies()`
