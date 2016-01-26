import sys
sys.path.insert(0, '../database/database')
from sql_insert import insertNewRow
from createDeviceChain import createChain 
from cplReadWrite import doStart, doStop, read, write
import time, sys
from ErrorHandler import ErrorHandler
import os
import subprocess

from threading import Thread

# STILL NEED TO DO ERROR CHECKING FOR WHOLE PROGRAM

setpoint = 80
deviceList = createChain()
started = False


for x in range(0,1):
    start = time.time()                     ################################
    here = deviceList

    while here != None:
        try:
            print "\nConnecting to " + here.getObjectName()
            #started = doStart(here)

            ipAddress = here.getRequestAddress()
            with open(os.devnull, "wb") as limbo:
                result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ipAddress],
                        stdout=limbo, stderr=limbo).wait()
                if result:
                        started = False
                else:
                        started = doStart(here)
            if started == True:
                start1 = time.time()            ################################
                numberOfConnectedPorts = len(here.getPort())+1
                readDic = {}
                manipulatedDic = {}
                
                # Reading all ports on device
                for item in range(1,numberOfConnectedPorts):
                    portObj = here.getPortItem(item)
                    #readDic[portObj.getPortName()] = read(here, portObj)
                    readDic[item] = read(here, portObj)
                end1 = time.time()              ################################
                print "After Reading all ports: " + str(readDic)                 
                
                #commit it to the database, NOT FUllY WORKING. Uses dummy data for column name.
    #     array = ['tempOA','tempRA','tempMA','tempPA','tempSA','humidityOA']
    #            valDic = {}
    #            for i in range(0,len(readDic)):
    #                
    #                valDic[array[i]] = readDic[i+1]
    #            print valDic
        #        table = here.getObjectName()
        #       tablename = table.lower()
        #        print tablename
        #        insertNewRow(tablename, valDic)
               
                 #manipulate data
                for item in range(1,numberOfConnectedPorts):
                    portObj = here.getPortItem(item)
                    if portObj.getControlled():
                        #manipulatedDic should conatin the value from the Ploop with the key being the port of the actuator that the sensor is paired with
                        manipulatedDic[portObj.getConnectedTo()] = portObj.Ploop(setpoint, readDic[portObj.getPortNum()])     
                print "P-Loop result: " + str(manipulatedDic)
                        
                start2 = time.time()            ################################
                #print "Started write ..."
                for item in manipulatedDic:
                    portObj = here.getPortItem(item)
                    write(here, portObj, manipulatedDic[item])      
                end2 = time.time()              ################################
        
        except Exception, e:    
            # ErrorHandler(e)
            print e
        
        finally:
            if started == True:
                doStop() 
                #print "The first read took: " + str(end1 - start1) + " seconds"
                #print "The write took: " + str(end2 - start2) + " seconds"
                #print "The whole program took: " + str(end2 - start) + " seconds\n\n" 
            here = here.getNext()

