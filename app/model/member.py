from db.ormdua import insertdb,Users,selectdb,update_table_user,update_table_user2
from tools import randomword,hashingpw,cocokpw,setredis,getredis,hashingpw2,checkpass2
from datetime import datetime,timedelta
import json

from datetime import datetime

now = datetime.now()
sekarang = now.strftime('%Y-%m-%d %H:%M:%S')


def addmember(username,password,email,phone,name):
	userdb = selectdb(Users,Users.username, nilai=username)
	if userdb:
		return False
	acak_token = (randomword(16)+username)
	password_hash = hashingpw2(password)
	access_token = hashingpw(acak_token)
	public_key = 'NULL'
	private_key = 'NULL'
	datajs = {'token':acak_token,'password':password_hash,'acess_token':access_token,'public_key':public_key}
	userprofile = {"email":email,"phone":phone,"name":name}
	user_profile = json.dumps(userprofile)
	try:
		new = Users(None, username, password_hash,access_token,public_key,private_key,'0','0',sekarang,sekarang,'[]',str(user_profile))
		a = insertdb(new)
		return True
	except Exception:
		return False

def addmember2(data):
	#print data
	username = data[0]
	password = data[1]
	email = data[2]
	phone = data[3]
	name = data[4]
	#print username,password,email,phone,name
	try:
		addmember(username,password,email,phone,name)
		return True
	except Exception:
		return False

def aktifasi(data):
	try:
		a = selectdb(Users,Users.access_token,nilai=data)
		user_id = a[0][0]
		username = a[0][1]
		if a == [] or a[0][6]==1:
			return False
		acak = randomword(32)
		hashpw = hashingpw(acak)
		data_dict = {'public_key':acak,'private_key':hashpw,'status':'1','role':'[0,0]'}
		update_table_user2(Users,Users.user_id,user_id,data_dict)
		return username
	except Exception:
		return False

def login(username,password):
	try:
		userdb = selectdb(Users,Users.username, nilai=username)
		print userdb[0]
	except Exception:
		return False
	if userdb[0][6] == 0:
		return "user id telah terdaftar"
	check = checkpass2(userdb[0][2],password)
	if check != True:
		return False
	else:
		print userdb[0][9]
		return True
#print login('ligerrendy','rendiimut')
#print addmember('ligerrendy', '16102510182', '16102510182', '16102510182', '16102510182')
#aktifasi('@rp!:09ff1a597246c9d81c22e708bf28838d7c932e3ed6ccf4b0ffdb072b')