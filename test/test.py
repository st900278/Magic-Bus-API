# -*- coding: utf-8 -*-

import os,sys
import json

sys.path.append("..")
from Taipei_Bus.Taipei_Bus import TaipeiBus


log = open("log.txt","a")
bus = TaipeiBus()
bus_stop = {}
bus_list = bus.fetchBusList()
with open("bus_list.txt","w") as text_file:
	text_file.writelines(str(i) + "\n" for i in bus_list)
log.write("bus_list.txt is written.\n")
log.flush()
for x in ["905","B31華江","棕1","紅19","綠1"]:
	try:
		"info is a dict; stop is a list;"
		bus_info, bus_stop = bus.fetchBusRoute(x)
		f = open("bus_info/" + x + "-info.json", "w")
		f.write(json.dumps(bus_info))
		f.close()
		log.write(x + "-info.json is written.\n")
		log.flush()
		print x + "-info.json is written.\n"
		print bus_stop
		with open("bus_stop/" + x + "-stop.txt", "w") as f:
			f.writelines(i.encode("utf8") + "\n" for i in bus_stop)
		log.write(x + "-stop.txt is written. \n")
		log.flush()
		print x + "-stop.txt is written.\n"

	except:
		log.write(x + " Failed\n")
		log.flush()


log.close()

