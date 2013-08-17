# -*- coding: utf-8 -*-

from ghost import Ghost
from PyQt4 import QtCore
from bs4 import BeautifulSoup
import urllib
import urllib2
import json

class TaipeiBus:
	def __init__(self):
		self.index_url = "http://pda.5284.com.tw/MQS/businfo1.jsp"
		self.bus_url = "http://pda.5284.com.tw/MQS/businfo2.jsp?routename="
	
	def fetchBusList(self):
		ghost = Ghost()
		page, resources = ghost.open(self.index_url)
		assert page.http_status==200
		result, resources = ghost.evaluate("routeArray")
		bus_list = [unicode(x).encode("utf8") for x in result]
		return bus_list
	
	def fetchBusRoute(self, bus_name):
		bus_new_url = self.bus_url + bus_name
		bus_info = {"name":bus_name,"forward":[],"backward":[]}
		bus_stop = []
		req = urllib2.Request(bus_new_url)
		f = urllib2.urlopen(req,timeout=2)
		bus_index = f.read()
		soup = BeautifulSoup(bus_index)
		table = soup.find_all("table")
		for bus_stop in table[2].find_all("tr"):
			td_data = bus_stop.find_all("td")
			bus_info["forward"].append((td_data[0].string,td_data[0].a['href']))
			bus_stop.append((td_data[0].string,bus_name))
		for bus_stop in table[3].find_all("tr"):
			td_data = bus_stop.find_all("td")
			bus_info["backward"].append((td_data[0].string,td_data[0].a['href']))
		return bus_info, bus_stop
	
	def generateBusStop(self, bus_stop_list):
		bus_stop = {}
		for each_bus in bus_stop_list:
			for each_stop in each_bus:
				if(bus_stop[each_stop[0]] in bus_stop):
					bus_stop[each_stop[0]].append(each_stop[1])
				else:
					bus_stop[each_stop[0]] = []
					bus_stop[each_stop[0]].append(each_stop[1])
		
		return bus_stop
			
	
	
	
	
	
	
	
	"def fetchBusInfo(self,bus_name):"
		
if __name__=="__main__":
	print("This is a class")
