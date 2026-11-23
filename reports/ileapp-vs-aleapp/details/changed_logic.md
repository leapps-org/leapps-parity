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
- only in aleapp: `OnFocusIn` — `def OnFocusIn(event)`
- only in aleapp: `ValidateInput` — `def ValidateInput()`
- only in aleapp: `allow_output_folder_name_chars` — `def allow_output_folder_name_chars(proposed)`
- only in aleapp: `ask_signal_recovery_key` — `def ask_signal_recovery_key(parent)`
- only in aleapp: `case_data` — `def case_data()`
- only in aleapp: `center_main_window_macos` — `def center_main_window_macos(window, width, height)`
- only in aleapp: `close_main_window` — `def close_main_window()`
- only in ileapp: `crunch` — `def crunch(request)`
- only in aleapp: `deselect_all` — `def deselect_all()`
- only in aleapp: `explore_lava` — `def explore_lava()`
- only in aleapp: `filter_modules` — `def filter_modules(*args)`
- only in aleapp: `finish_crunch` — `def finish_crunch(crunch_successful, out_params)`
- only in aleapp: `geometry_offset` — `def geometry_offset(value)`
- only in aleapp: `get_selected_modules` — `def get_selected_modules()`
- only in aleapp: `input_paths` — `def input_paths()`
- only in aleapp: `load_profile` — `def load_profile()`
- only in aleapp: `module_matches_filter` — `def module_matches_filter(module_infos, filter_term=...)`
- only in aleapp: `open_folder` — `def open_folder(output_path)`
- only in aleapp: `open_lava` — `def open_lava(project_path, launcher)`
- only in aleapp: `open_report` — `def open_report(report_path)`
- only in aleapp: `open_settings_window` — `def open_settings_window()`
- only in aleapp: `open_website` — `def open_website(url)`
- only in aleapp: `pickModules` — `def pickModules()`
- only in aleapp: `poll_crunch` — `def poll_crunch(message_queue, out_params)`
- only in aleapp: `process` — `def process(casedata)`
- only in aleapp: `resource_path` — `def resource_path(filename)`
- only in aleapp: `run_crunch` — `def run_crunch(message_queue, selected_modules, extracttype, input_path, out_params, wrap_text, case_info, image_password=..., found_members=..., hash_files=...)`
- only in aleapp: `save_profile` — `def save_profile()`
- only in aleapp: `scroll` — `def scroll(event)`
- only in aleapp: `select_all` — `def select_all()`
- only in aleapp: `select_input` — `def select_input(button_type)`
- only in aleapp: `select_output` — `def select_output()`
- only in ileapp: `selfcheck` — `def selfcheck()`
- only in aleapp: `set_input_selection` — `def set_input_selection(paths)`
- only in aleapp: `set_signal_key` — `def set_signal_key()`
- only in aleapp: `show_history_menu` — `def show_history_menu(button, path_type)`
- only in aleapp: `show_signal_key_state` — `def show_signal_key_state()`

### `packaging/build.py`

- module-level logic changed
- only in aleapp: `_installed_msl_plugins` — `def _installed_msl_plugins() -> ...`
- only in aleapp: `_require_folder_build` — `def _require_folder_build() -> ...`
- only in aleapp: `_require_tool` — `def _require_tool(name, hint) -> ...`
- only in aleapp: `_staged_files` — `def _staged_files(root) -> ...`
- only in ileapp: `_unifiedlog_binary` — `def _unifiedlog_binary() -> ...`
- logic changed: `appimage_desktop_entry`
- only in aleapp: `build_deb` — `def build_deb() -> ...`
- logic changed: `build_exe`
- only in aleapp: `build_linux_packages` — `def build_linux_packages() -> ...`
- only in aleapp: `build_rpm` — `def build_rpm() -> ...`
- only in ileapp: `bundle_binaries` — `def bundle_binaries() -> ...`
- logic changed: `bundle_datas`
- only in ileapp: `bundled_bin_dir` — `def bundled_bin_dir() -> ...`
- only in aleapp: `bundled_root` — `def bundled_root() -> ...`
- only in aleapp: `deb_arch` — `def deb_arch(machine=...) -> ...`
- only in aleapp: `debian_control` — `def debian_control(version, arch, installed_kib) -> ...`
- only in aleapp: `debian_md5sums` — `def debian_md5sums(root) -> ...`
- only in aleapp: `install_commands` — `def install_commands(python) -> ...`
- only in aleapp: `linux_staging` — `def linux_staging(folder, root) -> ...`
- logic changed: `main`
- only in aleapp: `package_version` — `def package_version(version) -> ...`
- only in ileapp: `read_config` — `def read_config(field) -> ...`
- logic changed: `read_version`
- only in aleapp: `rpm_spec` — `def rpm_spec(version, arch) -> ...`
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
- logic changed: `ArtifactHtmlReport.start_artifact_report`

