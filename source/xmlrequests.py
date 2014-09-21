#!/usr/bin/python
# -*- coding: utf-8 -*-
from lxml import etree


class Request:
	def __init__(self, key=""):
		self.el_fbixml = etree.Element('FbiXml')
		self.el_ticket = etree.SubElement(self.el_fbixml, 'Ticket')
		self.el_key = etree.SubElement(self.el_ticket, 'Key')
		self.el_key.text = key
		self.el_fbimsgsrq = etree.SubElement(self.el_fbixml, 'FbiMsgsRq')

class Login(Request):
	def __init__(self, username, password, key=""):
		Request.__init__(self, key)
		self.el_loginrq = etree.SubElement(self.el_fbimsgsrq, 'LoginRq')
		self.el_iaid = etree.SubElement(self.el_loginrq, 'IAID')
		self.el_iaid.text = '22'
		self.el_ianame = etree.SubElement(self.el_loginrq, 'IAName')
		self.el_ianame.text = 'PythonApp'
		self.el_iadesc = etree.SubElement(self.el_loginrq, 'IADescription')
		self.el_iadesc.text = 'Connection for Python Wrapper'
		self.el_username = etree.SubElement(self.el_loginrq, 'UserName')
		self.el_username.text = username
		self.el_password = etree.SubElement(self.el_loginrq, 'UserPassword')
		self.el_password.text = password
		xmlmsg = etree.tostring(self.el_fbixml, pretty_print=True)
		self.request = xmlmsg

class AddInventory(Request):
	def __init__(self, partnum, qty, uomid, cost, loctagnum, note="", tracking="", key=""):
		Request.__init__(self, key)
		if key == '':
			raise TypeError("An API key was not provided (not enough aruments for " + 
				            self.__class__.__name__ + " request)")
		self.el_addinventoryrq = etree.SubElement(self.el_fbimsgsrq, 'AddInventoryRq')
		self.el_partnum = etree.SubElement(self.el_addinventoryrq, 'PartNum')
		self.el_partnum.text = partnum
		self.el_quantity = etree.SubElement(self.el_addinventoryrq, 'Quantity')
		self.el_quantity.text = qty
		self.el_uomid = etree.SubElement(self.el_addinventoryrq, 'UOMID')
		self.el_uomid.text = uomid
		self.el_cost = etree.SubElement(self.el_addinventoryrq, 'Cost')
		self.el_cost.text = cost
		self.el_note = etree.SubElement(self.el_addinventoryrq, 'Note')
		self.el_note.text = note
		self.el_tracking = etree.SubElement(self.el_addinventoryrq, 'Tracking')
		self.el_note.text = tracking
		self.el_loctagnum = etree.SubElement(self.el_addinventoryrq, 'LocationTagNum')
		self.el_loctagnum.text = loctagnum
		self.el_tagnum = etree.SubElement(self.el_addinventoryrq, 'TagNum')
		self.el_tagnum.text = '0'
		xmlmsg = etree.tostring(self.el_fbixml, pretty_print=True)
		self.request = xmlmsg

class CycleCount(Request):
	def __init__(self, partnum, qty, locationid, tracking="", key=""):
		Request.__init__(self, key)
		if key == '':
			raise TypeError("An API key was not provided (not enough aruments for " + 
				            self.__class__.__name__ + " request)")
		self.el_cyclecountrq = etree.SubElement(self.el_fbimsgsrq, 'CycleCountRq')
		self.el_partnum = etree.SubElement(self.el_cyclecountrq, 'PartNum')
		self.el_partnum.text = partnum
		self.el_quantity = etree.SubElement(self.el_cyclecountrq, 'Quantity')
		self.el_quantity.text = qty
		self.el_locationid = etree.SubElement(self.el_cyclecountrq, 'LocationID')
		self.el_locationid.text = locationid
		xmlmsg = etree.tostring(self.el_fbixml, pretty_print=True)
		self.request = xmlmsg

class GetPOList(Request):
	def __init__(self, locationgroup, key=""):
		Request.__init__(self, key)
		if key == '':
			raise TypeError("An API key was not provided (not enough aruments for " + 
				            self.__class__.__name__ + " request)")
		self.el_getpolistrq = etree.SubElement(self.el_fbimsgsrq, 'GetPOListRq')
		self.el_locationgroup = etree.SubElement(self.el_getpolistrq, 'LocationGroup')
		self.el_locationgroup.text = locationgroup
		xmlmsg = etree.tostring(self.el_fbixml, pretty_print=True)
		self.request = xmlmsg	