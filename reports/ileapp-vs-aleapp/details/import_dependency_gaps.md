# Import dependency gaps

- `main_entry.py` imports `scripts.ios_keychain:report_supplied_keychain` → missing `scripts/ios_keychain.py`
- `main_gui.py` imports `scripts.tz_offset:tzvalues` → missing `scripts/tz_offset.py`
- `scripts/ccl_leveldb.py` imports `scripts.ccl_simplesnappy` → missing `scripts/ccl_simplesnappy.py`
