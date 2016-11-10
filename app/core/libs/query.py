from flask import abort, request, Response
from datetime import datetime, timedelta
from app.core.libs.db.db_query import insertdb, selectdb
from app.core.libs.db.db_tables import od_users
from app.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
import json
from flask import abort

now = datetime.now()
sekarang = now.strftime('%Y-%m-%d %H:%M:%S')


def add_member(username, password, email, name, phone):
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
            status='0',
            role='0',
            created=sekarang,
            last_login=sekarang,
            user_profile=str(user_profile),
        )
        try:
            insertdb(data)
        except Exception as e:
            return e
    except Exception as e:
        return e
    return user_profile

def login_member(username, password):
    try:
        data = selectdb(od_users,None, None)
        if len(data) < 1:
            abort(403)
        return data
    except Exception as e:
        return "Error"
