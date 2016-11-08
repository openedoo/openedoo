from sqlalchemy import *
from sqlalchemy.orm import relationship, backref,create_session,Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker
import json
from datetime import datetime, date
import datetime


##table declaration
from db_tables import od_session, od_users

engine = create_engine('mysql://root:aris1996@localhost:3306/openedoo')
Base = declarative_base()
metadata = MetaData(bind=engine)
auto_map = automap_base()


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
		Session = sessionmaker(bind=engine)
		session = Session()
		Base.metadata.create_all(engine)
		session.add(new)
		session.commit()

	except Exception as e:
		print e

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

#print Base.metadata.create_all(engine)
