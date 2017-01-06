#from flask import Flask,abort
from openedoo.core.libs import *
import json
import config
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=10)
#db = SQLAlchemy(app)

try:
	with open('config.json') as data_file:
		data_json = json.loads(data_file.read())

	if data_json['config']=="Development":
		app.config.from_object(config.Development)
	elif data_json['config']=="Production":
		app.config.from_object(config.Production)
	elif data_json['config']=="Testing":
		app.config.from_object(config.Testing)
	else:
		app.config.from_object(config.Development)

	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db = SQLAlchemy(app)
	from openedoo import tables


except Exception as e:
	#print e
	app.config.from_object(config.Development)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db = SQLAlchemy(app)
	from openedoo import tables


import route
import error