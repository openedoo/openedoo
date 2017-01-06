from openedoo.core.libs.get_modul import *

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

def database_table(module_name=None):
	if module_name is None:
		return "please insert name module"
	get_information = find_modul(module_name)
	get_information = get_information['requirement']
	#return get_information
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

def get_database():
	get_information = find_modul("module_member")

	return get_information['requirement']