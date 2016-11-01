from flask import render_template, redirect, url_for, request, session
from flask import Flask
from flask import g
from flask import Response
from flask import request
import json


app = Flask(__name__)

app.config.from_pyfile('config.py')

from app.controller.view import view
app.register_blueprint(view, url_prefix='/')

from app.controller.api import api
app.register_blueprint(api, url_prefix='/api')
app.register_blueprint(api, url_prefix='/api/gpio')

from app.controller.device import device
app.register_blueprint(device, url_prefix='/device')

from app.controller.member import member
app.register_blueprint(member, url_prefix='/member')

from app.controller.public import public
app.register_blueprint(public, url_prefix='/public')



@app.errorhandler(404)
def page_not_found(e):
	error = { 'status' : 'page not found' }
	error = json.dumps(error)
	resp = Response(error, status=404, mimetype='application/json')
	return resp
@app.errorhandler(401)
def page_not_found(e):
	error = { 'status' : 'bad password or username' }
	error = json.dumps(error)
	resp = Response(error, status=401, mimetype='application/json')
	return resp
@app.errorhandler(400)
def page_not_found(e):
	error = { 'status' : 'bad requests' }
	error = json.dumps(error)
	resp = Response(error, status=400, mimetype='application/json')
	return resp

@app.errorhandler(500)
def page_not_found(e):
	error = { 'status' : 'bad requests' }
	error = json.dumps(error)
	resp = Response(error, status=500, mimetype='application/json')
	return resp
@app.errorhandler(403)
def page_not_found(e):
	error = { 'status' : 'forbidden to access' }
	error = json.dumps(error)
	resp = Response(error, status=403, mimetype='application/json')
	return resp


from app.controller.blink import blink
app.register_blueprint(blink, url_prefix='/blink')
