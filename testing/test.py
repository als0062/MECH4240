from iniParser import *
from Class import *
from SQL.sql_query import *


iniName = queryColumn(Devices, "ini")
for x in range(0,len(iniName)):
    value = iniParser("iniFiles/" + str(iniName[x]))
    value.append(CompIPToRequestIP(value[1]))
    if x == 0:
        deviceList = Device(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9])
        counter = deviceList
    elif x ==1 :
        temp = Device(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9])
        deviceList.addDevice(temp)
        counter = counter.getNext()
    else:
        temp = Device(value[0],value[1],value[2],value[3],value[4],value[5],value[6],value[7],value[8],value[9])
        counter.addDevice(temp)
        counter = counter.getNext()
        

for x in range(1,4):
    here = deviceList
    while here != None: 
        print here.getObjectName()
        here = here.getNext()
