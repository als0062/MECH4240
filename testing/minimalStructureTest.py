import database

print database.databaseCreation()
table = 'Devices'
rowOne = {'name':'ControllerOne','ini':'ControllerOne.ini','ip':'192.168.92.69','mac':'macAddressOne'}
rowTwo = {'name':'ControllerTwo','ini':'ControllerTwo.ini','ip':'192.168.92.70','mac':'macAddressTwo'}
rowThree = {'name':'ControllerThree','ini':'ControllerThree.ini','ip':'192.168.92.71','mac':'macAddressThree'}
rowFour = {'name':'ControllerFour','ini':'ControllerFour.ini','ip':'192.168.92.72','mac':'macAddressFour'}

database.insertNewRow(table, rowOne)
database.insertNewRow(table, rowTwo)
database.insertNewRow(table, rowThree)
database.insertNewRow(table, rowFour)

tablename = 'Setpoints'
setpointrow = {'tempSA':70,'tempMA':72,'tempPA':73,'tempSA':75,'humidityRA':20,'airFlowOA':25,'coRA':30}
database.insertNewRow(tablename, setpointrow)

value =database.queryTable('Devices','name')
print value
valuetwo =database.queryTable('Setpoints','id')
print valuetwo
