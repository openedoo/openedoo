from flask_script import Manager, Command
from openedoo.core.libs.get_requirement import *
import sys
import time
import shutil
from delete_module import Delete
from create_module_app import CreateModule
from create_module import Create
from install_module import Install
from update_module import Update



class Modules(Command):
    module = Manager(usage="Manage application modules")

    module.add_command('remove', Delete())
    module.add_command('create', Create())
    module.add_command('install', Install())
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
