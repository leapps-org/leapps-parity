# Import dependency gaps

- `ileappGUI.py` imports `scripts.context:Context` → missing `scripts/context.py`
- `ileappGUI.py` imports `scripts.tz_offset:tzvalues` → missing `scripts/tz_offset.py`
- `main_entry.py` imports `scripts.context:Context` → missing `scripts/context.py`
- `scripts/ccl_leveldb.py` imports `scripts.ccl_simplesnappy` → missing `scripts/ccl_simplesnappy.py`
- `scripts/ilapfuncs.py` imports `scripts.context:Context` → missing `scripts/context.py`
- `scripts/lavafuncs.py` imports `scripts.context:Context` → missing `scripts/context.py`
