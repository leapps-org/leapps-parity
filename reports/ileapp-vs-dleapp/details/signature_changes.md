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
