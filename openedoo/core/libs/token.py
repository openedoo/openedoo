import jwt
import datetime
from flask import g
from functools import wraps
from flask import request, jsonify
from jwt import InvalidTokenError, ExpiredSignatureError

def encode_auth_token(secret_key, user_id, expired_time):
    """ Encode id to token """
    if expired_time is None:
        expired_time = datetime.datetime.utcnow() + datetime.timedelta(days=1)
    try:
        payload = {
            'sub': int(user_id),
            'iat': datetime.datetime.utcnow(),
            'exp': expired_time
        }
        token = jwt.encode(
            payload,
            secret_key, algorithm='HS256'
        )
        return token.decode('unicode_escape')
    except Exception as e:
        raise

def decode_auth_token(secret_key, auth_token):
    """
        Decodes the auth token
        :param auth_token:
        :return: integer|string
    """
    """if app_name is None:
        #from openedoo_project import app
        app = ""
        app_name = app"""
    try:
        token = auth_token.headers.get('Authorization').split( )[1]
    except AttributeError:
        token = auth_token
    except Exception:
        token = auth_token.headers.get('Authorization')

    payload = jwt.decode(token, secret_key)
    return payload

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not request.headers.get('Authorization'):
            response = jsonify(message="Missing Authorization header"), 401
            return response
        try:
            payload = decode_auth_token(request)
        except ExpiredSignatureError:
            return jsonify(message='Signature Expired. Please log in again.'), 401
        except InvalidTokenError:
            return jsonify(message='Invalid token. Please log in again.'), 401
        g.user_id = payload
        return f(*args, **kwargs)
    return decorated_function
