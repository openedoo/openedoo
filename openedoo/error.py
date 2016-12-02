
from core.libs import response
from openedoo.core.libs import abort
from openedoo import app
import json


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
