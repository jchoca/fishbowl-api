from fishwrapper import Fishbowlapi

stream = Fishbowlapi('admin', 'admin', '10.0.2.2')
stream.add_inventory('B500', 5, 1, 50.00, 386)
stream.close()