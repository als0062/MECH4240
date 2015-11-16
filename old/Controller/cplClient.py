from cplReadWrite import read, write, doStop, doStart
import time


obj_type = 'analogInput'
obj_inst = int(2)
prop_id = 'presentValue'
ini_name = 'BACpypes'

doStart(ini_name)

confirmationValue = read(obj_type, obj_inst, prop_id)
print "Current Temperature: " + str(confirmationValue) + "\n"


obj_type = 'analogOutput'
obj_inst = int(3)
value = float(2)
index = int(0)
priority = int(1)

time.sleep(1)

confirmationValue = write(obj_type, obj_inst, prop_id, value, index, priority)
print "Write: " + str(confirmationValue)

value = float(0)

print "Lighting LED for 10 seconds\n"
time.sleep(10)
confirmationValue = write(obj_type, obj_inst, prop_id, value, index, priority)
print "Write: " + str(confirmationValue)

doStop()