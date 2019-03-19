import flask
import numpy as np

from flask_cors import CORS, cross_origin

from flask import request, jsonify
import mysql.connector

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
	db = mysql.connector.connect(host="sydrv.myqnapcloud.com", user="office", passwd="ShipIt2019", database="mysql")
	mycursor = db.cursor()

	mycursor.execute("SELECT * FROM Office_Environment")
	result = []
	# rows = np.ones((4, 5))
	for row in mycursor.fetchall():
		result.append(
			{"CO2": float(row[3]),
			 "Temperature": float(row[1]),
			 "Microphone": float(row[4]),
			 "Humidity": float(row[2]),
			 "Light": float(row[5])})

	result = jsonify(result)
	mycursor.close()
	return result

@app.route('/historic', methods=['GET'])
@cross_origin(origin='localhost', headers=['Content- Type', 'Authorization'])
def historic():
	db = mysql.connector.connect(host="sydrv.myqnapcloud.com", user="office", passwd="ShipIt2019", database="mysql")
	mycursor = db.cursor()

	mycursor.execute("SELECT * FROM Office_Environment_Historic ORDER BY Pimary_ID DESC")

	# rows = np.ones((4, 5))
	result = []
	idx = 0
	for idx, row in enumerate(mycursor.fetchall()):
		result.append(
			{"CO2": float(row[5]),
			 "Temperature": float(row[3]),
			 "Time": str(row[2].time())[:5]})

	result.insert(0, {"length": idx + 1})
	result = jsonify(result)
	mycursor.close()
	return result


if __name__ == "__main__":
	app.run()
