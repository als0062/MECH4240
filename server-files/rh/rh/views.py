#Add database-files to our path
import sys
sys.path.insert(0, '../../database/database')

#flask imports
from rh import app
import os
from flask import jsonify, render_template, redirect, url_for, request, flash

#python modules
import ConfigParser

#Our Modules
from sql_query import queryTable
from sql_insert import insertNewRow
from sql_declarative import databaseCreation
#import sql_declarative

#---------------------Sample Data-----------------------
#alerts 0-Completed, 1-Warning, 2-Critical
alerts = [
	{
		'id': 1,
		'type': 2,
		'date': u'Thursday 4-11-2014 at 7:44:57 PM',
		'description': u'Outside air damper error at AUH-ER1',
		'done': False
	},
	{
		'id': 2,
		'type': 1,
		'date': u'Friday 4-10-2014 at 2:40:53 PM',
		'description': u'High humidity at AUH-ER1',
		'done': False
	}
]
#Maintenance
maintenance = [
	{
		'id': 1,
		'target': u'Fire Extinguisher',
		'date': u'8-19-2014',
		'countdown': 74
	}
]

@app.route('/')
def index():
	return redirect(url_for('return_overview'))

@app.route('/rh/api/v1.0/alerts', methods = ['GET'])
def return_alerts():
	#Authenticate
	#populate alerts
	return render_template("alerts.html")

@app.route('/rh/api/v1.0/contact', methods = ['GET'])
def return_contact():
	#populate contact info
	return render_template("contact.html")

@app.route('/rh/api/v1.0/equipment', methods = ['GET'])
def return_equipment():
	#authenticate
	#populate equipment
	#devices = queryTable("Devices")
	return render_template("equipment.html")

@app.route('/rh/api/v1.0/equipment/all', methods = ['GET'])
def return_equipment_list():
	queryResult = queryTable("devices", 'name', 'sqlite:///../../database/database/rh.db')
	#print queryResult["ControllerThree"]
	return jsonify(queryResult)

@app.route('/rh/api/v1.0/equipment/<string:controller_id>', methods = ['GET'])
def return_trend_data(controller_id):
	print controller_id
	queryResult = queryTable(controller_id, 'timestamp', 'sqlite:///../../database/database/rh.db')
	return jsonify(queryResult)

@app.route('/rh/api/v1.0/equipment/ini', methods = ['POST'])
def create_ini():
	config = ConfigParser.ConfigParser()
	config['BACpypes'] = {"objectName" : "ControllerOne",
						"address" : "192.168.92.69",
						"objectIdentifier" : "2451",
						"maxApduLengthAccepted" : "1024",
						"segmentationSupported" : "segmentedBoth",
						"vendorIdentifier" : "245",
						"foreignPort" : "0",
						"foreignBBMD" : "0.0.0.0",
						"foreignTTL" : "30",
						}
	config['Ports'] = {"portOne" : "LED", "portTwo" : "ThermistorCC", "portThree" : "LED"}
	with open('example.ini', 'w') as configfile:
		config.write(configfile)

@app.route('/rh/api/v1.0/login', methods = ['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		flash('login')
		return redirect(url_for('return_overview'))

	return render_template('login.html', error = error)

@app.route('/rh/api/v1.0/logout')
def logout():
	return 'logout'

@app.route('/rh/api/v1.0/maintenance', methods = ['GET'])
def return_maintenance():
	#authenticate
	#populate scheduled maintenance
	return jsonify( {'maintenance': maintenance} )

@app.route('/rh/api/v1.0/overview', methods = ['GET'])
def return_overview():
	#authenticate
	#populate summary reports
	#populate scheduled maintenance
	#populate recent alerts
	return render_template("index.html")
