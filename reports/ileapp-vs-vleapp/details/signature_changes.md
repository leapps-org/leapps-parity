# Signature changes

### `main_entry.py` — `crunch_artifacts`

| | Signature |
|:---|:---|
| Baseline | `def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, time_offset, profile_filename, itunes_backup_password=..., decryption_keys=...)` |
| Comparison | `def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, profile_filename)` |

### `scripts/report.py` — `generate_key_val_table_without_headings`

| | Signature |
|:---|:---|
| Baseline | `def generate_key_val_table_without_headings(title, data_list, agency_logo_mimetype, agency_logo_b64)` |
| Comparison | `def generate_key_val_table_without_headings(title, data_list, html_escape=..., width=...)` |
