from createDeviceChain import createChain 
from sql_query import queryValue
import time, os, numpy, subprocess

tablename = "controllerone"
columnname = "tempOA"
path = 'sqlite:///../database/database/rh.db'

value = queryValue(tablename,columnname,path)
print(value)
