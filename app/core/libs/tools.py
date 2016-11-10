import hashlib
import random, string
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import Signer, URLSafeSerializer as urlsafe
import redis,json

def randomword(length):
	return ''.join(random.choice(string.lowercase+string.uppercase+string.digits) for i in range(length))

def hashingpw(password):
	try:
		hashpw = hashlib.sha224()
		hashpw.update(password)
		data = ('@rp!:%s' % hashpw.hexdigest())
		return data
	except Exception:
		return False
def cocokpw(password,passworddb):
	try:
		hashpw = hashlib.sha224()
		hashpw.update(password)
		data = ('@rp!:%s' % hashpw.hexdigest())
		if data == passworddb:
			return True
		else:
			return False
	except Exception:
		return False

def hashingpw2(password):
	me = generate_password_hash(password)
	return me

def checkpass2(password,password_input):
	choice = check_password_hash(password,password_input)
	return choice
def gettoken(username):
	acak = randomword(4)
	data = (acak+username)
	s = urlsafe('generate:grupi.org')
	b = s.dumps(data)
	return b

def setredis(key,data,secnd):
	try:
		r = redis.StrictRedis()
		data = json.dumps(data)
		dataset = (str(key),str(data))
		a = r.set('%s' %key,'%s' %data)
		#rdis.bgsave()
		b = r.expire('%s' %key, secnd)
		return a
	except Exception:
		return False

def getredis(key):
	try:
		r = redis.StrictRedis()
		data = r.get(key)
		return json.loads(data)
	except Exception:
		return False
