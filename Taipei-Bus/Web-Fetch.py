# -*- coding: utf-8 -*-

from ghost import Ghost
from PyQt4 import QtCore
from bs4 import BeautifulSoup
import urllib
import urllib2
"Fetch Catalog Web"

url = "http://pda.5284.com.tw/MQS/businfo1.jsp"
bus_info = []
index = 0
"Fetch Bus List"
ghost = Ghost()
page, resources = ghost.open(url)
assert page.http_status==200
result, resources = ghost.evaluate("routeArray")
data = [unicode(x).encode("utf8") for x in result]  


for bus in data:
	bus_url = "http://pda.5284.com.tw/MQS/businfo2.jsp?routename=" + bus
	print bus_url
	bus_info.append(bus)
	
	req = urllib2.Request(bus_url)
	f = urllib2.urlopen(req)
	bus_index = f.read()
	soup = BeautifulSoup(bus_index)
	table = soup.find_all("table")
	for bus_stop in table[2].find_all("tr"):
		td_data = bus_stop.find_all("td")
		print td_data[0].string
		print td_data[0].a['href']
		if(td_data[1].find("font") != None):
			td_data[1].font.extract()
		print td_data[1].string
	for bus_stop in table[3].find_all("tr"):
		td_data = bus_stop.find_all("td")
		print td_data[0].string
		print td_data[0].a['href']
		if(td_data[1].find("font") != None):
			td_data[1].font.extract()
		print td_data[1].string





'''
for bus in data:
	bus_url = "http://pda.5284.com.tw/MQS/businfo2.jsp?routename=" + bus
	print bus_url
	req = urllib2.Request(bus_url)
	f = urllib2.urlopen(req)
	bus_index = f.read()
	soup = BeautifulSoup(bus_index)

	print soup.table
'''

"Get the Catalog"

'''
bus{
	name
	type
	stop{
		name
		url
	}


}
'''
