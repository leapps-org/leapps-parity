# Signature changes

### `main_entry.py` — `crunch_artifacts`

| | Signature |
|:---|:---|
| Baseline | `def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, time_offset, profile_filename, itunes_backup_password=..., decryption_keys=...)` |
| Comparison | `def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, profile_filename)` |

### `scripts/ilapfuncs.py` — `check_in_embedded_media`

| | Signature |
|:---|:---|
| Baseline | `def check_in_embedded_media(source_file, data, name=..., force_type=..., force_extension=..., force_creation_date=..., force_modification_date=...)` |
| Comparison | `def check_in_embedded_media(artifact_info, report_folder, seeker, source_file, data, name=..., updated_at=...)` |

### `scripts/ilapfuncs.py` — `check_in_media`

| | Signature |
|:---|:---|
| Baseline | `def check_in_media(file_path, name=..., converted_file_path=..., force_type=..., force_extension=..., force_creation_date=..., force_modification_date=...)` |
| Comparison | `def check_in_media(artifact_info, report_folder, seeker, files_found, file_path, name=..., converted_file_path=...)` |

### `scripts/ilapfuncs.py` — `get_media_references_id`

| | Signature |
|:---|:---|
| Baseline | `def get_media_references_id(media_id, artifact_name, name)` |
| Comparison | `def get_media_references_id(media_id, artifact_info, name)` |

### `scripts/ilapfuncs.py` — `set_media_references`

| | Signature |
|:---|:---|
| Baseline | `def set_media_references(media_ref_id, media_id, module_name, artifact_name, name)` |
| Comparison | `def set_media_references(media_ref_id, media_id, artifact_info, name, media_path)` |

### `scripts/lavafuncs.py` — `lava_create_sqlite_table`

| | Signature |
|:---|:---|
| Baseline | `def lava_create_sqlite_table(table_name, data)` |
| Comparison | `def lava_create_sqlite_table(table_name, data, create_table=...)` |

### `scripts/lavafuncs.py` — `lava_process_artifact`

| | Signature |
|:---|:---|
| Baseline | `def lava_process_artifact(category, module_name, artifact_name, data, record_count=..., func_name=..., data_views=..., artifact_icon=..., source_path=...)` |
| Comparison | `def lava_process_artifact(category, module_name, artifact_name, data, record_count=..., data_views=..., create_table=...)` |

### `scripts/report.py` — `create_index_html`

| | Signature |
|:---|:---|
| Baseline | `def create_index_html(reportfolderbase, time_in_secs, time_HMS, extraction_type, image_input_path, nav_list_data, casedata, profile_filename, lava_only)` |
| Comparison | `def create_index_html(reportfolderbase, time_in_secs, time_HMS, extraction_type, image_input_path, nav_list_data, casedata, profile_filename)` |

### `scripts/report.py` — `generate_report`

| | Signature |
|:---|:---|
| Baseline | `def generate_report(reportfolderbase, time_in_secs, time_HMS, extraction_type, image_input_path, casedata, profile_filename, icons, lava_only)` |
| Comparison | `def generate_report(reportfolderbase, time_in_secs, time_HMS, extraction_type, image_input_path, casedata, profile_filename, icons)` |

### `scripts/search_files.py` — `FileSeekerBase.search`

| | Signature |
|:---|:---|
| Baseline | `def search(self, filepattern, return_on_first_hit=...)` |
| Comparison | `def search(self, filepattern_to_search, return_on_first_hit=...)` |