### `scripts/chromium_sync_data.py`

- module-level logic changed

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
- logic changed: `OutputParameters.__init__`
- only in ileapp: `_deserialize_nska` — `def _deserialize_nska(data)`
- only in ileapp: `_is_appledouble` — `def _is_appledouble(path)`
- only in ileapp: `_is_unrepresentable_cocoa_year_one` — `def _is_unrepresentable_cocoa_year_one(seconds, helper)`
- only in ileapp: `_read_binary_plist_tolerantly` — `def _read_binary_plist_tolerantly(file_path)`
- only in aleapp: `abxread` — `def abxread(in_path, multi_root)`
- logic changed: `artifact_processor`
- only in aleapp: `checkabx` — `def checkabx(in_path)`
- only in ileapp: `convert_bytes_to_unit` — `def convert_bytes_to_unit(size)`
- only in ileapp: `convert_cocoa_core_data_ts_to_utc` — `def convert_cocoa_core_data_ts_to_utc(cocoa_core_data_ts)`
- only in ileapp: `convert_log_ts_to_utc` — `def convert_log_ts_to_utc(str_dt)`
- only in ileapp: `convert_plist_date_to_timezone_offset` — `def convert_plist_date_to_timezone_offset(plist_date, timezone_offset)`
- only in ileapp: `convert_plist_date_to_utc` — `def convert_plist_date_to_utc(plist_date)`
- only in ileapp: `convert_ts_human_to_timezone_offset` — `def convert_ts_human_to_timezone_offset(ts, timezone_offset)`
- only in ileapp: `convert_ts_int_to_timezone` — `def convert_ts_int_to_timezone(time, time_offset)`
- logic changed: `convert_ts_int_to_utc`
- only in ileapp: `convert_unix_ts_to_str` — `def convert_unix_ts_to_str(ts)`
- only in ileapp: `convert_unix_ts_to_timezone` — `def convert_unix_ts_to_timezone(ts, timezone_offset)`
- logic changed: `convert_unix_ts_to_utc`
- only in aleapp: `decode_protobuf` — `def decode_protobuf(data, typedef=...)`
- logic changed: `device_info`
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
- only in ileapp: `get_sysdiagnose_files` — `def get_sysdiagnose_files(files_found, target, text_mode=..., encoding=...)`
- only in ileapp: `iOS` — `class iOS`
- only in ileapp: `iOS.get_version` — `@@def get_version()`
- only in ileapp: `iOS.set_version` — `@@def set_version(os_version)`
- only in ileapp: `is_sysdiagnose_archive` — `def is_sysdiagnose_archive(path)`
- only in ileapp: `lava_only_info` — `def lava_only_info(category, artifact_name, table_name, records)`
- only in aleapp: `logdevinfo` — `def logdevinfo(message=...)`
- only in ileapp: `strings` — `def strings(data)`
- only in ileapp: `strings_raw` — `def strings_raw(data)`
- only in aleapp: `timestampsconv` — `def timestampsconv(webkittime)`
- logic changed: `tsv`
- only in ileapp: `webkit_timestampsconv` — `def webkit_timestampsconv(webkittime)`
- only in ileapp: `write_lava_only_log` — `def write_lava_only_log()`

### `scripts/lavafuncs.py`

- module-level logic changed
- logic changed: `_prepare_datetime_value`
- logic changed: `initialize_lava`

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
- only in aleapp: `_gui_image_key` — `def _gui_image_key(parent, path)`
- only in aleapp: `_gui_volume_keys` — `def _gui_volume_keys(parent, name, image, keys)`
- only in ileapp: `_image_key` — `def _image_key(asker, path)`
- only in ileapp: `_volume_keys` — `def _volume_keys(asker, name, image, keys)`
- logic changed: `ask_raw_input`
- only in ileapp: `unlock_raw_input` — `def unlock_raw_input(input_path, asker, look_beside=...)`

### `scripts/report.py`

- module-level logic changed
- logic changed: `processed_files_tab_content`

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

### `scripts/version_info.py`

- module-level logic changed
