import sys
sys.path.insert(0, '../database/database')
from sql_insert import insertNewRow
from createDeviceChain import createChain 
from cplReadWrite import doStart, doStop, read, write
import time, sys
from ErrorClasses import *

# STILL NEED TO DO ERROR CHECKING FOR WHOLE PROGRAM

setpoint = 80
deviceList = createChain()
started = False

#Testing Thread connections
connected = True
startM = time.time()
count = 0
run = True


#while run == True:
for x in range(0,1):
    count = count + 1
    start = time.time()                     ################################
    here = deviceList
    while here != None:
        try:
            print "Connecting to " + here.getObjectName()
            started = doStart(here)
            if started == True:
                start1 = time.time()            ################################
                numberOfConnectedPorts = len(here.getPort())+1
                readDic = {}
                manipulatedDic = {}
                
                # Reading all ports on device
                for item in range(1,numberOfConnectedPorts):
                    portObj = here.getPortItem(item)
                    readDic[int(portObj.getPortNum())] = read(here, portObj)
                end1 = time.time()              ################################
                print "After Reading all ports: " + str(readDic)                 
                #commit it to the database
                array = ['tempOA','tempRA','tempMA','tempPA','tempSA','humidityOA']
                valDic = {}
                for i in range(0,len(readDic)):
                    valDic[array[i]] = readDic[i+1]
                print valDic
                table = here.getObjectName()
                tablename = table.lower()
                print tablename
                insertNewRow(tablename, valDic)
               
                 #manipulate data
                for item in range(1,numberOfConnectedPorts):
                    portObj = here.getPortItem(item)
                    if portObj.getControlled():
                        manipulatedDic[portObj.getConnectedTo()] = portObj.Ploop(setpoint, readDic[portObj.getPortNum()])     #manipulatedDic should conatin the value from the Ploop with the key being the port of the actuator that the sensor is paired with
                print "after Ploop : " + str(manipulatedDic)
                        
                start2 = time.time()            ################################
                #print "Started write ..."
                for item in manipulatedDic:
                    portObj = here.getPortItem(item)
                    write(here, portObj, manipulatedDic[item])      
                end2 = time.time()              ################################

            
            
           # else:
           #     print 'An error has been captured: ' + str(started) + ", " + here.getObjectName()  + "\n\n"
            
        except ComputerNotConnectedToIP, exc:
            print exc 
        
        except:    
            print "You found a new error. Congrats!\n\n" #+ str(e)
        
        finally:
            if started == True:
                doStop() 
                print "The first read took: " + str(end1 - start1) + " seconds"
                print "The write took: " + str(end2 - start2) + " seconds"
                print "The whole program took: " + str(end2 - start) + " seconds\n\n" 
  #          else:
  #              connected = False
            here = here.getNext()
            #time.sleep(2)
            #print str(count) + "\n\n"
  #          if (count > 1 and connected == True) or time.time()-startM > .2:
  #              print "haha"
  #              run = False
                
#timeStop = time.time()                
#print "Tiem: " +str(timeStop - startM)
