This is a client (written in Python) for the Fishbowl Inventory API.

Currently supports add inventory request, cycle inventory count.

```
add_inventory(part_number, quantity, UOM_ID, cost, location_tag_num[,log])
```
```
cycle_inventory(part_number, new_qty, location_id[,log])
```

Optional argument log defaults to False.  If set to True, a log file will be created in the immediate directory and changes appended to it.


Example usage:
```
from fishwrapper import Fishbowlapi

stream = Fishbowlapi('admin', 'admin', '10.0.2.2')
stream.add_inventory('B500', 5, 1, 50.00, 386)
stream.close()
```
