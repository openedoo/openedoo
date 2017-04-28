#!/usr/bin/env python
# -*- coding: latin1 -*-


from sqlalchemy import *
import json

##table declaration
from openedoo_project import config

config_uri = config.DB_URI
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)
database_name = config.database_name

import decimal, datetime

def alchemyencoder(obj):
    """JSON encoder function for SQLAlchemy special classes."""
    if isinstance(obj, datetime.datetime):
        return obj.isoformat()
    elif isinstance(obj, decimal.Decimal):
        return float(obj)

def query(query):
    """output json """
    connection = engine.connect()
    res = connection.execute(query)

    # use special handler for dates and decimals
    return json.dumps([dict(r) for r in res], default=alchemyencoder,encoding='latin-1  ')