from functools import wraps
from flask import request, abort
from db import selectdb
from db.db_tables import Users
from tools import cocokpw,hashingpw,checkpass2

def check_auth(username, password):
    return username == 'admin' and password == 'secret'

def check_token(token):
    try:
        a = selectdb(Users,Users.public_key,nilai=token)
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


def token_auth(f):
    @wraps(f)
    def token_decorator(*args,**kwargs):
        token = request.headers.get('token')
        agent = request.headers.get('User-Agent')
        if agent is None:
            abort(403)
        elif check_token(token) != True:
            abort(401)
        return f(*args, **kwargs)
    return token_decorator

def token_auth2(f):
    @wraps(f)
    def token_decorator2(*args,**kwargs):
        token =  request.args.get('token')
        print token
        if check_token(token) != True:
            abort(401)
        return f(*args, **kwargs)
    return token_decorator
