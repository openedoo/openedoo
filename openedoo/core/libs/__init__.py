from flask import render_template, redirect, request, session, Blueprint
from flask import Flask
from flask import g
from flask import Response
from flask import abort

def blueprint(name,init,template_folder=None):
	if template_folder==None:
		blueprint = Blueprint(name,init)
	else:
		blueprint = Blueprint(name,init,template_folder)
	return blueprint

response = Response
request = request
redirect = redirect
abort = abort
render_template = render_template
session = session
