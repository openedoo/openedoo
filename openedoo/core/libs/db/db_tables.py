from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
import json
from datetime import datetime, date
import datetime
from sqlalchemy.orm import relationship, backref,create_session,Session, sessionmaker
from openedoo import config

engine = create_engine(config.DB)
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
	def __init__(self,user_id, username,password,access_token,public_key,private_key,status,role,created,last_login,user_profile):
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
		self.user_profile = user_profile

