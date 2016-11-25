from flask import Flask,abort
import json
import config
from datetime import timedelta
app = Flask(__name__)

app.permanent_session_lifetime = timedelta(minutes=10)

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

import route
import error
