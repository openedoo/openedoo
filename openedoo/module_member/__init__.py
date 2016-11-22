from flask import Blueprint
from flask import request
from flask import Response
import json
import member
from openedoo.core.db import query
from openedoo.core.db.db_tables import od_users
from openedoo.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
from datetime import datetime,timedelta
from flask import abort
from member import aktivasi, edit_password



query = query()

member = Blueprint('hello', __name__)

@member.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"

@member.route('/add/', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        username = load_json['username']
        password = load_json['password']
        email = load_json['email']
        name = load_json['name']
        phone = load_json['phone']
    else:
        username = request.args.get('username')
        password = request.args.get('password')
        email = request.args.get('email')
        name = request.args.get('name')
        phone = request.args.get('phone')
    try:
        if (username or email or password) is None:
            abort(401)
        member.registration(username,password,email,name,phone)
        payload = {'messege':'registration sucessful'}
        payload = json.dumps(payload)
        resp = Response(payload, status=200, mimetype='application/json')
        return resp
    except Exception as e:
        return e

@member.route('/delete/', methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
    else:
        user_id = request.args.get('id')
    return member.delete(user_id=user_id)

@member.route('/find/', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
        member.object.by_id(user_id=user_id)
        #member.object.order_by(user_id=user_id)
        return member.object.show_data()

@member.route('/activation/<key>')
def activation(key):
    try:
        aktivasi(key)
    except Exception as e:
        raise e

@member.route('/password/', methods=['POST','GET'])
def password():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        try:
            edit_password(
                user_id=load_json['user_id'],
                password_old=load_json['old_password'],
                password_new=load_json['new_password'],
                password_confirm=load_json['confirm_password']
            )
        except Exception as e:
            raise
