import sys
sys.path.insert(0, '../database/database')
from sql_insert import insertNewRow
from createDeviceChain import createChain 
from cplReadWriteThreading import doStart, doStop, read, write
import time, sys
from ErrorHandler import ErrorHandler

# STILL NEED TO DO ERROR CHECKING FOR WHOLE PROGRAM

setpoint = 80
deviceList = createChain()
started = False
applicationDic = {}

device = deviceList
while device != None:
    applicationDic[device.getObjectName()] = doStart(device)
    device = device.getNext()
print applicationDic
time.sleep(5)



for x in range(0,1):
    start = time.time()                     ################################
    here = deviceList
    while here != None:
        try:
            print "\nConnecting to " + here.getObjectName()
        #    started = doStart(here)
            app = (applicationDic[here.getObjectName()] != None)
            if app == True:
                start1 = time.time()            ################################
                numberOfConnectedPorts = len(here.getPort())+1
                readDic = {}
                manipulatedDic = {}
                
                # Reading all ports on device
                for item in range(1,numberOfConnectedPorts):
                    portObj = here.getPortItem(item)
                    #readDic[portObj.getPortName()] = read(here, portObj)
                    readDic[item] = read(applicationDic[here.getObjectName()], here, portObj)
                end1 = time.time()              ################################
                print "After Reading all ports: " + str(readDic)                 
            else:
                print "No application for device %s" %here.getObjectName()
        except Exception, e:    
            ErrorHandler(e)
        
        finally:
            if app == True: 
                doStop()
                #print "The first read took: " + str(end1 - start1) + " seconds"
                #print "The write took: " + str(end2 - start2) + " seconds"
                #print "The whole program took: " + str(end2 - start) + " seconds\n\n" 
            here = here.getNext()

