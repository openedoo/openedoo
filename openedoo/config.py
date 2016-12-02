import os
import json

try:
	with open('config.json') as data_file:
		data_json = json.loads(data_file.read())
except Exception as e:
	data_json = {
    "db":
        {
            "db_engine": "mysql",
            "db_id": "db_id",
            "db_password" : "password",
            "db_host" : "localhost",
            "db_port" : "3306",
            "db_name" : "db_openedoo"
        },
    "config": "Development",
    "secret_key" : "aksaramaya_openedoo"
}

class config(object):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True
	SQLALCHEMY_DATABASE_URI = ('%s://%s:%s@%s:%s/%s' % (data_json['db']['db_engine'],data_json['db']['db_id'],data_json['db']['db_password'],data_json['db']['db_host'],data_json['db']['db_port'],data_json['db']['db_name']))

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


SQLALCHEMY_DATABASE_URI = config.SQLALCHEMY_DATABASE_URI
