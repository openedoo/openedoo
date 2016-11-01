from sqlalchemy import *
from sqlalchemy.orm import relationship, backref,create_session,Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import json
from datetime import datetime, date
import datetime

engine = create_engine('mysql://root:ayambakar@localhost:3306/pagekit')
Base = declarative_base()
metadata = MetaData(bind=engine)
auto_map = automap_base()

 
class device(Base):
	__tablename__ = 'gr_device'
	no_device = Column(Integer, primary_key=True,autoincrement=True)
	user_id = Column(Integer)
	value_sensor = Column(String)
	gpio = Column(String)
	name_device = Column(String)
	last_connect = Column(String)
	def __init__(self,no_device,user_id,value_sensor,gpio,name_device,last_connect):
		self.no_device = no_device
		self.user_id = user_id
		self.value_sensor = value_sensor
		self.gpio = gpio
		self.name_device = name_device
		self.last_connect = last_connect

class Users(Base):
	__tablename__ = 'gr_user'
	user_id = Column(Integer,primary_key=True,autoincrement=True)
	username = Column(String)
	password = Column(String)
	access_token = Column(String)
	public_key = Column(String)
	private_key = Column(String)
	status = Column(Integer)
	role = Column(String)
	created = Column(String)
	last_login = Column(String)
	device = Column(String)
	user_profile = Column(String)
	def __init__(self,user_id, username,password,access_token,public_key,private_key,status,role,created,last_login,device,user_profile):
		self.user_id = user_id
		self.username = username
		self.password = password
		self.access_token = access_token
		self.public_key = public_key
		self.private_key = private_key
		self.status = status
		self.role = role
		self.created = created
		self.last_login = last_login
		self.device = device
		self.user_profile = user_profile
'''	def __repr__(self):
		return "<User(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)>" % (self.user_id, self.username, self.password, self.access_token,self.public_key,self.private_key,self.status,self.role,self.created,self.last_login,self.device,self.user_profile)
'''


def selectdb(namatable,filtering, **nilai_optional):
	session = sessionmaker()
	session.configure(bind=engine)
 	Base.metadata.create_all(engine)
	s = session()
	if ('nilai' in nilai_optional):
		kueridb = s.query(namatable).filter(filtering == nilai_optional['nilai'])
	else:
		kueridb = s.query(namatable)
	list1 = list(s.execute(kueridb))
	engine.dispose()
	return list1

def update_table_user(val1, val2, val3,val4,val5):
	session = sessionmaker()
	session.configure(bind=engine)
 	Base.metadata.create_all(engine)
	s = session()
	try:
		s.query(Users).filter_by(access_token=val1).update(dict(public_key=val2,private_key=val3,status=val4,role=val5))
		s.commit()
		return True
	except Exception:
		return False

def update_table_user2(namatable,filtering,nilai_optional,dict_update):
	namatable = namatable
	session = sessionmaker()
	session.configure(bind=engine)
 	Base.metadata.create_all(engine)
	s = session()
	try:
		s.query(Users).filter(filtering==nilai_optional).update(dict_update)
		s.commit()
		return True
	except Exception:
		return False

def insertdb(new):
	try:
		session = sessionmaker()
		session.configure(bind=engine)
		Base.metadata.create_all(engine)
		s = session()
		Base.metadata.create_all(engine)
		s.add(new)
		s.commit()
		engine.dispose()
		return True
	except Exception:
		return False

def deletedb(namatable,data):
	try:
		namatable = namatable
		session = sessionmaker()
		session.configure(bind=engine)
		Base.metadata.create_all(engine)	
		s = session()
		Base.metadata.create_all(engine)
		jack = s.query(namatable).get(data)
		s.delete(jack)
		s.commit()
		return True
	except Exception as e:
		return False
#print delete(Users,4)
#dict_update = (access_token="asd")
#print insert_table_user2(Users,Users.user_id,6,{"username": "Bob Marley"})
#print user()
#kueridb.tambah
#kueridb = s.add(kueridb)

#list1 = list(s.execute(kueridb))
#engine.dispose()


'''
jsonkan = list1[0][1]
deco = json.loads(jsonkan)
print deco
test = len(deco["sensor1"])
print deco['sensor1']
lines = sorted(deco['sensor1'], key=lambda k: k['waktu'], reverse=True)
print lines
test = len(lines)
#test = 300
if test > 1:
	for i in range(int(test)-1,-1,-1):
		del lines[i]
		print i
	print lines

'''
