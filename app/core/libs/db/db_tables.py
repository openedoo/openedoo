from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
import json
from datetime import datetime, date
import datetime
from sqlalchemy.orm import relationship, backref,create_session,Session, sessionmaker



#Base = declarative_base()
engine = create_engine('mysql://root:aris1996@localhost:3306/openedoo')
Base = declarative_base()
metadata = MetaData(bind=engine)
auto_map = automap_base()

class od_session(Base):
	__tablename__ = 'od_user_session'
	session_id = Column(Integer, primary_key=True,autoincrement=True)
	user_id = Column(Integer)
	token_session = Column(Text())
	created = Column(DateTime())
	def __init__(self,session_id,user_id,token_session,created):
		self.session_id = session_id
		self.user_id = user_id
		self.token_session = token_session
		self.created = created

class od_users(Base):
	__tablename__ = 'od_user'
	user_id = Column(Integer,primary_key=True,autoincrement=True)
	username = Column(String(16))
	password = Column(Text())
	access_token = Column(Text())
	public_key = Column(Text())
	private_key = Column(Text())
	status = Column(Integer)
	role = Column(String(64))
	created = Column(DateTime())
	last_login = Column(DateTime())
	user_profile = Column(Text())
	def __init__(self,username,password,access_token,public_key,private_key,status,role,created,last_login,user_profile):
		self.username = username
		self.password = password
		self.access_token = access_token
		self.public_key = public_key
		self.private_key = private_key
		self.status = status
		self.role = role
		self.created = created
		self.last_login = last_login
		self.user_profile = user_profile
	'''
	def insert(data):
		Session = sessionmaker(bind=engine)
		session = Session()
		Base.metadata.create_all(engine)

		data = od_users(
			username=self.username,
			password=self.password,
			access_token= self.access_token,
			public_key= self.public_key,
			private_key=self.private_key,
			status=self.status,
			role=self.role,
			created=self.created,
			last_login=self.last_login,
			user_profile=self.user_profile,
		)


		session.add(data)
		session.commit()
		'''

def db_create():
	engine = create_engine('mysql://root:aris1996@localhost:3306/openedoo')
	metadata = MetaData(bind=engine)
	auto_map = automap_base()
	Base.metadata.create_all(engine)

db_create()
