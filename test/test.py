# -*- coding: utf-8 -*-


import os,sys
sys.path.append("..")
from Taipei_Bus.Taipei_Bus import TaipeiBus


bus = TaipeiBus()
bus_info = {}
bus_stop = []
bus_list = bus.fetchBusList()
with open("bus_list.txt","w") as text_file:
	text_file.writelines(str(i) + "\n" for i in bus_list)
	

for x in bus_list:
	bus_info, bus_stop = bus.fetchBusRoute(x)
	
