from readWrite import read, write, createApplication, doStop
from createDeviceChain import createChain 
from sql_insert import insertNewRow
import time, os, subprocess



#CHANGES
deviceChain = createChain()
device = deviceChain
setpoint = 72


i = 0

while device != None:
	try:
		if i < 2:
			createApplication(device)
	except:
		print "Except: "
	finally:
		device = device.getNext()
		i += 1


for x in range(0,2):
	device = deviceChain
	i = 0	
	while device != None:

		print device.getObjectName()

		try:
			numberOfConnectedPorts = len(device.getPort())+1
			print "numberOfConnectedPorts: " + str(numberOfConnectedPorts)
			readDic = {}
			# manipulatedDic = {}
			# print "Preparing to read ports..."
			# getting error somewhere below
			for item in range(1,numberOfConnectedPorts):
				portObj = device.getPortItem(item)
				readDic[item] = read(i, device, portObj)
			print "After Reading all ports: " + str(readDic)
			#----------------------------------------

			#----------------------------------------
		except ValueError:
			print "Except: " + str(ValueError)
		finally:
			device = device.getNext()
			i += 1

time.sleep(1.5)

print "Stopping applications..."
i = 0
device = deviceChain
while device != None:
	doStop(i)
	i += 1
	device = device.getNext()
print "Applications successfully stopped."


