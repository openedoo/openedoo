from flask import Blueprint, render_template
from flask import request
from flask import Response
import json
from app.core.libs import query
from app.core.libs.db.db_query import insertdb, deletedb, selectdb
from app.core.libs.db.db_tables import od_users
from app.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
from datetime import datetime,timedelta
from flask import abort


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
            query.add_member(username=username, password=password, name=name, email=email, phone=phone)
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

        datauser = selectdb(od_users, od_users.user_id, nilai=loadjson['user_id'])

        if len(datauser) >= 1:
            try:
                deletedb(od_users, loadjson['user_id'])
                response = 'Berhasil'
            except Exception as e:
                return e
        else:
            response = 'Data tidak ditemukan'
    return response






        #return "Data berhasil dihaspus"
