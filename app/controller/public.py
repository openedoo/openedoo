
from flask import Blueprint, render_template
import json
from flask import abort, Flask, g, request, Response
from app.model.auth import requires_auth
from app.model.tools import randomword,hashingpw,cocokpw,setredis,getredis

public = Blueprint('newbot_public', __name__)
@public.route('/', methods = ['POST','GET'])
def newbot():
	a = request.headers.get('User-Agent')
	token =  request.headers.get('token')
	if "grupi" not in str(a):# and "google" not in str(a):
		abort(403)
	elif token is None:
		abort(401)
	if request.method == 'POST':
		try:			
			data = getredis(token)
			cocok = cocokpw(token,data)
			if cocok == True:
				output = {'status':202,'response':{'message':'data diterima'}}
				resp = Response(json.dumps(output), status=202, mimetype='application/json')
				return resp
			else:
				output = {'status':202,'response':{'message':'data ditolak'}}
				resp = Response(json.dumps(output), status=202, mimetype='application/json')
				return resp
		except Exception:
			abort(204)
	print token
	acak = randomword(32)
	hashpw = hashingpw(acak)
	payload = {'status':200,'response':{'message':'data diterima','public_key':acak}}
	output = json.dumps(payload)
	setredis(acak,hashpw,120)
	resp = Response(output, status=200, mimetype='application/json')
	return resp
