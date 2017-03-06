from openedoo.core.libs.get_modul import *
from openedoo.core.management.commands.create_module_app import get_root_project

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = BASE = os.path.join(BASE_DIR, get_root_project())

def database_table(module_name=None):
	if module_name is None:
		return "please insert name module"
	try:
		get_information = find_modul(module_name)
		get_information = get_information['requirement']
		if get_information['database'] == "" and "None":
			return "database not found"
		if '.' in get_information['database']:
			database_name = get_information['database'].split('.')
		else:
			database_name = get_information['database']
		with open(os.path.join(BASE, "tables.py"), "a") as f:
			f.write("\n \nfrom modules.{module} import {database_name}".format(module=get_information['name'],database_name=database_name[0]))
			f.close()
		return "database inserted"
	except Exception as e:
		print e
		return "module doesn't have database"

def get_database(module_name=None):
	get_information = find_modul(module_name)
	return get_information['requirement']
