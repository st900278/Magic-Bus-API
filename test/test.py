# -*- coding: utf-8 -*-

import os,sys
import json

sys.path.append("..")
from Taipei_Bus.Taipei_Bus import TaipeiBus
bus_stop_list = {}

log = open("log.txt","a")
bus = TaipeiBus()

bus_list = bus.fetchBusList()
with open("bus_list.txt","w") as text_file:
	text_file.writelines(str(i) + "\n" for i in bus_list)
log.write("bus_list.txt is written.\n")
log.flush()
'''
for x in ["274","281","297","704區","705","706","711","918延","940","F921","南軟通勤專車雙和","棕15區","橘13","紅33"]:
	try:
		"info is a dict; stop is a list;"
		bus_info, bus_stop = bus.fetchBusRoute(x)
		f = open("bus_info/" + x + "-info.json", "w")
		f.write(json.dumps(bus_info))
		f.close()
		log.write(x + "-info.json is written.\n")
		log.flush()
		print x + "-info.json is written.\n"
		with open("bus_stop/" + x + "-stop.txt", "w") as f:
			f.writelines(i.encode("utf8") + "\n" for i in bus_stop)
		log.write(x + "-stop.txt is written. \n")
		log.flush()
		print x + "-stop.txt is written.\n"

	except:
		log.write(x + " Failed\n")
		log.flush()
		
log.close()

'''
stop_list = []
for x in os.walk("./bus_stop"):
	stop_list = x[2]
for x in stop_list:
	recent_stop = []
	t ={}
	url = "./bus_stop/" + x
	bus_name = x.split("-stop")[0]
	with open(url,"r") as f:
		for text in f.readlines():
			stop_name = text[0:-1]
			print stop_name
			recent_stop.append((stop_name,bus_name))
	bus.generateBusStop(recent_stop,bus_stop_list)
			
			
print json.dumps(bus_stop_list)
	
