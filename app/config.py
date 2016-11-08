import os
basedir = os.path.abspath(os.path.dirname(__file__))


class config(object):
	DEBUG = True
	TESTING = False
	CSRF_ENABLED = True
	SECRET_KEY = 'this-really-needs-to-be-changed'


class ProductionConfig(config):
	DEBUG = False


class StagingConfig(config):
	DEVELOPMENT = True
	DEBUG = True


class DevelopmentConfig(config):
	DEVELOPMENT = True
	DEBUG = True


class TestingConfig(config):
	TESTING = True

