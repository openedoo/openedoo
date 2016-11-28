from functools import wraps
from openedoo.core.libs import request, abort, session, Response
from openedoo.core.db import query
from openedoo.core.db.db_tables import od_users
from tools import *

query_auth = query()
def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def check_token(token):
    try:
        user_check = query_auth.select_db(od_users, od_users.public_key, value=token)
        password = user_check[0][5]
        if password != hashing_password(token) or user_check[0][6] == 0 :
            return abort(401)
        set_redis(token,user_check[0][1],86400)
        return True
    except Exception as e:
        return abort(401)

def login(username, password):
    try:
        check_user = query_auth.select_db(tables=od_users, column=od_users.username, value=username)
        if len(check_user) < 1:
            return {"message":"User not found","token":""}
        check_password = check_werkzeug(password_hash= check_user[0][2], password_input=password)
        if check_password != True:
            return {"message":"Wrong Password","token":""}
        sasy = session_encode(check_user[0][3])
        session['username'] = sasy
        print "hahah"
        return {"message":"Login Success","token":check_user[0][5]}
    except Exception as e:
        return e

def get_user_id(token):
    try:
        user_check = query.select_db(od_users, od_users.public_key, value=token)
        password = a[0][5]
        if password == hashing_password(token):
            return True
    except Exception as e:
        return abort(401)

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return abort(401)
        return f(*args, **kwargs)
    return decorated

def read_session(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        session.permanent = True
        try:
            if session['username'] is False:
                error = json.dumps({"message":"You must Login first"})
                return Response(error, status=401, mimetype='application/json')
            return f(*args, **kwargs)
        except KeyError:
            error = json.dumps({"message":"Your Session is time out, login first"})
            return Response(error, status=401, mimetype='application/json')
    return wrap

def logout():
    session['username'] = False
    return {"Message":"Log out"}

def token_auth_header(f):
    @wraps(f)
    def token_decorator(*args,**kwargs):
        token = request.headers.get('token')
        if check_token(token) != True:
            abort(401)
        return f(*args, **kwargs)
    return token_decorator

def token_auth_params(f):
    @wraps(f)
    def token_decorator2(*args,**kwargs):
        token =  request.args.get('token')
        if check_token(token) != True:
            abort(401)
        return f(*args, **kwargs)
    return token_decorator
