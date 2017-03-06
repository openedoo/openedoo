import os
import json
from openedoo import app

DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
file_config = os.path.join(DIR, 'config.json.example')

try:
	with open('config.json') as data_file:
		data_json = json.loads(data_file.read())
except Exception as e:
	try:
		print "please replace config.json.example with your configuration to config.json"
		with open(file_config) as data_file:
			data_json = json.loads(data_file.read())
	except:
		data_json = {"db":{"db_engine": "mysql","db_id": "your_username","db_password" : "your_password","db_host" : "localhost","db_port" : "3306","db_name" : "db_openedoo","db_prefix" : "openedoo"},"config": "Development","secret_key" : "aksaramaya_openedoo"}



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
