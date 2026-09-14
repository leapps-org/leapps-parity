# Signature changes

### `main_entry.py` — `crunch_artifacts`

| | Signature |
|:---|:---|
| Baseline | `def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, time_offset, profile_filename, itunes_backup_password=..., decryption_keys=...)` |
| Comparison | `def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, profile_filename)` |

### `main_gui.py` — `run_crunch`

| | Signature |
|:---|:---|
| Baseline | `def run_crunch(message_queue, selected_modules, extracttype, input_path, out_params, wrap_text, case_info, time_offset, decryption_keys)` |
| Comparison | `def run_crunch(message_queue, selected_modules, extracttype, input_path, out_params, wrap_text, case_info)` |

### `scripts/report.py` — `create_index_html`

| | Signature |
|:---|:---|
| Baseline | `def create_index_html(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, nav_list_data, casedata, profile_filename, lava_only)` |
| Comparison | `def create_index_html(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, nav_list_data, casedata, profile_filename)` |

### `scripts/report.py` — `generate_report`

| | Signature |
|:---|:---|
| Baseline | `def generate_report(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, casedata, profile_filename, icons, lava_only)` |
| Comparison | `def generate_report(reportfolderbase, time_in_secs, time_hms, extraction_type, image_input_path, casedata, profile_filename, icons)` |
