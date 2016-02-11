from readWrite import read, write, createApplication, doStop
from createDeviceChain import createChain 
from sql_insert import insertNewRow
import time, os, subprocess

#CHANGES
deviceChain = createChain()
device = deviceChain
#setpoint = 72

i = 0

while device != None:
	try:
		if i < 2:
			createApplication(device)
	except:
		print "EXCEPTION: TOO MANY DEVICES CREATED BY DEVICECHAIN"
	finally:
		device = device.getNext()
		i += 1
count = 0

while count < 100:
	for x in range(0,2):
		device = deviceChain
		i = 0	
		while device != None:

			print device.getObjectName()

			try:
				numberOfConnectedPorts = len(device.getPort())+1
				print "numberOfConnectedPorts: " + str(numberOfConnectedPorts)
				readDic = {}
				#manipulatedDic = {}
				print "Preparing to read ports..."
				for item in range(1,numberOfConnectedPorts):
					portObj = device.getPortItem(item)
					readDic[item] = read(i, device, portObj)

				print "After Reading all ports: " + str(readDic)


				#----------------------------------------
				#Hard Coded write statements for database
				print "Writing values to database..."
				#These are just possible column key names. Ideally these would be read from a configuration database and would reflect
				#the actual key for the port.  
				#dummyColList = ['tempOA', 'humidityOA' ,'coOA', 'coRA', 'tempRA', 'tempMA', 'tempSA', 'damperPositionRA']
				dummyColListOne = ['tempOA','tempRA','tempMA','tempSA','valuePositionCW']
				dummyColListTwo = ['damperPositionOA','damperPositionRA', 'fanSpeedOutput', 'fanSpeedFrequency', 'airFlowOA' ] 
				#fanSpeedOutput and fanSpeedFrequency are dummy placeholders to hold an empty port
				temp = {}
				for j in range(0, len(readDic)):
					if i == 0:
						temp[dummyColListOne[j]] = readDic[j + 1]
					if i == 1:
						temp[dummyColListTwo[j]] = readDic[j + 1]
				print str(temp)
				if i == 0:
					insertNewRow('controllerone', temp, 'sqlite:///../database/database/rh.db')
				if i == 1:
					insertNewRow('controllertwo', temp, 'sqlite:///../database/database/rh.db')


				#----------------------------------------

				# for item in range(1,numberOfConnectedPorts):
				# 	portObj = device.getPortItem(item)
				# 	if portObj.getControlled():
				# 		#manipulatedDic should contain the value from the Ploop with the key being the port of the actuator that the sensor is paired with
				# 		print readDic[portObj.getPortNum()]
				# 		manipulatedDic[portObj.getConnectedTo()] = portObj.Ploop(setpoint, readDic[portObj.getPortNum()])     
				# print "P-Loop result: " + str(manipulatedDic)

				# for item in manipulatedDic:
				# 	portObj = device.getPortItem(item)
				# 	write(i, device, portObj, manipulatedDic[item])

			except ValueError:
				print "Except: " + str(ValueError)
			finally:
				device = device.getNext()
				i += 1

	time.sleep(1.5)
	count += 1

print "Stopping applications..."
i = 0
device = deviceChain
while device != None:
	doStop(i)
	i += 1
	device = device.getNext()

