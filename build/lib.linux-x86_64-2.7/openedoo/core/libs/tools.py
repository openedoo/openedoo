import hashlib
import random, string
from werkzeug.security import generate_password_hash, check_password_hash
from itsdangerous import Signer, URLSafeSerializer as urlsafe
import redis,json
import smtplib
import os
from urllib2 import urlopen, URLError, HTTPError


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

def hashing_werkzeug(password):
	hashpw = generate_password_hash(password)
	return hashpw

def check_werkzeug(password_hash,password_input):
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

def send_email(mail_user, mail_password, mail_recipient, subject, body):
	FROM = mail_user
	TO = mail_recipient if type(mail_recipient) is list else [mail_recipient]
	SUBJECT = subject
	TEXT = body

	# Prepare actual message
	message = """From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		server = smtplib.SMTP_SSL("mail.openedoo.org", 465)
		server.ehlo()
		#server.starttls()
		server.login(mail_user, mail_password)
		server.sendmail(FROM, TO, message)
		server.close()
		return 'successfully sent the mail'
	except Exception as e:
		return "failed to send mail"
