# Import dependency gaps

- `main_entry.py` imports `scripts.ios_keychain:report_supplied_keychain` → missing `scripts/ios_keychain.py`
- `main_gui.py` imports `scripts.tz_offset:tzvalues` → missing `scripts/tz_offset.py`
- `scripts/blackboxprotobuf/__init__.py` imports `scripts.blackboxprotobuf.lib.interface:*` → missing `scripts/blackboxprotobuf/lib/interface.py`
- `scripts/blackboxprotobuf/lib/interface.py` imports `scripts.blackboxprotobuf.lib.types.length_delim` → missing `scripts/blackboxprotobuf/lib/types/length_delim.py`
- `scripts/blackboxprotobuf/lib/interface.py` imports `scripts.blackboxprotobuf.lib.types.type_maps` → missing `scripts/blackboxprotobuf/lib/types/type_maps.py`
- `scripts/blackboxprotobuf/lib/types/length_delim.py` imports `scripts.blackboxprotobuf.lib.types` → missing `scripts/blackboxprotobuf/lib/types/__init__.py`
- `scripts/blackboxprotobuf/lib/types/length_delim.py` imports `scripts.blackboxprotobuf.lib.types:varint` → missing `scripts/blackboxprotobuf/lib/types/__init__.py`
- `scripts/blackboxprotobuf/lib/types/type_maps.py` imports `scripts.blackboxprotobuf.lib.types:fixed` → missing `scripts/blackboxprotobuf/lib/types/__init__.py`
- `scripts/blackboxprotobuf/lib/types/type_maps.py` imports `scripts.blackboxprotobuf.lib.types:length_delim` → missing `scripts/blackboxprotobuf/lib/types/__init__.py`
- `scripts/blackboxprotobuf/lib/types/type_maps.py` imports `scripts.blackboxprotobuf.lib.types:varint` → missing `scripts/blackboxprotobuf/lib/types/__init__.py`
- `scripts/ccl_leveldb.py` imports `scripts.ccl_simplesnappy` → missing `scripts/ccl_simplesnappy.py`
