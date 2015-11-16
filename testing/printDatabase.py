import sys
sys.path.insert(0, '../database/database')
from sql_query import queryTable

print "Controller One:"
queryResult = queryTable("controllerone", 'timestamp', 'sqlite:///../database/database/rh.db')
print queryResult
print "\nController Two:"
queryResult = queryTable("controllertwo", 'timestamp', 'sqlite:///../database/database/rh.db')
print queryResult