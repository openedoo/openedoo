from flask import Blueprint
from flask import request
from flask import Response
import json
import member as Member
from openedoo.core.libs.tools import *
from flask import abort
from member import aktivasi, edit_password


member = Blueprint('hello', __name__, url_prefix='/beta/member')

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
    try:
        if (username or email or password) is None:
            abort(401)
        Member.registration(username,password,email,name,phone)
        payload = {'message':'registration sucessful'}
        payload = json.dumps(payload)
        resp = Response(payload, status=200, mimetype='application/json')
        print resp
        return resp
    except Exception as e:
        print e

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
        Member.object.by_id(user_id=user_id)
        #member.object.order_by(user_id=user_id)
        return member.object.show_data()

@member.route('/update', methods=['GET','POST'])
def update():
    if request.method == 'POST':
        load_json = json.loads(request.data)

@member.route('/test',methods=['GET'])
#@token_auth_header
def check():
    return "akla"

@member.route('/activation/<key>')
def activation(key):
    aktivasi = json.dumps(Member.aktivasi(key))
    resp = Response(aktivasi, status=200, mimetype='application/json')
    return resp

@member.route('/password/', methods=['POST','GET'])
def password():
    if request.method == 'POST':
        load_json = json.loads(request.data)

        edit = json.dumps(Member.edit_password(
            user_id=load_json['user_id'],
            password_old=load_json['old_password'],
            password_new=load_json['new_password'],
            password_confirm=load_json['confirm_password']
        ))
        resp = Response(edit, status=200, mimetype='application/json')

    return resp

@member.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        load_json = json.loads(request.data)
        log = json.dumps(Member.login(password=load_json['password'], username=load_json['username']))
        resp = Response(log, status=200, mimetype='application/json')
        return resp

@member.route('/logout/')
@Member.login_required
def logout():
    log = json.dumps(Member.logout())
    resp = Response(log, status=200, mimetype='application/json')
    return resp

@member.route('/coba')
@Member.login_required
def coba():
    return 'a'
