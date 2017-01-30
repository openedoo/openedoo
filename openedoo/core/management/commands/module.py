from flask_script import Manager, Command
from openedoo.core.libs.get_requirement import *
import sys
import time
import shutil

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

class Modules(Command):
    module = Manager(usage="Manage application modules")

    from delete_module import Delete
    module.add_command('remove', Delete())

    from create_module import Create
    module.add_command('create', Create())

    from install_module import Install
    module.add_command('install', Install())

    from update_module import Update
    module.add_command('update', Update())
    
    @module.command
    def available():
        """ Check Module Available """

        list_module = check_modul_available()
        print "Module Available : "
        for available in list_module:
            print available['name'] +" : "+ available['url_git']

    @module.command
    def installed():
        """print all modul has installed"""
        data = open("manifest.json","r")
        #print database_table("module_member")
        data_json  = json.loads(data.read())
        if data_json['installed_module'] == []:
            return "no module hasn't installed"
        for available in data_json['installed_module']:
            print available['name_module']
