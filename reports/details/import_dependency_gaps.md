# Import dependency gaps

- `ileappGUI.py` imports `leapps.functions.history` → missing `leapps/functions/history.py`
- `ileappGUI.py` imports `scripts.tz_offset:tzvalues` → missing `scripts/tz_offset.py`
- `main_entry.py` imports `leapps.functions.history` → missing `leapps/functions/history.py`
- `scripts/ccl_leveldb.py` imports `scripts.ccl_simplesnappy` → missing `scripts/ccl_simplesnappy.py`
