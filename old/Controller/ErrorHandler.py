
def ErrorHandler(error,device):
	errNumber = error[0]
	if errNumber == 99:
            print "Can not connect to requested device %s at address %s" % (device.getObjectName(), device.getDeviceAddress())
            #raise error
        elif errNumber == 49:
            print "Address %s is already in use. No connection made to device %s" % (device.getDeviceAddress(), device.getObjectName())
        else:    
            print str(error)
