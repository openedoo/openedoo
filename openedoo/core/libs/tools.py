import hashlib
import random, string
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import Signer, URLSafeSerializer as urlsafe
import redis,json

def random_word(length):
	return ''.join(random.choice(string.lowercase+string.uppercase+string.digits) for i in range(length))

def hashing_password(password):
	try:
		hashpw = hashlib.sha224()
		hashpw.update(password)
		data = hashpw.hexdigest()
		return data
	except Exception:
		return False
def check_password(password_input,password_hash):
	try:
		hashpw = hashlib.sha224()
		hashpw.update(password)
		data = hashpw.hexdigest()
		if data == passworddb:
			return True
		else:
			return False
	except Exception:
		return False

def hashing_password_2(password):
	hashpw = generate_password_hash(password)
	return hashpw

def check_password_2(password_hash,password_input):
	check = check_password_hash(password_hash,password_input)
	return check

def session_encode(string_input):
	data = (random_word(16)+"."+string_input+"."+random_word(16))
	s = urlsafe('generate:openedoo')
	b = s.dumps(data)
	return b

def session_decode(string_input):
	s = urlsafe('generate:openedoo')
	data = s.loads(string_input)
	words = data.split(".")
	return words[1]

def set_redis(key,data,secnd):
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

def get_redis(key):
	try:
		r = redis.StrictRedis()
		data = r.get(key)
		return json.loads(data)
	except Exception:
		return False
