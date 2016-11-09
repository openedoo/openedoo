from app.core.libs import blueprint,response,redirect,request
#from flask import Blueprint
testing = blueprint('newbot_', __name__)

import json


@testing.route('/')
def newbot():
	return redirect("http://google.com", code=302)

@testing.route('/bac')
def newbot2():
	return "rendi"

