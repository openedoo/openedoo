from datetime import datetime, timedelta
from openedoo.core.db import query
from openedoo.core.db.db_tables import od_tryout,od_users
from openedoo.core.libs.tools import *
from openedoo.core.libs.auth import *
import json
from email.utils import parseaddr
from functools import wraps
from openedoo.core.libs import session, Response
now_temp = datetime.now()
now = now_temp.strftime('%Y-%m-%d %H:%M:%S')

query = query()

def tryout_add(tryout_question,tryout_selection,tryout_answer,tryout_type,tryout_weight,tryout_attachment_information,tryout_attachment):
	tryout_selection = json.dumps(tryout_selection)
	if tryout_attachment != None:
		tryout_attachment = json.dumps(tryout_attachment)
	else:
		tryout_attachment = ""
	if tryout_attachment_information != None:
		tryout_attachment_information = json.dumps(tryout_attachment_information)
	else:
		tryout_attachment_information = "None"
	try:
		print tryout_attachment
		data = od_tryout(
					tryout_question=tryout_question,
					tryout_selection=tryout_selection,
					tryout_answer=tryout_answer,
					tryout_weight=tryout_weight,
					tryout_type=tryout_type,
					tryout_attachment=tryout_attachment,
					tryout_attachment_information=tryout_attachment_information
    	    		)
		query.insert_db(new=data)
		return True
	except Exception as e:
		print e
		return False