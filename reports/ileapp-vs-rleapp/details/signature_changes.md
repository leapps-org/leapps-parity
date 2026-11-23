# Signature changes

### `main_entry.py` — `crunch_artifacts`

| | Signature |
|:---|:---|
| Baseline | `@@def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, time_offset, profile_filename, itunes_backup_password=..., decryption_keys=..., image_password=..., found_members=..., hash_files=...)` |
| Comparison | `@@def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, profile_filename, image_password=..., found_members=..., hash_files=...)` |

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

### `scripts/report.py` — `generate_report`

| | Signature |
|:---|:---|
| Baseline | `def generate_report(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, casedata, profile_filename, icons, lava_only, stopped_note=...)` |
| Comparison | `def generate_report(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, casedata, profile_filename, icons, lava_only)` |
