from flask import Blueprint, render_template
api = Blueprint('newbot', __name__)

from app.model.db.ormdua import selectdb,device
import json
from flask import jsonify, abort, Flask, g, request, Response
from app.model.auth import requires_auth

def decryptsl(key, encryped):
	msg = []
	for i, c in enumerate(encryped):
		key_c = ord(key[i % len(key)])
		enc_c = ord(c)
		msg.append(chr((enc_c - key_c) % 127))
	return ''.join(msg)
'''
@api.route('/', methods = ['POST','GET'])
@requires_auth
def getsensor():
	panggildb = koneksidb(device,device.user_id,nilai="1")
	panggildb = json.loads(panggildb[0][1])
	nama = panggildb['nama']

	output = { 'sensor' : panggildb['sensor1']}
	jsondata = json.dumps(output)
	resp = Response(jsondata, status=200, mimetype='application/json')
	
	if request.method == 'POST':
		try:
			misahjs = json.loads(request.data)
			nama2 = misahjs['nama']
		except Exception:
			abort(500)
		if 'suhu' and 'waktu' in request.data:
			try:
				if nama2 in nama:
					callvar = nama[('%s' % nama2)]
					del misahjs['nama']
				else:
					abort(500)
			except Exception:
				abort(500)
			panggildb[('%s' % callvar)].append(misahjs)
			lines = { ('%s' % callvar) :sorted(panggildb[('%s' % callvar)], key=lambda k: k['waktu'], reverse=True)}
			susun = {
			'nama' : nama,
			('%s' % callvar) : lines[('%s' % callvar)]	
			}
			
			print susun
			jsondata = json.dumps(susun)
			resp = Response(jsondata, status=200, mimetype='application/json')
			return resp
		return request.data
	else:
		return resp
'''


@api.route('/gpio/<username>', methods = ['PUT','GET'])
def getgpio(username):
	try:
		username = int(username)
		print username
		panggildb = selectdb(device,device.user_id,nilai=username)
		panggildb = json.loads(panggildb[0][2])
		if request.method == 'PUT':
			return "put masuk"
		else:
			return jsonify(panggildb)
	except Exception:
		return abort(401)

@api.route('/post', methods = ['POST','GET'])
def cobapost():
	if request.method == 'POST':
		data = decryptsl('my_device_raspberry',eval(request.data))
		return data
	else:
		return abort(404)
