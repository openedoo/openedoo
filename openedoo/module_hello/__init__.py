from flask import Blueprint
from flask import request
from flask import Response
import json
from openedoo.core.member import member
from openedoo.core.db import query
from openedoo.core.db.db_tables import od_users
from openedoo.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
from datetime import datetime,timedelta
from flask import abort



query = query()

hello = Blueprint('hello', __name__)

@hello.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"

@hello.route('/add/', methods=['POST','GET'])
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
        return "Berhasil"
    except Exception as e:
        return "GAGAL"

@hello.route('/delete/', methods=['GET','POST'])
def delete():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
    else:
        user_id = request.args.get('id')
    return member.delete(user_id=user_id)

@hello.route('/find/', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        user_id = load_json['user_id']
        member.object.by_id(user_id=user_id)
        #member.object.order_by(user_id=user_id)
        return member.object.show_data()

@hello.route('/update/', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        load_json = json.loads(request.data)
