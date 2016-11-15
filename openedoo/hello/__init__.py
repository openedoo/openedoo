from flask import Blueprint
from flask import request
from flask import Response
import json
from openedoo.core.libs.member import registration
from openedoo.core.libs.db import query
from openedoo.core.libs.db.db_tables import od_users
from openedoo.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
from datetime import datetime,timedelta
from flask import abort

query = query()

hello = Blueprint('hello', __name__)

@hello.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"

@hello.route('/add/', methods=['POST', 'GET'])
def addmember():
    if request.method == 'POST':
        loadjson = json.loads(request.data)
        password = loadjson['password']
        username = loadjson['username']
        name = loadjson['name']
        email = loadjson['email']
        phone = loadjson['phone']
        try:
            registration(username=username, password=password, name=name, email=email, phone=phone)
        except Exception as e:
            return e
        return "Successfully add member"
    else:
        return "Coba"

@hello.route('/delete/', methods=['GET', 'POST'])
def delmember():
    if request.method == 'POST':
        loadjson = json.loads(request.data)
        if loadjson['user_id'] is None:
            abort(401)

        datauser = query.select_db(tables=od_users, column=od_users.user_id, value=loadjson['user_id'])
        if len(datauser) >= 1:
            try:
                query.delete_db(od_users, loadjson['user_id'])
                response = 'Berhasil'
            except Exception as e:
                return e
        else:
            response = 'Data tidak ditemukan'
    else:
        return "Delete Data"
    return response

@hello.route('/find/', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        loadjson = json.loads(request.data)
        if len(loadjson['user_id']) < 1:
            user = query.select_db(tables=od_users, column=None, value=None)
        else:
            user = query.select_db(tables=od_users, column=od_users.user_id, value=loadjson['user_id'])
        if len(user)>=1:
            try:
                value = []
                for data in range(len(user)):
                    value.append({user[data][0]:{"user_id":user[data][0],"username":user[data][1]}})
                value = Response(json.dumps(value), mimetype='application/json', status=202)
            except Exception as e:
                raise
        else:
            value = "Not Found"
    else:
        value = "Find with Json POST"
    return value

@hello.route('/update/', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        loadjson = json.loads(request.data)
        if loadjson['user_id'] is None or len(loadjson['user_id']) < 1:
            abort(401)
        user = query.select_db(tables=od_users, column=od_users.user_id, value=loadjson['user_id'])
    return "ADA"
