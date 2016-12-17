#!/bin/python

import os
import sys
from flask_script import Server, Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from openedoo.core.db.db_tables import Base
from openedoo.core.db import query
from openedoo import app
from openedoo import config
import unittest
import json
from openedoo.core.libs.get_modul import *
import shutil
import time

query = query()

manager = Manager(app)

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')
def delete_module(name):
    file = open("{direktory}/route.py".format(direktory=BASE),"r+")
    readfile = file.readlines()
    file.seek(0)
    delete = ("\n \nfrom openedoo.module_{module} import {module}".format(module=name))
    for line in readfile:
        if str(name) not in line:
            file.writelines(line)
    file.truncate()
    file.close()
    shutil.rmtree('{dir_file}/modules/{name}'.format(dir_file=BASE_DIR,name=name))
def migrate():
    #query.drop_table('alembic_version')
    query.create_database(config.database_name)
    migrate = Migrate(app, Base)
    return migrate

manager.add_command('shell', Shell())
migrate = migrate()
manager.add_command('db', MigrateCommand)

def file(dir, file, apps):
    try:
        with open(os.path.join(dir, file), "a") as f:
            f.write("from openedoo.core.libs import blueprint\n\n{dir} = blueprint('{dir}', __name__)\n\n".format(dir=apps))
            f.write("@{}.route('/', methods=['POST', 'GET'])".format(apps))
            f.write("\ndef index():\n\treturn \"Hello World\"")
            f.close()
    except Exception as e:
        raise "error creating "+name

@manager.command
def create(name):
    """Create your app module"""
    dir = os.path.join('modules', str("module_{}".format(name)))
    try:
        os.mkdir(dir)
        try:
            with open(os.path.join(BASE, "route.py"), "a") as f:
                f.write("\n \nfrom modules.module_{module} import {module}".format(module=name))
                f.write("\napp.register_blueprint({modulename}, url_prefix='/{modulename}')".format(modulename=name))
                f.close()
        except Exception as e:
            print "Error Writing __init__.py"

        try:
            file(dir, file="__init__.py", apps=name)
            print "...... Successfully created app {}.......".format(name)
        except Exception as e:
            print "error write "+e
    except BaseException:
        print "error >> \"{} is Exist\"".format(name)
        sys.exit(0)

@manager.command
def delete(name):
    """Delete your app module"""
    try:
        delete_module(name)
        del_version(name)
        print "{name} has deleted".format(name=name)
    except Exception as e:
        print "module has deleted"

@manager.command
def runserver():
    """ run server with wekezeug """
    app.run(
        host='0.0.0.0',
        port=5000
    )


@manager.command
def check_module():
    """ Check Module Available """

    list_module = check_modul_available()
    print "Module Available : "
    for available in list_module:
        print available['name']

@manager.command
def install(name):
    """ Install module """
    data = find_modul(modul_name=name)
    if os.path.exists('modules/{name}'.format(name=name)):
        return "module exist"
    try:
        install_git(url=data['url_git'],name_modul=name)
        if os.path.isfile('modules/__init__.py') is False:
            open(os.path.join('modules', '__init__.py'), "a")
        print "Module installed"
        add_version(name_module=data['requirement']['name'],version_modul=data['requirement']['version'])
        try:
            with open(os.path.join(BASE, "route.py"), "a") as f:
                f.write("\nfrom modules.{module} import {module}".format(module=data['requirement']['name']))
                f.write("\napp.register_blueprint({modulename}, url_prefix='{url_endpoint}')".format(modulename=data['requirement']['name'],url_endpoint=data['requirement']['url_endpoint']))
                f.close()
        except Exception as e:
            print "Error Writing __init__.py"
    except Exception as e:
        print e
        print "Module not found"

@manager.command
def git(url,name):
    """ Install module from your git """
    if os.path.exists('modules/{name}'.format(name=name)):
        return "module exist"
    try:
        install_git(url=url,name_modul=name)
        if os.path.isfile('modules/__init__.py') is False:
            open(os.path.join('modules', '__init__.py'), "a")
        print "Module installed"
        time.sleep(0.2)
        data_requirement = open("modules/{direktory}/requirement.json".format(direktory=name),"r")
        requirement_json = json.loads(data_requirement.read())
        add_version(name_module=requirement_json['name'],version_modul=requirement_json['version'])
        try:
            with open(os.path.join(BASE, "route.py"), "a") as f:
                f.write("\nfrom modules.{module_folder} import {module}".format(\
                    module_folder=requirement_json['name'],\
                    module=name))
                f.write("\napp.register_blueprint({modulename}, url_prefix='{url_endpoint}')".format(\
                    modulename=requirement_json['name'],\
                    url_endpoint=requirement_json['url_endpoint']))
                f.close()
        except Exception as e:
            print "Error Writing __init__.py"
    except Exception as e:
        print e
        print "Module not found"

@manager.command
def modul_installed():
    data = open("version.json","r")
    data_json  = json.loads(data.read())
    if data_json['modul_installed'] == []:
        return "no modul hasn't installed"
    for available in data_json['modul_installed']:
        print available['name_module']
@manager.command
def test():
    print "no problemo"
    pass

def main():
    manager.run()
