from sqlalchemy import create_engine, insert,update
from sqlalchemy.orm import sessionmaker
from sql_query import queryRow
 
from sqlalchemy_declarative import Base, Devices
 
#Functions takes the the table name(i.e. the class found in sql_declarative) and a dictionary to insert all of the values into the database
def insertNewRow(table, TheDict):
	engine = create_engine('sqlite:///rh.db')
	# Bind the engine to the metadata of the Base class so that the
	# declaratives can be accessed through a DBSession instance
	Base.metadata.bind = engine
	DBSession = sessionmaker(bind=engine)
	# A DBSession() instance establishes all conversations with the database
	# and represents a "staging zone" for all the objects loaded into the
	# database session object. Any change made against the objects in the
	# session won't be persisted into the database until you call
	# session.commit(). If you're not happy about the changes, you can
	# revert all of them back to the last commit by calling
	# session.rollback()
	session = DBSession()
	l = insert(table)
	l = l.values(TheDict)
	session.execute(l)
	session.commit()

