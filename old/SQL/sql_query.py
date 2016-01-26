from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sqlite3
from sqlalchemy_declarative import Base, Devices
 
def row2dict(row):
    d = {}
    for column in row.__table__.columns:
        d[column.name] = str(getattr(row, column.name))
    return d

def list2dict(list):
	d = {}
	for i in range(0, len(list)):
		key = list[i][0]
		d[key]= list[i]
	return d

def queryRow(tableName):
	#SQL alchemy process for creating the engine and session to query the database
	#insert table name as a variable not a string
	engine = create_engine('sqlite:///rh.db')
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	#Functions assume that the desired output is the last value inputed into the database, arragned by auto-incrementing id
	databaseRow = session.query(tableName).order_by(tableName.id.desc()).first()
	#return databaseRow
	#query is then converted into a dictionary in which the database's column name is the key and the value is value.
	dict = row2dict(databaseRow)
	return dict

def queryTable(tableName):
	#Requires table name as a string because it works using SQLite3. Method will return a dictionary of the entire table.
	#The keys are the unique ID,but can be changed via the list2dict function.(line 15)
	db = sqlite3.connect('rh.db')
	cursor = db.cursor()
	cursor.execute("SELECT * FROM "+tableName)
	fetchedValue = cursor.fetchall()
	print fetchedValue
	tableDictionary = list2dict(fetchedValue)
	return tableDictionary



def queryValue(tableName,columnName):
	#Note: all inputs must be entered in as string. This comes from the fact that it was done through
	#SQLite3 instead of SQL_alchemy
	db = sqlite3.connect('rh.db')
	cursor = db.cursor()
	cursor.execute("SELECT " +columnName+ " FROM "+tableName+" ORDER BY id DESC")
	fetchedValue = cursor.fetchone()
	return fetchedValue
	db.close()

def queryValueSpecific(tableName,columnName,indicator,indicatorValue):
	#Note: all inputs must be entered in as string. This comes from the fact that it was done through
	#SQLite3 instead of SQL_alchemy
	db = sqlite3.connect('rh.db')
	cursor = db.cursor()
	cursor.execute("SELECT " +columnName+ " FROM "+tableName+" WHERE "+indicator+" = "+indicatorValue)
	fetchedValue = cursor.fetchone()
	return fetchedValue
	db.close()

