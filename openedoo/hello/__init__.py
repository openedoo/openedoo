from flask import Blueprint
from flask import request
from flask import Response
import json
from openedoo.core.libs.member import registration
from openedoo.core.libs.db import query
from openedoo.core.libs.db.db_tables import od_users
from openedoo.core.libs.tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
from datetime import datetime,timedelta
from flask import abort

query = query()

hello = Blueprint('hello', __name__)

@hello.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"