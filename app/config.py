import os
basedir = os.path.abspath(os.path.dirname(__file__))

import json

with open('app/config.json') as data_file:
    data_json = json.loads(data_file.read())


class config(object):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True	
	DB = ('%s://%s:%s@%s:%s/%s' % (data_json['db']['db_engine'],data_json['db']['db_id'],data_json['db']['db_password'],data_json['db']['db_host'],data_json['db']['db_port'],data_json['db']['db_name']))

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
