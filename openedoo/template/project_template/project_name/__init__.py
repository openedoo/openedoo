import json
import config
from datetime import timedelta
from flask import Flask

app = Flask(__name__)

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
    app.config.from_object(config.Development)
	app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
	db = SQLAlchemy(app)

    from .%(project_name)s import tables

from .%(project_name)s import route
from .%(project_name)s import error
