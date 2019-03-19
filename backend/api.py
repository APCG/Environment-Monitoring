import flask
import numpy as np

from flask_cors import CORS, cross_origin

from flask import request, jsonify
import mysql.connector

db = mysql.connector.connect(host="sydrv.myqnapcloud.com", user="office", passwd="ShipIt2019", database="mysql")
mycursor = db.cursor()
mycursor.execute("SELECT * FROM Office_Environment_Dummy")
  
app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'the quick brown fox jumps over the lazy   dog'
app.config['CORS_HEADERS'] = 'Content-Type'

CORS(app, resources={r"/dummy": {"origins": "http://localhost:5000"}})
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
	return "Hey Mate"

@app.route('/dummy', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def dummy():
	result = []
	rows = np.ones((4, 5))
	for row in rows:
		result.append(
			{"CO2": row[0],
			 "Temperature": row[1],
			 "Microphone": row[2],
			 "Humidity": row[3],
			 "Light": row[4]})

	result = jsonify(result)
	return result

app.run()
