import os
import json

try:
	with open('config.json') as data_file:
		data_json = json.loads(data_file.read())
except Exception as e:
	print "please replace config.json.example with your configuration to config.json"
	with open('config.json.example') as data_file:
		data_json = json.loads(data_file.read())

class config(object):
	DEBUG = True
	TESTING = False
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	CSRF_ENABLED = True
	SQLALCHEMY_DATABASE_URI = ('{engine}://{username}:{password}@{host}:{port}/{db_name}'.format(\
		engine=data_json['db']['db_engine'],\
		username=data_json['db']['db_id'],\
		password=data_json['db']['db_password'],\
		host=data_json['db']['db_host'],\
		port=data_json['db']['db_port'],\
		db_name=data_json['db']['db_name']))

class Production(config):
	DEBUG = False
	SECRET_KEY = data_json['secret_key']

class Development(config):
	DEVELOPMENT = True
	DEBUG = True
	SECRET_KEY = data_json['secret_key']

class Testing(config):
	TESTING = True
	SECRET_KEY = data_json['secret_key']

DB_URI = ('{engine}://{username}:{password}@{host}:{port}'.format(\
		engine=data_json['db']['db_engine'],\
		username=data_json['db']['db_id'],\
		password=data_json['db']['db_password'],\
		host=data_json['db']['db_host'],\
		port=data_json['db']['db_port'],))
SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
database_name = data_json['db']['db_name']
database_prefix = data_json['db']['db_prefix']