
import os
#os.path.abspath(os.path.dirname(__file__))

import json

with open('config.json') as data_file:
    data_json = json.loads(data_file.read())


class config(object):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True
	DB = ('%s://%s:%s@%s:%s/%s' % (data_json['db']['db_engine'],data_json['db']['db_id'],data_json['db']['db_password'],data_json['db']['db_host'],data_json['db']['db_port'],data_json['db']['db_name']))

        def Production(self):
        	self.DEBUG = False
        	SECRET_KEY = data_json['secret_key']
        	CRYPT_LEVEL = 12

        def Development(self):
        	DEVELOPMENT = True
        	self.DEBUG = True
        	SECRET_KEY = data_json['secret_key']
        	CRYPT_LEVEL = 12

        def Testing(self):
        	self.TESTING = True
        	SECRET_KEY = data_json['secret_key']
        	CRYPT_LEVEL = 12

SQLALCHEMY_DATABASE_URI = config.DB
