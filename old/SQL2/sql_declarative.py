import os
import sys
import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()

class Devices(Base):
	__tablename__ = 'devices'
	id = Column(Integer, primary_key=True)
	name = Column(String(250), nullable=False)
	ini = Column(String(250), nullable=False)
	ip = Column(String(250), nullable=False)
	mac = Column(String(250), nullable=False)
	
	# def __init__(self, name=None, ini=None, ip=None, mac=None):
 #        self.name = name
 #        self.ini = ini
 #        self.ip = ip
 #        self.mac = mac
class Errors(Base):
	__tablename__= 'errors'
	id = Column(Integer, primary_key=True)
	type = Column(String(250), nullable=False)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)
	priority = Column(Integer)
	location = Column(String(250))
	device = Column(String(250), nullable=False)

class Maintenance(Base):
	__tablename__ = 'maintenance'
	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)
	dueDate = Column(Date, nullable=False)
	priority = Column(Integer)
	description = Column(String(250), nullable=False)

class AirHandlerOne(Base):
	__tablename__ = 'airhandlerOne'
	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)
	tempOA = Column(Integer)
	tempRA = Column(Integer)
	tempMA = Column(Integer)
	tempPA = Column(Integer)
	tempSA = Column(Integer)
	humidityOA = Column(Integer)
	humidityRA = Column(Integer)
	humiditySA = Column(Integer)
	airFlowOA = Column(Integer)
	airFlowRA = Column(Integer)
	airFlowREA = Column(Integer)
	airFlowSA = Column(Integer)
	filterPDrop = Column(Integer)
	coolingCoilPDrop = Column(Integer)
	heatingCoilPDrop = Column(Integer)
	coOA = Column(Integer)
	coRA = Column(Integer)
	coMA = Column(Integer)
	coSA = Column(Integer)
	fanVoltage = Column(Integer)
	fanAmperage = Column(Integer)
	fanPower = Column(Integer)
	fanPowerUsage = Column(Integer)
	fanStatus = Column(Boolean)
	chilledWaterST = Column(Integer)
	chilledWaterRT = Column(Integer)
	chilledWaterTDrop = Column(Integer)
	chilledWaterSP = Column(Integer)
	chilledWaterRP = Column(Integer)
	chilledWaterPDrop = Column(Integer)
	chilledWaterFlow = Column(Integer)
	heatedWaterST = Column(Integer)
	heatedWaterRT = Column(Integer)
	heatedWaterTDrop = Column(Integer)
	heatedWaterSP = Column(Integer)
	heatedWaterRP = Column(Integer)
	heatedaterPDrop = Column(Integer)
	heatedWaterFlow = Column(Integer)
	damperPositionOA = Column(Integer)
	damperPositionRA = Column(Integer)
	damperPositionRE = Column(Integer)
	valuePositionCW = Column(Integer)
	valuePositionHW = Column(Integer)
	valuePositionHumidifier = Column(Integer)
	fanSpeedFrequency = Column(Integer)
	fanSpeedOutput = Column(Integer)
	fanSPeedEnergieze = Column(Boolean)

class Setpoints(Base):
	__tablename__ = 'setpoint'
	id = Column(Integer, primary_key=True)
	timestamp = Column(DateTime, default=datetime.datetime.utcnow)
	tempOA = Column(Integer)
	tempRA = Column(Integer)
	tempMA = Column(Integer)
	tempPA = Column(Integer)
	tempSA = Column(Integer)
	humidityOA = Column(Integer)
	humidityRA = Column(Integer)
	humiditySA = Column(Integer)
	airFlowOA = Column(Integer)
	airFlowRA = Column(Integer)
	airFlowREA = Column(Integer)
	airFlowSA = Column(Integer)
	filterPDrop = Column(Integer)
	coolingCoilPDrop = Column(Integer)
	heatingCoilPDrop = Column(Integer)
	coOA = Column(Integer)
	coRA = Column(Integer)
	coMA = Column(Integer)
	coSA = Column(Integer)
	fanVoltage = Column(Integer)
	fanAmperage = Column(Integer)
	fanPower = Column(Integer)
	fanPowerUsage = Column(Integer)
	fanStatus = Column(Boolean)
	chilledWaterST = Column(Integer)
	chilledWaterRT = Column(Integer)
	chilledWaterTDrop = Column(Integer)
	chilledWaterSP = Column(Integer)
	chilledWaterRP = Column(Integer)
	chilledWaterPDrop = Column(Integer)
	chilledWaterFlow = Column(Integer)
	heatedWaterST = Column(Integer)
	heatedWaterRT = Column(Integer)
	heatedWaterTDrop = Column(Integer)
	heatedWaterSP = Column(Integer)
	heatedWaterRP = Column(Integer)
	heatedaterPDrop = Column(Integer)
	heatedWaterFlow = Column(Integer)



# Create an engine that stores data in the local directory's
# sqlalchemy_example.db file.
engine = create_engine('sqlite:///rh.db')
 
# Create all tables in the engine. This is equivalent to "Create Table"
# statements in raw SQL.
Base.metadata.create_all(engine)

