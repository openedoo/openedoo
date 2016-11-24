from functools import wraps
from flask import request, abort
from openedoo.core.db import query
from openedoo.core.db.db_tables import od_users
from tools import cocokpw,hashingpw,checkpass2

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def check_token(token):
    try:
        user_check = query.select_db(od_users, od_users.public_key, value=token)
        password = user_check[0][5]
        if password == hashingpw(token):
            return True
    except Exception:
        return abort(401)

def get_user_id(token):
    try:
        user_check = query.select_db(od_users, od_users.public_key, value=token)
        password = a[0][5]
        if password == hashingpw(token):
            return True
    except Exception:
        return abort(401)
        
def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return abort(401)
        return f(*args, **kwargs)
    return decorated

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
        print token
        if check_token(token) != True:
            abort(401)
        return f(*args, **kwargs)
    return token_decorator
