from sqlalchemy import *
from sqlalchemy.orm import relationship, backref,create_session,Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import json
from datetime import datetime, date

##table declaration
from db_tables import od_session, od_users
from openedoo import config


engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
Base = declarative_base()
metadata = MetaData(bind=engine)
auto_map = automap_base()


class query(object):
	def __init__(self):
		self = "welcome to help menu"

	def select_db(self,tables,column,**value_column):
		try:
			session = sessionmaker()
			session.configure(bind=engine)
	 		Base.metadata.create_all(engine)
			s = session()
			if ('value' in value_column):
				kueridb = s.query(tables).filter(column == value_column['value'])
			else:
				kueridb = s.query(tables)
			list1 = list(s.execute(kueridb))
			engine.dispose()
			return list1
		except Exception:
			return False
			
	def update_db(self,tables,column,value_column,dict_update):
		namatable = namatable
		session = sessionmaker()
		session.configure(bind=engine)
 		Base.metadata.create_all(engine)
		s = session()
		try:
			s.query(tables).filter(column==value_column).update(dict_update)
			s.commit()
			return True
		except Exception:
			return False
	def delete_db(self,tables,data):
#		try:
		#namatable = tables
		session = sessionmaker()
		session.configure(bind=engine)
		Base.metadata.create_all(engine)
		s = session()
		Base.metadata.create_all(engine)
		jack = s.query(tables).get(data)
		s.delete(jack)
		s.commit()
		return True
#		except Exception as e:
#			return False

	def insert_db(self,new):
		try:
			Session = sessionmaker(bind=engine)
			session = Session()
			Base.metadata.create_all(engine)
			session.add(new)
			session.commit()
			return True
		except Exception as e:
			return False
