from datetime import datetime, timedelta
from openedoo.core.db import query
from openedoo.core.db.db_tables import od_users
from openedoo.core.libs.tools import *
from openedoo.core.libs.auth import *
import json
from email.utils import parseaddr
from functools import wraps
from openedoo.core.libs import session, Response


now_temp = datetime.now()
now = now_temp.strftime('%Y-%m-%d %H:%M:%S')

query = query()

def registration(username, password, email, name, phone):
    user_check = query.select_db(od_users, od_users.username, value=username)
    if user_check:
        return {'message':'username is exist'}
    user_profile = {"email":email,"phone":phone,"name":name}
    user_profile_json = json.dumps(user_profile)
    public_key = 'NULL'
    private_key = 'NULL'
    test_mail = '@' in parseaddr(email)[1]
    if test_mail == False:
        return {'message':'invalid mail'}

    acak_pass = (random_word(16)+username)
    password_hash = hasing_werkzeug(password)
    access_token = hashing_password(acak_pass)
    try:
        data = od_users(
            username=username,
            password=password_hash,
            access_token= access_token,
            public_key= public_key,
            private_key=private_key,
            status=0,
            role=1,
            created=now,
            last_login=now,
            user_profile=str(user_profile_json)
        )
        query.insert_db(new=data)
        return True
    except Exception as e:
        return e

def delete(user_id):
    try:
        if len(query.select_db(tables=od_users, column=od_users.user_id, value=user_id)) < 1 :
            response = json.dumps({"message":"User not Found"})
        else:
            query.delete_db(tables=od_users, data=user_id)
            response = {"message":"Success"}
    except Exception as e:
        response = {"message":"Failed"}
    return response

class search(object):
    response = None

    def __init__(self):
        pass
    def by_id(self, user_id):
        data = query.select_db(tables=od_users, column=od_users.user_id, value=user_id)
        if len(data) < 1:
            self.response = {"message":"User not Found"}
        for index in range(len(data)):
            self.response = {
                "{}".format(data[index][1]):{
                    "username":"{}".format(data[index][1]),
                    "user_profile":"{}".format(data[index][10])
                }
            }

    def show_data(self):
        return self.response

def activation(access_token):
    try:
        userdb = query.select_db(tables=od_users, column=od_users.access_token, value=access_token)
        user_id = userdb[0][0]
        if userdb is [] or userdb[0][6]:
            return {'message':'user is active'}
    except Exception as e:
        return {'message':'user not found'}
    acak_pass = (random_word(64)+userdb[0][1])
    acak_pass = hashing_password(acak_pass)
    hash_pass = hashing_password(acak_pass)
    data_dict = {'public_key':acak_pass,'private_key':hash_pass,'status':1,'role':3}
    query.update_db(tables=od_users,column=od_users.access_token,value_column=access_token,dict_update=data_dict)
    return {"message":"Activation Success"}



def edit_password(user_id,password_old, password_new, password_confirm):
    if password_new != password_confirm:
        return {'message':'new password not match'}
    userdb = query.select_db(tables=od_users,column=od_users.user_id,value=user_id)
    if check_werkzeug(userdb[0][2],password_old) != True:
        return {'message':'password invalid'}
    elif check_werkzeug(userdb[0][2],password_new) == True:
        return {'message':'prohibited using same password'}
    password_hash = hasing_werkzeug(password_new)
    data_dict = {'password':password_hash}
    query.update_db(tables=od_users,column=od_users.user_id,value_column=user_id,dict_update=data_dict)
    return {'message':'password has change'}

def edit_profile(user_id,user_profile):
    query.update_db(tables=od_users,column=od_users.user_id,value_column=user_id,dict_update=data_dict)
    return {'message':'user profile succesfull to edit'}

object = search()
