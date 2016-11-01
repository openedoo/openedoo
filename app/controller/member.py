
from flask import Blueprint, render_template
import json
from flask import jsonify, abort, Flask, g, request, Response
from app.model.member import addmember2,aktifasi

member = Blueprint('newbot_member', __name__)

from flask import jsonify, abort, Flask, g, request, Response
import json

@member.route('/')
def newbot():
	return "hello world"

@member.route('/add', methods = ['POST','GET'])
def add_member():
	if request.method == 'POST':
		#try:
		misahjs = json.loads(request.data)
		if misahjs['username'] is None or misahjs['password'] is None or misahjs['email'] is None or misahjs['phone'] is None or misahjs['name'] is None:
			abort(401)
		print misahjs
		name = "NULL"
		phone = "NULL"
		if misahjs['phone'] is not None:
			phone = str(misahjs['phone'])
		else:
			phone = "NULL"
		if misahjs['name'] is not None:
			name = str(misahjs['name'])
		else:
			name = "NULL"
		print name, phone
		email = str(misahjs['email'])
		username = str(misahjs['username'])
		password = str(misahjs['password'])
		data = (username,password,email,phone,name)
		print data
		add = addmember2(data)
		if add == False:
			payload = {'messege':'data not valid'}
			jsondata = json.dumps(payload)
			resp = Response(jsondata, status=400, mimetype='application/json')
			return resp
		payload = {'messege':'pendaftaran sukses'}
		jsondata = json.dumps(payload)
		resp = Response(jsondata, status=200, mimetype='application/json')
		return resp
		#except Exception:
		#	abort(500)

@member.route('/aktifasi/<key_user>')
def verifikasi_member(key_user):
	aktifmember = aktifasi(key_user)
	if aktifmember == False:
		pesan = "user tidak terdaftar atau user telah aktif"
	else:
		pesan = "user %s telah aktif" % aktifmember
	payload = {'messege':pesan}
	jsondata = json.dumps(payload)
	resp = Response(jsondata, status=200, mimetype='application/json')
	return resp

@member.route('/edit/<kategori>')
def edit_member(kategori):
	return "hello world"

@member.route('/delete')
def delete_member():
	return "hello world"

@member.route('/list')
def list_member():
	return "hello world"

@member.route('/login')
def login_member():
	return "hello world"