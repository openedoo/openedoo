from datetime import datetime, timedelta
from openedoo.core.db import query
from openedoo.core.db.db_tables import od_users
from openedoo.core.libs.tools import hashingpw
from openedoo.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
import json

now_temp = datetime.now()
now = now_temp.strftime('%Y-%m-%d %H:%M:%S')

query = query()



def registration(username, password, email, name, phone):
    user_profile = {"email":email,"phone":phone,"name":name}
    user_profile_json = json.dumps(user_profile)
    public_key = 'NULL'
    private_key = 'NULL'

    acak_pass = (randomword(16)+password)
    password_hash = hashingpw2(password)
    access_token = hashingpw(acak_pass)
    try:
        data = od_users(
            username=username,
            password=password_hash,
            access_token= access_token,
            public_key= public_key,
            private_key=private_key,
            status=1,
            role='0',
            created=now,
            last_login=now,
            user_profile=str(user_profile_json)
        )
        query.insert_db(new=data)
    except Exception:
        return False
    return user_profile_json

def delete(user_id):
    try:
        if len(query.select_db(tables=od_users, column=od_users.user_id, value=user_id)) < 1 :
            response = json.dumps({"Status":"User not Found"})
        else:
            query.delete_db(tables=od_users, data=user_id)
            response = json.dumps({"Status":"Success"})
    except Exception as e:
        response = json.dumps({"Status":"Failed"})
    return response

class search(object):
    response = None

    def __init__(self):
        pass
    def by_id(self, user_id):
        data = query.select_db(tables=od_users, column=od_users.user_id, value=user_id)
        if len(data) < 1:
            self.response = json.dumps({"Status":"User not Found"})
        for index in range(len(data)):
            self.response = json.dumps({
                "{}".format(data[index][1]):{
                    "username":"{}".format(data[index][1]),
                    "user_profile":"{}".format(data[index][10])
                }
            })

    def show_data(self):
        return self.response

def update(user_id):
    if len(query.select_db(tables=od_users, column=od_users.user_id, value=user_id))<1:
        response = json.dumps({"Status":"User not Found"})
    else:
        try:
            query.update_db(tables=od_users, column=od_users.user_id, value_column='', dict_update=[])
            response = json.dumps({"Status":"Success"})
        except Exception as e:
            response = json.dumps({"Status":"Failed"})
    return response



object = search()
