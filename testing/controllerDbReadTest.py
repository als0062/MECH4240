import sys
sys.path.insert(0, '../database/database')
from sql_declarative import databaseCreation
from sql_insert import insertNewRow
from sql_query import queryRowSpecific, queryColumn, queryRow, queryTable, queryValue, queryValueSpecific


print databaseCreation()
table = 'Devices'
rowOne = {'name':'Hello!','ini':'ControllerOne.ini','ip':'192.168.92.69','mac':'macAddressOne'}
rowTwo = {'name':'ControllerTwo','ini':'ControllerTwo.ini','ip':'192.168.92.70','mac':'macAddressTwo'}
rowThree = {'name':'ControllerThree','ini':'ControllerThree.ini','ip':'192.168.92.71','mac':'macAddressThree'}
rowFour = {'name':'ControllerFour','ini':'ControllerFour.ini','ip':'192.168.92.72','mac':'macAddressFour'}

insertNewRow(table, rowOne)
insertNewRow(table, rowTwo)
insertNewRow(table, rowThree)
insertNewRow(table, rowFour)

tablename = 'Setpoints'
setpointrow = {'tempSA':10000,'tempMA':72,'tempPA':73,'tempSA':75,'humidityRA':20,'airFlowOA':25,'coRA':30}
insertNewRow(tablename, setpointrow)

value =queryTable('Devices','name')
print value
valuetwo = queryTable('Setpoints','id')
print valuetwo
