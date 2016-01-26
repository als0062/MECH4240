from cplReadWrite import write

array_Port = [1,3,4,5,6]
array_ObjType = ['analogOutput', 'analogOutput', 'analogOutput', 'analogOutput','analogOutput']
array_PropId = ['presentValue', 'presentValue', 'presentValue', 'presentValue', 'presentValue']

def deviceWrite(array_WriteVal):
    index = int(0)
    priority = int(1)
    writeVal = array_WriteVal
    for count in array_WriteVal:
        #print count, array_ObjType[count], array_Port[count],array_PropId[count], writeVal[count]
        write(str(array_ObjType[count]), int(array_Port[count]),str(array_PropId[count]), float(writeVal[count]), index, priority)
