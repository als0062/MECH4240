
import sqlite3
conn = sqlite3.connect('rh.db')
c = conn.cursor()
c.execute('''
          CREATE TABLE IF NOT EXISTS devices
          (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(250) NOT NULL, ini VARCHAR(250) NOT NULL,
          ip VARCHAR(250) NOT NULL, mac VARCHAR(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS errors
          (id INTEGER PRIMARY KEY AUTOINCREMENT, type INTEGER NOT NULL, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
          priority INTEGER, location VARCHAR(250), device VARCHAR(250) NOT NULL)
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS maintenance
          (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
          dueDate DATE NOT NULL, priority INTEGER, description VARCHAR(250))
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS airHandlerOne
          (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, tempOA INTEGER, tempRA INTEGER,
          tempMA INTEGER, tempPA INTEGER, tempSA INTEGER, humidityOA INTEGER, humidityRA INTEGER, humiditySA INTEGER, 
          airFlowOA INTEGER, airFlowRA INTEGER, airFlowREA INTEGER, airFlowSA INTEGER, filterPDrop INTEGER, coolingCoilPDrop INTEGER,
          heatingCoilPDrop INTEGER, coOA INTEGER, coRA INTEGER, coMA INTEGER,coSA INTEGER, fanVoltage INTEGER, fanAmperage INTEGER, 
          fanPower INTEGER, fanPowerUsage INTEGER, fanStatus BOOLEAN, chilledWaterST INTEGER, chilledWaterRT INTEGER, 
          chilledWaterTDrop INTEGER, chilledWaterSP INTEGER, chilledWaterRP INTEGER, chilledWaterPDrop INTEGER, chilledWaterFlow INTEGER, 
          heatedWaterST INTEGER, heatedWaterRT INTEGER, heatedWaterTDrop INTEGER, heatedWaterSP INTEGER, heatedWaterRP INTEGER, 
          heatedaterPDrop INTEGER, heatedWaterFlow INTEGER, damperPositionOA INTEGER, damperPositionRA INTEGER, damperPositionRE INTEGER, 
          valuePositionCW INTEGER, valuePositionHW INTEGER, valuePositionHumidifier INTEGER, fanSpeedFrequency INTEGER,
          fanSpeedOutput INTEGER, fanSPeedEnergieze BOOLEAN)
          ''')
c.execute('''
          CREATE TABLE IF NOT EXISTS setpoints
          (id INTEGER PRIMARY KEY AUTOINCREMENT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, tempOA INTEGER, tempRA INTEGER,
          tempMA INTEGER, tempPA INTEGER, tempSA INTEGER, humidityOA INTEGER, humidityRA INTEGER, humiditySA INTEGER, 
          airFlowOA INTEGER, airFlowRA INTEGER, airFlowREA INTEGER, airFlowSA INTEGER, filterPDrop INTEGER, coolingCoilPDrop INTEGER,
          heatingCoilPDrop INTEGER, coOA INTEGER, coRA INTEGER, coMA INTEGER,coSA INTEGER, fanVoltage INTEGER, fanAmperage INTEGER, 
          fanPower INTEGER, fanPowerUsage INTEGER, fanStatus BOOLEAN, chilledWaterST INTEGER, chilledWaterRT INTEGER, chilledWaterTDrop INTEGER, 
          chilledWaterSP INTEGER, chilledWaterRP INTEGER, chilledWaterPDrop INTEGER, chilledWaterFlow INTEGER, heatedWaterST INTEGER, 
          heatedWaterRT INTEGER, heatedWaterTDrop INTEGER, heatedWaterSP INTEGER, heatedWaterRP INTEGER, heatedaterPDrop INTEGER, 
          heatedWaterFlow INTEGER)
          ''')

c.execute('''
          INSERT INTO devices 
          VALUES (NULL,'Air Handler One','Controler01.ini','192.168.92.68','00-14-22-01-23-45')
          ''')
c.execute('''
          INSERT INTO devices 
          VALUES (NULL,'Air Handler Two','Controler02.ini','192.168.92.65','00-14-22-01-23-45')
          ''')
#possible method for airHandlerOne
#INSERT INTO Customers (CustomerName, ContactName, Address, City, PostalCode, Country)
#VALUES ('Cardinal','Tom B. Erichsen','Skagen 21','Stavanger','4006','Norway')
conn.commit()
conn.close()
