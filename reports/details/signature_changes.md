# Signature changes

### `main_entry.py` — `crunch_artifacts`

| | Signature |
|:---|:---|
| Baseline | `def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, time_offset, profile_filename, itunes_backup_password=..., decryption_keys=...)` |
| Comparison | `def crunch_artifacts(plugins, extracttype, input_path, out_params, wrap_text, loader, casedata, profile_filename)` |

### `scripts/plugin_loader.py` — `PluginLoader.__init__`

| | Signature |
|:---|:---|
| Baseline | `def __init__(self, plugin_paths=...)` |
| Comparison | `def __init__(self, plugin_path=...)` |

### `scripts/plugin_loader.py` — `PluginLoader._load_plugins`

| | Signature |
|:---|:---|
| Baseline | `def _load_plugins(self, plugin_path)` |
| Comparison | `def _load_plugins(self)` |

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
