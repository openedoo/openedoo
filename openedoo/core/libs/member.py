from datetime import datetime, timedelta
from openedoo.core.libs.db import query
from openedoo.core.libs.db.db_tables import od_users
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
            created=now,
            last_login=now,
            user_profile=str(user_profile_json)
        )
        query.insert_db(new=data)
    except Exception:
        return False
    return user_profile_json

def login(username, password):
    try:
        data = query.selectdb(od_users,None, None)
        if len(data) < 1:
            return False
        return data
    except Exception as e:
        return False
