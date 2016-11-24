from flask import Blueprint
from flask import request
from flask import Response
import json
import member as M
from openedoo.core.db import query
from openedoo.core.db.db_tables import od_users
from openedoo.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
from openedoo.core.libs.auth import *
from datetime import datetime,timedelta
from flask import abort

query = query()

member = Blueprint('hello', __name__)

@member.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"

@member.route('/add', methods=['POST','GET'])
def add():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        username = load_json['username']
        password = load_json['password']
        email = load_json['email']
        name = load_json['name']
        phone = load_json['phone']

#        if (username or email or password) is None:
#            abort(401)
    member = M.registration(username,password,email,name,phone)
    payload = {'messege':'registration sucessful'}
    payload = json.dumps(payload)
    resp = Response(payload, status=200, mimetype='application/json')
    return resp

@member.route('/delete', methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
    else:
        user_id = request.args.get('id')
    return member.delete(user_id=user_id)

@member.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
        member.object.by_id(user_id=user_id)
        #member.object.order_by(user_id=user_id)
        return member.object.show_data()

@member.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        load_json = json.loads(request.data)

@member.route('/test',methods=['GET'])
@token_auth_header
def check():
    return "akla"