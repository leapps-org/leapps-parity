# Signature changes

### `main_entry.py` — `crunch_artifacts`

| | Signature |
|:---|:---|
| Baseline | `@@def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, time_offset, profile_filename, itunes_backup_password=..., decryption_keys=..., image_password=..., found_members=..., hash_files=...)` |
| Comparison | `@@def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, profile_filename, image_password=..., found_members=..., hash_files=...)` |

### `scripts/artifact_report.py` — `ArtifactHtmlReport.write_artifact_data_table`

| | Signature |
|:---|:---|
| Baseline | `def write_artifact_data_table(self, data_headers, data_list, source_path, write_total=..., write_location=..., html_escape=..., cols_repeated_at_bottom=..., table_responsive=..., table_style=..., table_id=..., html_no_escape=..., row_count=..., row_limit=..., full_data_locations=..., html_multiline=...)` |
| Comparison | `def write_artifact_data_table(self, data_headers, data_list, source_path, write_total=..., write_location=..., html_escape=..., cols_repeated_at_bottom=..., table_responsive=..., table_style=..., table_id=..., html_no_escape=..., row_count=..., row_limit=..., full_data_locations=...)` |

### `scripts/lavafuncs.py` — `lava_finalize_output`

| | Signature |
|:---|:---|
| Baseline | `def lava_finalize_output(output_path, processing_status=...)` |
| Comparison | `def lava_finalize_output(output_path)` |

### `scripts/report.py` — `create_index_html`

| | Signature |
|:---|:---|
| Baseline | `def create_index_html(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, nav_list_data, casedata, profile_filename, lava_only, stopped_note=...)` |
| Comparison | `def create_index_html(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, nav_list_data, casedata, profile_filename, lava_only)` |

### `scripts/report.py` — `generate_key_val_table_without_headings`

| | Signature |
|:---|:---|
| Baseline | `def generate_key_val_table_without_headings(title, data_list, agency_logo_mimetype, agency_logo_b64)` |
| Comparison | `def generate_key_val_table_without_headings(title, data_list, html_escape=..., width=...)` |

### `scripts/report.py` — `generate_report`

| | Signature |
|:---|:---|
| Baseline | `def generate_report(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, casedata, profile_filename, icons, lava_only, stopped_note=...)` |
| Comparison | `def generate_report(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, casedata, profile_filename, icons, lava_only)` |
