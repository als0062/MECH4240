from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sql_declarative import Base, devices, errors, maintenance, controllerone,controllertwo, setpoints

def row2dict(row):
    d = {}
    for column in row.__table__.columns:
    	if str(getattr(row, column.name)) != 'None':
        	d[column.name] = str(getattr(row, column.name))
    return d

def list2dict(list):
	d = {}
	for i in range(0, len(list)):
		key = list[i][0]
		d[key]= list[i]
	return d

def queryRow(tableName, path):
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
	elif tableName == "errors":
		table = errors
	elif tableName == "maintenance":
		table = maintenance
	elif tableName == "controllerone":
		table = controllerone
	elif tableName == "controllertwo":
		table = controllertwo
	elif tableName == "setpoints":
		table = setpoints
	#SQL alchemy process for creating the engine and session to query the database
	#insert table name as a variable not a string
	#engine = create_engine('sqlite:///../database/database/rh.db')
	engine = create_engine(path)
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	#Functions assume that the desired output is the last value inputed into the database, arragned by auto-incrementing id
	databaseRow = session.query(table).order_by(table.id.desc()).first()
	#return databaseRow
	#query is then converted into a dictionary in which the database's column name is the key and the value is value.
	dict = row2dict(databaseRow)
	return dict

def queryRowSpecific(tableName,key,columnName):
	#Using the queryTable function to get a dictionary of the entire table with the key as the names. 
	#Function then returns a single row's dictionary based usign the given key
	table = queryTable(tableName,key)
	value = table[columnName]
	return value

def queryColumn(tableName,columnName, path):
	#SQL alchemy process for creating the engine and session to query the database
	#insert table name as a variable not a string, while the column name must be entered in as a string
	#column name is then converted from a string using the get attribute command
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
	elif tableName == "errors":
		table = errors
	elif tableName == "maintenance":
		table = maintenance
	elif tableName == "controllerone":
		table = controllerone
	elif tableName == "controllertwo":
		table = controllertwo
	elif tableName == "setpoints":
		table = setpoints
	#engine = create_engine('sqlite:///../database/database/rh.db')
	engine = create_engine(path)
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	list = []
	varableSelect = getattr(table,columnName)
	for value in session.query(varableSelect):
		 list.append(value[0])
	return list
	#appending line calls out the zeroth spot in a list to only place only the desired string into the list 


def queryTable(tableName, key, path):
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
	elif tableName == "errors":
		table = errors
	elif tableName == "maintenance":
		table = maintenance
	elif tableName == "controllerone":
		table = controllerone
	elif tableName == "controllertwo":
		table = controllertwo
	elif tableName == "setpoints":
		table = setpoints
	#Method takes the take name to query and returns a dictionary composed of a dictionary that contain all of the row information.
	#The dicitionary that contains the row information uses the column name as the key, while the returned dictionary uses
	#the unique ID as the key
	#engine = create_engine('sqlite:///rh.db')
	#engine = create_engine('sqlite:///../database/database/rh.db')
	engine = create_engine(path)

	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	dict = {}
	#Functions assume that the desired output is the last value inputed into the database, arragned by auto-incrementing id
	for row in session.query(table):
		innerDict = row2dict(row)
		dict[innerDict[key]]= innerDict
	return dict


def queryValue(tableName,columnName, path):
	#Method uses SQLalchemy to return a single value. The value is determined by the columnName and is found on the last row.
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
	elif tableName == "errors":
		table = errors
	elif tableName == "maintenance":
		table = maintenance
	elif tableName == "controllerone":
		table = controllerone
	elif tableName == "controllertwo":
		table = controllertwo
	elif tableName == "setpoints":
		table = setpoints
	#engine = create_engine('sqlite:///../database/database/rh.db')
	engine = create_engine(path)
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	varableSelect = getattr(table,columnName)
	value  = session.query(varableSelect).order_by(table.id.desc()).first()
	return value[0]

def queryValueSpecific(tableName,columnName,rowName,rowValue, path):
	#Method uses SQLalchemy to return a single value. The value is determined by the columnName the row is 
	#determined where the given row value is found and the given row.
	if tableName == "devices":
		table = devices
	elif tableName == "base":
		table = base
	elif tableName == "errors":
		table = errors
	elif tableName == "maintenance":
		table = maintenance
	elif tableName == "controllerone":
		table = controllerone
	elif tableName == "controllertwo":
		table = controllertwo
	elif tableName == "setpoints":
		table = setpoints
	#engine = create_engine('sqlite:///../database/database/rh.db')
	engine = create_engine(path)
	Base.metadata.bind = engine
	DBSession = sessionmaker()
	DBSession.bind = enginesession = DBSession()
	session = DBSession()
	varableSelect = getattr(table,columnName)
	indication = getattr(table,rowName)
	value  = session.query(varableSelect).filter(indication == rowValue)
	return value[0][0]
