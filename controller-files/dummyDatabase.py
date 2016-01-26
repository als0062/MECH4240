import sys
sys.path.insert(0, '../database/database')
from sql_insert import insertNewRow
from sql_declarative import databaseCreation
from sql_query import queryTable

import os
dbfilepath = '../database/database/rh.db'
## if file exists, delete it ##
if os.path.isfile(dbfilepath) is True:
    os.remove(dbfilepath)
    print 'Old file removed.'
else:
	print 'No existing file found.'

databaseCreation()
table = 'devices'
rowOne = {'name':'ControllerOne','ini':'ControllerOne.ini','ip':'192.168.92.69','mac':'macAddressOne'}
rowTwo = {'name':'ControllerTwo','ini':'ControllerTwo.ini','ip':'192.178.92.79','mac':'macAddressTwo'}

insertNewRow(table, rowOne, 'sqlite:///../database/database/rh.db')
insertNewRow(table, rowTwo, 'sqlite:///../database/database/rh.db')
print 'New file created.'

tablename = 'setpoints'
setpointrow = {'tempSA':70,'tempMA':72,'tempPA':73,'tempSA':75,'humidityRA':20,'airFlowOA':25,'coRA':30}
insertNewRow(tablename, setpointrow,'sqlite:///../database/database/rh.db')

# print queryTable(table,'ip','sqlite:///../database/database/rh.db')



