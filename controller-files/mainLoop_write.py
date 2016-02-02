from readWrite import read, write, createApplication, doStop
from createDeviceChain import createChain 
from sql_insert import insertNewRow
import time, os, subprocess



#CHANGES
deviceChain = createChain()
device = deviceChain
print device
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
			manipulatedDic = {}
			print "Preparing to read ports..."
			for item in range(1,numberOfConnectedPorts):
				portObj = device.getPortItem(item)
				readDic[item] = read(i, device, portObj)

			print "After Reading all ports: " + str(readDic)


			#----------------------------------------
			#Hard Coded write statements for database
			#print "Writing values to database..."
			#These are just possible column key names. Ideally these would be read from a configuration database and would reflect
			#the actual key for the port.  
			#dummyColList = ['tempOA', 'humidityOA' ,'coOA', 'coRA', 'tempRA', 'tempMA', 'tempSA', 'damperPositionRA']
			#temp = {}
			#for j in range(0, len(readDic)):
			#	temp[dummyColList[j]] = readDic[j + 1]
			#print str(temp)
			#if i == 0:
			#	insertNewRow('controllerone', temp, 'sqlite:///../database/database/rh.db')
			#if i == 1:
			#	insertNewRow('controllertwo', temp, 'sqlite:///../database/database/rh.db')
			#----------------------------------------

			# P-Loop -- Proportional Control Loop
			#for item in range(1,numberOfConnectedPorts):
			#	portObj = device.getPortItem(item)
			#	if portObj.getControlled(): #gets portObj that are controlled 
					# manipulatedDic should contain the value from the Ploop with the key being the port of the actuator that the sensor is paired with
					# print readDic[portObj.getPortNum()]
					# hard coded write value:
					
					# getConnectedTo() returns the port number of the actuator that the sensor is paired with
					# manipulatedDic[portObj.getConnectedTo()] = portObj.Ploop(setpoint, readDic[portObj.getPortNum()]) 

			#print "P-Loop result: " + str(manipulatedDic)


			# testing response time of ports
			#if i == 0:
			#	manipulatedDic[5] = 10
			#elif i == 1:
			#	if x == 0:
			#		manipulatedDic = {1:10,2:10}
			#	else:
			#		manipulatedDic = {1:0,2:0}
			#print manipulatedDic

			# Writing values to controlled devices
			#for item in manipulatedDic:
			#	portObj = device.getPortItem(item)
			#	write(i, device, portObj, manipulatedDic[item])

			#----------------------------------------
			#if i == 0:
			#	print "Writing to C1 ports"
			#	portobj = device.getPortItem(6)
			#	print portobj
			#	write(i, device, portobj, 0)
			#	print "C1 write attempted"
			if i == 1:
				print "Writing to C2 ports"
				portobj = device.getPortItem(6)
				print portobj
				write(i, device, portobj, 0)
				print "C2 write attempted"
			#----------------------------------------

		except ValueError:
			print "Except: " + str(ValueError)
		finally:
			device = device.getNext()
			i += 1

		# threshold seems to be about 1.5 seconds for port one on controller two
		# sleep for 2 seconds in order to make sure actuator responds
		time.sleep(2)

time.sleep(2)

print "Stopping applications..."
i = 0
device = deviceChain
while device != None:
	doStop(i)
	i += 1
	device = device.getNext()

