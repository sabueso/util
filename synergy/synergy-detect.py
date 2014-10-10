#!/usr/bin/env python
import os,subprocess

comando=subprocess.check_output(['ip addr show'], shell=True)

#Saltos de linea legibles
#comando=subprocess.check_output(['ip addr show'], shell=True).splitlines()



hosts=[["192.168.120","192.168.120.100"],
	["192.168.100","192.168.100.40"]]

for line in hosts:
	if  line[0] in comando:
		#print "Estamos en "+str(line[0])+""
		subprocess.call("synergyc "+str(line[1])+"",shell=True)
		break

#for line in hosts:
#	print line[0]


