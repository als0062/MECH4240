'''Build a read request to read the inputs from each device

need to have the device configured for all inputs then all outputs'''
from cplReadWrite import read

array_ObjType = ['analogOutput', 'analogInput', 'analogOutput', 'analogOutput', 'analogOutput', 'analogOutput']
array_PropId = ['presentValue', 'presentValue', 'presentValue', 'presentValue', 'presentValue', 'presentValue']

def deviceRead():
    readDic = {}          #create the outer dictionary layer
    index = 1
    maxInput = len(array_ObjType)
    while index <= maxInput:
        #print array_ObjType[index-1], index, array_PropId[index-1]
        readDic[index] = read(str(array_ObjType[index-1]), int(index), str(array_PropId[index-1]))       #Calls readRequest and gets the value from sensor, loops for each I/O port
        #print readDic[index]
        index = index+1
    return readDic
