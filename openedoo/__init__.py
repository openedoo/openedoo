from core.libs import response
from flask import Flask,abort
import json
import config
app = Flask(__name__)

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

from .hello import hello
app.register_blueprint(hello, url_prefix='/hello')


@app.errorhandler(400)
def page_not_found(e):
	error = { 'status' : 'bad requests' }
	error = json.dumps(error)
	resp = response(error, status=400, mimetype='application/json')
	return resp
@app.errorhandler(401)
def page_not_found(e):
	error = { 'status' : 'bad password or username' }
	error = json.dumps(error)
	resp = response(error, status=401, mimetype='application/json')
	return resp
@app.errorhandler(403)
def page_not_found(e):
	error = { 'status' : 'forbidden to access' }
	error = json.dumps(error)
	resp = response(error, status=403, mimetype='application/json')
	return resp
@app.errorhandler(404)
def page_not_found(e):
	error = { 'status' : 'page not found' }
	error = json.dumps(error)
	resp = response(error, status=404, mimetype='application/json')
	return resp
@app.errorhandler(405)
def page_not_found(e):
	error = { 'status' : 'methods not allowed' }
	error = json.dumps(error)
	resp = response(error, status=405, mimetype='application/json')
	return resp
@app.errorhandler(500)
def page_not_found(e):
	error = { 'status' : 'bad requests' }
	error = json.dumps(error)
	resp = response(error, status=500, mimetype='application/json')
	return resp
