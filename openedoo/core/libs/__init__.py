from flask import render_template, redirect, request, session, Blueprint
from flask import Flask
from flask import g
from flask import Response
from flask import request

def blueprint(name,init):
	blueprint = Blueprint(name,init)
	return blueprint

response = Response
request = request
redirect = redirect