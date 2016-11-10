import os
basedir = os.path.abspath(os.path.dirname(__file__))

import json

with open(os.path.join(basedir, 'config.json')) as data_file:
    data_json = json.loads(data_file.read())


class config(object):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True
	DB = ('%s://%s:%s@%s:%s/%s' % (data_json['db']['db_engine'],data_json['db']['db_id'],data_json['db']['db_password'],data_json['db']['db_host'],data_json['db']['db_port'],data_json['db']['db_name']))

        def production(self):
            DEBUG = False
            SECRET_KEY = data_json['secret_key']
            CRYPT_LEVEL = 12

        def Development(self):
        	DEVELOPMENT = True
        	DEBUG = True
        	SECRET_KEY = data_json['secret_key']
        	CRYPT_LEVEL = 12

        def Testing(self):
        	TESTING = True
        	SECRET_KEY = data_json['secret_key']
        	CRYPT_LEVEL = 12

SQLALCHEMY_DATABASE_URI = config.DB
