from flask import Blueprint, render_template
from flask import request
from flask import Response
import json
from app.core.libs.db.db_query import insertdb, deletedb, selectdb
from app.core.libs.db.db_tables import od_users
from app.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
from datetime import datetime,timedelta
from flask import abort


hello = Blueprint('hello', __name__)

now = datetime.now()
sekarang = now.strftime('%Y-%m-%d %H:%M:%S')

@hello.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"

@hello.route('/add/', methods=['POST', 'GET'])
def addmember():
    if request.method == 'POST':
        loadjson = json.loads(request.data)
        password = loadjson['password']
        public_key = 'NULL'
        private_key = 'NULL'

        acakpass = (randomword(16)+password)
        passwordhash = hashingpw2(password)
        access_token = hashingpw(acakpass)
        datajs = {'token':acakpass,'password':passwordhash,'acess_token':access_token,'public_key':public_key}
        userprofile = {"email":loadjson['email'],"phone":loadjson['phone'],"name":loadjson['name']}
        user_profile = json.dumps(userprofile)
        
        try:
            data = od_users(
                username=loadjson['username'],
                password=passwordhash,
                access_token= access_token,
                public_key= public_key,
                private_key=private_key,
                status='0',
                role='0',
                created=sekarang,
                last_login=sekarang,
                user_profile=str(user_profile),
            )
            try:
                insertdb(data)

            except Exception as e:
                print e

        except Exception as e:
            return e
        response = Response(user_profile, status=201, mimetype='application/json')
        return response
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
