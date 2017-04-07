from sqlalchemy import *
from sqlalchemy.orm import relationship, backref,create_session,Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import json
from datetime import datetime, date

##table declaration
from openedoo import config

class Query(object):
	def __init__(self,SQLALCHEMY_DATABASE_URI=None,database_name=None,db_uri=None):
		#SQLALCHEMY_DATABASE_URI = sql_uri
		#self.config_uri = db_uri
		#self.engine = create_engine(SQLALCHEMY_DATABASE_URI)
		#self.database_name = database_name
		config_uri = config.DB_URI
		self.engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
		self.database_name = config.database_name
		self.Base = declarative_base()
		self.metadata = MetaData(bind=self.engine)
		self.auto_map = automap_base()

	def select_db(self,tables,column,page=0,page_size=None,**value_column):
		'''equvalent with select * from tables where column = value_column, this didn't support with order by or join table'''
		try:
			session = sessionmaker()
			session.configure(bind=self.engine)
	 		self.Base.metadata.create_all(self.engine)
			s = session()
			if ('value' in value_column):
				kueridb = s.query(tables).filter(column == value_column['value'])
			else:
				kueridb = s.query(tables)
			if page_size != None:
				kueridb = kueridb.limit(page_size)
			if page != 0:
				kueridb = kueridb.offset(page*page_size)
			list1 = list(s.execute(kueridb))
			engine.dispose()
			return list1
		except Exception as e:
			return False

	def update_db(self,tables,column,value_column,dict_update):
		'''for update row in tables'''
		#namatable = namatable
		session = sessionmaker()
		session.configure(bind=self.engine)
 		self.Base.metadata.create_all(self.engine)
		s = session()
		try:
			s.query(tables).filter(column==value_column).update(dict_update)
			s.commit()
			self.engine.dispose()
			return True
		except Exception as e:
			return e
	def delete_db(self,tables,data):
		try:
			session = sessionmaker()
			session.configure(bind=self.engine)
			self.Base.metadata.create_all(self.engine)
			s = session()
			self.Base.metadata.create_all(self.engine)
			jack = s.query(tables).get(data)
			s.delete(jack)
			s.commit()
			self.engine.dispose()
			return True
		except Exception as e:
			return False

	def insert_db(self,new):
		try:
			Session = sessionmaker(bind=self.engine)
			session = Session()
			self.Base.metadata.create_all(self.engine)
			session.add(new)
			session.commit()
			self.engine.dispose()
			return True
		except Exception as e:
			return False
	def create_database(self,database_name):
		try:
			engine_new = create_engine(self.config_uri)
			connection_engine = engine_new.connect()
			connection_engine.execute("commit")
			connection_engine.execute("create database {database}".format(database=database_name))
			connection_engine.close()
			return True
		except Exception as e:
			message = {'message':'database exist'}
			return message
	def drop_table(self,name_table):
		sql = text('DROP TABLE IF EXISTS {name_table};'.format(name_table=name_table))
		result = self.engine.execute(sql)
		return result
	def version(self):
		query = 'SELECT VERSION()'
		connection = create_engine(config_uri).connect()
		result = connection.execute(query)
		data = []
		for value in result:
			row = dict(value)
			data.append(row)
		return data
	def raw(self,query=None):
		if query == None:
			return "query syntax is None"
		connection = create_engine(config_uri).connect()
		result = connection.execute(query)
		try:
			data = []
			for value in result:
				row = dict(value)
				data.append(row)
			return data
		except:
			return {'query':'database has change'}