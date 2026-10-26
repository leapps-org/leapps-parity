# Signature changes

### `main_entry.py` — `crunch_artifacts`

| | Signature |
|:---|:---|
| Baseline | `@@def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, time_offset, profile_filename, itunes_backup_password=..., decryption_keys=..., image_password=..., found_members=..., hash_files=...)` |
| Comparison | `@@def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, profile_filename, image_password=..., found_members=..., hash_files=...)` |

### `main_gui.py` — `run_crunch`

| | Signature |
|:---|:---|
| Baseline | `def run_crunch(message_queue, selected_modules, extracttype, input_path, out_params, wrap_text, case_info, time_offset, decryption_keys, image_password=..., found_members=..., hash_files=...)` |
| Comparison | `def run_crunch(message_queue, selected_modules, extracttype, input_path, out_params, wrap_text, case_info, image_password=..., found_members=..., hash_files=...)` |

### `scripts/report.py` — `generate_key_val_table_without_headings`

| | Signature |
|:---|:---|
| Baseline | `def generate_key_val_table_without_headings(title, data_list, agency_logo_mimetype, agency_logo_b64)` |
| Comparison | `def generate_key_val_table_without_headings(title, data_list, html_escape=..., width=...)` |
