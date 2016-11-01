
from flask import Blueprint, render_template, abort, Response
import json
from app.model.tools import getredis
blink = Blueprint('newbot_blink', __name__)
@blink.route('/')
def newbot():
	data = getredis("blink")
	output = {'status':200,'response':data}
	if data == False:
		abort(50)
	resp = Response(json.dumps(output), status=200, mimetype='application/json')
	return resp
