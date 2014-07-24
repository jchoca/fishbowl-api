#!/usr/bin/python
# -*- coding: utf-8 -*-

def getstatus(code):
    if code == "1000":
        value = "Success!"
    elif code == "1001":
        value = "Unknown Message Received"
    elif code == "1002":
        value = "Connection to Fishbowl Server was lost"
    elif code == "1003":
        value = "Some Requests had errors -- now isn't that helpful..."
    elif code == "1004":
        value = "There was an error with the database."
    elif code == "1009":
        value = "Fishbowl Server has been shut down."
    elif code == "1010":
        value = "You have been logged off the server by an administrator."
    elif code == "1012":
        value = "Unknown request function."
    elif code == "1100":
        value = "Unknown login error occurred."
    elif code == "1110":
        value = "A new Integrated Application has been added to Fishbowl Inventory. Please contact your Fishbowl Inventory Administrator to approve this Integrated Application."
    elif code == "1111":
        value = "This Integrated Application registration key does not match."
    elif code == "1112":
        value = "This Integrated Application has not been approved by the Fishbowl Inventory Administrator."
    elif code == "1120":
        value = "Invalid Username or Password."
    elif code == "1130":
        value = "Invalid Ticket passed to Fishbowl Inventory Server."
    elif code == "1131":
        value = "Invalid Key value."
    elif code == "1140":
        value = "Initialization token is not correct type."
    elif code == "1150":
        value = "Request was invalid"
    elif code == "1160":
        value = "Response was invalid."
    elif code == "1162":
    	value = "The login limit has been reached for the server's key."
    elif code == "1200":
        value = "Custom Field is invalid."
    elif code == "1500":
        value = "The import was not properly formed."
    elif code == "1501":
        value = "That import type is not supported"
    elif code == "1502":
        value = "File not found."
    elif code == "1503":
        value = "That export type is not supported."
    elif code == "1504":
        value = "File could not be written to."
    elif code == "1505":
        value = "The import data was of the wrong type."
    elif code == "2000":
        value = "Was not able to find the Part {0}."
    elif code == "2001":
        value = "The part was invalid."
    elif code == "2100":
        value = "Was not able to find the Product {0}."
    elif code == "2101":
        value = "The product was invalid."
    elif code == "2200":
        value = "The yield failed."
    elif code == "2201":
        value = "Commit failed."
    elif code == "2202":
        value = "Add initial inventory failed."
    elif code == "2203":
        value = "Can not adjust committed inventory."
    elif code == "2300":
        value = "Was not able to find the Tag number {0}."
    elif code == "2301":
        value = "The tag is invalid."
    elif code == "2302":
        value = "The tag move failed."
    elif code == "2303":
        value = "Was not able to save Tag number {0}."
    elif code == "2304":
        value = "Not enough available inventory in Tagnumber {0}."
    elif code == "2305":
        value = "Tag number {0} is a location."
    elif code == "2400":
        value = "Invalid UOM."
    elif code == "2401":
        value = "UOM {0} not found."
    elif code == "2402":
        value = "Integer UOM {0} cannot have non-integer quantity."
    elif code == "2500":
        value = "The Tracking is not valid."
    elif code == "2510":
        value = "Serial number is missing."
    elif code == "2511":
        value = "Serial number is null."
    elif code == "2512":
        value = "Serial number is duplicate."
    elif code == "2513":
        value = "Serial number is not valid."
    elif code == "2600":
        value = "Location not found."
    elif code == "2601":
        value = "Invalid location."
    elif code == "2602":
        value = "Location Group {0} not found."
    elif code == "3000":
        value = "Customer {0} not found."
    elif code == "3001":
        value = "Customer is invalid."
    elif code == "3100":
        value = "Vendor {0} not found."
    elif code == "3101":
        value = "Vendor is invalid."
    elif code == "4000":
        value = "There was an error load PO {0}."
    elif code == "4001":
        value = "Unknow status {0}."
    elif code == "4002":
        value = "Unknown carrier {0}."
    elif code == "4003":
        value = "Unknown QuickBooks class {0}."
    elif code == "4004":
        value = "PO does not have a PO number. Please turn on the auto-assign PO number option in the purchase order module options."
    else:
        value = 'Unknown status'
    return value
