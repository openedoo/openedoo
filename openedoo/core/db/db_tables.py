from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
import json
from datetime import datetime, date
import datetime
from sqlalchemy.orm import relationship, backref,create_session,Session, sessionmaker
from openedoo import config

engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
metadata = MetaData(bind=engine)
auto_map = automap_base()

class od_users(Base):
	__tablename__ = 'od_user'
	user_id = Column(Integer,primary_key=True,autoincrement=True)
	username = Column(String(16), unique=True)
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
class od_roles(Base):
	__tablename__ = 'od_user_role'
	role_id = Column(Integer, primary_key=True,autoincrement=True)
	role = Column(String(64))
	role_status = Column(Text)
	def __init__(self,role,max_device,role_status):
		self.role = role
		self.role_status = role_status
class od_tryout(Base):
	__tablename__ = 'od_module_tryout'
	tryout_id = Column(Integer, primary_key=True,autoincrement=True)
	tryout_question = Column(Text)
	tryout_selection = Column(Text)
	tryout_answer = Column(Text)
	tryout_weight = Column(Integer)
	tryout_type = Column(String(16))
	tryout_attachment = Column(Text)
	tryout_attachment_information = Column(Text)
	def __init__(self,tryout_question,tryout_selection,tryout_answer,tryout_weight,tryout_type,tryout_attachment,tryout_attachment_information):
		self.tryout_question = tryout_question
		self.tryout_selection = tryout_selection
		self.tryout_answer = tryout_answer
		self.tryout_weight = tryout_weight
		self.tryout_type = tryout_type
		self.tryout_attachment = tryout_attachment
		self.tryout_attachment_information = tryout_attachment_information
