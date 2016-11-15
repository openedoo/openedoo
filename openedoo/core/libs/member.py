from flask import abort, request, Response
from datetime import datetime, timedelta
from openedoo.core.libs.db import query
from openedoo.core.libs.db.db_tables import od_users
from openedoo.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
import json
from flask import abort

now = datetime.now()
sekarang = now.strftime('%Y-%m-%d %H:%M:%S')

query = query()

def registration(username, password, email, name, phone):
    userprofile = {"email":email,"phone":phone,"name":name}
    user_profile = json.dumps(userprofile)
    public_key = 'NULL'
    private_key = 'NULL'

    acakpass = (randomword(16)+password)
    passwordhash = hashingpw2(password)
    access_token = hashingpw(acakpass)
    try:
        data = od_users(
            username=username,
            password=passwordhash,
            access_token= access_token,
            public_key= public_key,
            private_key=private_key,
            status=1,
            role='0',
            created=sekarang,
            last_login=sekarang,
            user_profile=str(user_profile)
        )
        try:
            query.insert_db(new=data)
        except Exception as e:
            raise e
    except Exception as e:
        raise e
    return user_profile

def login(username, password):
    try:
        data = query.selectdb(od_users,None, None)
        if len(data) < 1:
            abort(403)
        return data
    except Exception as e:
        return "Error"
