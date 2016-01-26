# This file creates a singly linked list of Device objects. Each device object holds all of the information that is needed for a single controller and a pointer to the next device object in the list. 
#The last item in the list holds a pointer to a null item to signify the end of the list.


import sys
sys.path.append('../database/database')
from iniParser import iniParser, CompIPToRequestIP, parsePorts
from Class import *
from sql_query import queryColumn 



#SUMMARY
def createChain():
    # This retrives the name of all of the ini files that are listed in the database.
    iniName = queryColumn('devices', "ini", 'sqlite:///../database/database/rh.db')

    for index in range(0,len(iniName)):
        portDic = None  #a dictionary of port objects
        deviceDic = None #a dictionary of device objects
        
        #ADD A CHECK TO SEE IF FILE EXISTS
        
        #parses the ini file section, BACPYPES, to return a dictionary of controller properties
        deviceDic = iniParser("iniFiles/" + str(iniName[index]))
        #adds the request IP to the dictionary (this is the device IP - 1)
        deviceDic['requestip'] = CompIPToRequestIP(deviceDic['address'])
        #parses the PORTS section of the ini file to return a dictionary of port properties
        portDic = parsePorts("iniFiles/" + str(iniName[index]))

        #for each item in the ports dictionary, create a port object of that name and return it to a dictionary with the port number as the dictionary key
        for port in portDic:
            portDic[port] = instantiatePortClass(portDic[port], portNumber(port))
        
        #This if statement links the device objects into the linked list. I do not think the elif statement is nessacary but I did not want to remove it or change the code befor the presentation.
        if index == 0:
            deviceList = Device(deviceDic, portDic)
            counter = deviceList
        elif index ==1 :
            temp = Device(deviceDic, portDic)
            deviceList.addDevice(temp)
            counter = counter.getNext()                     
        else:
            temp = Device(deviceDic, portDic)
            counter.addDevice(temp)
            counter = counter.getNext()

    return deviceList


#This method 
def instantiatePortClass(str_className,portNum):
    if str_className.lower() == "led":
        return DamperPositionOA(portNum)
    elif str_className.lower() == "thermistorcc":
        # TempSA(self,pairedPort)
        return TempSA(portNum, 1)
    elif str_className.lower() == "thermistorhc":
        return TempPA(portNum, 3)
    else:
        return "Error: Type not recognised"
    
#   
def portNumber(str_portNum):
    if str_portNum.lower() == "portone":
        return 1
    elif str_portNum.lower() == "porttwo":
        return 2
    elif str_portNum.lower() == "portthree":
        return 3     
    elif str_portNum.lower() == "portfour":
        return 4    
    elif str_portNum.lower() == "portfive":
        return 5
    elif str_portNum.lower() == "portsix":
        return 6
    elif str_portNum.lower() == "portseven":
        return 7
    elif str_portNum.lower() == "porteight":
        return 8
    elif str_portNum.lower() == "portnine":
        return 9

