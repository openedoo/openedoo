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


manager = Manager(app)

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')
def delete_module(name):
    file = open("{direktory}/route.py".format(direktory=BASE),"r+")
    readfile = file.readlines()
    file.seek(0)
    delete = ("\n \nfrom openedoo.{module} import {module}".format(module=name))
    for line in readfile:
        if str(name) not in line:
            file.writelines(line)
    file.truncate()
    file.close()
    shutil.rmtree('{dir_file}/modules/{name}'.format(dir_file=BASE_DIR,name=name))
def migrate():
    #query.drop_table('alembic_version')
    query().create_database(config.database_name)
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

def requirements(dir, file):
    try:
        import os
        name=os.path.splitext(file)[0]
        print file
        print a
        with open(os.path.join(dir, str(file)), "a") as f:
            f.write('{\
                \n\t"name":"{module_name}}",\
                \n\t"version":"0.0.1",\
                \n\t"requirement":"openedoo_core",\
                \n\t"pip_library":[],\
                \n"comment":"Comment Here .. ",\
                \n"type":"end_point",\
                \n"url_endpoint":"/{module_name}}"\
            \n}'.format(module_name=a))
            f.close()
    except Exception as e:
        raise "error creating "+name

@manager.command
def create(name):
    """Create your app module"""
    if os.path.isfile('modules/__init__.py') is False:
        os.mkdir('modules')
        open(os.path.join('modules', '__init__.py'), "a")
    dir = os.path.join('modules', str("{}".format(name)))
    try:
        os.mkdir(dir)
        try:
            with open(os.path.join(BASE, "route.py"), "a") as f:
                f.write("\n \nfrom modules.{module} import {module}".format(module=name))
                f.write("\napp.register_blueprint({modulename}, url_prefix='/{modulename}')".format(modulename=name))
                f.close()
                print("/route.py edited")

            with open(os.path.join(dir, "requirements.py"), "a") as f:
                f.write('{')
                f.write('\n\t"name":"{}",'.format(name))
                f.write('\n\t"version":"0.0.1",')
                f.write('\n\t"requirement":"openedoo_core",')
                f.write('\n\t"pip_library":[],')
                f.write('\n\t"comment":"Comment Here..",')
                f.write('\n\t"type":"end_point",')
                f.write('\n\t"url_endpoint":"/'+name+'",')
                f.write('\n}')
                f.write('\n')
                f.close()
                print(name+"/requirements.py created")
        except Exception as e:
            print e
            print "Error Writing __init__.py"

        try:
            add_version(name_module=name,version_modul='0.1')
            file(dir, file="__init__.py", apps=name)
            print(name+'/__init__.py created')
            print "...... Successfully created app {}.......".format(name)
        except Exception as e:
            print "error write "+e
    except BaseException as e:
        print e
        print "error >> \"{} is Exist\"".format(name)
        sys.exit(0)

@manager.command
def remove(name):
    """Delete your app module"""
    if os.path.exists('modules/{name}'.format(name=name))==False:
        return "module not found"
    try:
        delete_module(name)
        del_version(name)
        print "{name} has deleted".format(name=name)
    except Exception as e:
        print "module has deleted"

@manager.command
def run():
    """ run server with wekezeug """
    app.run(
        host='0.0.0.0',
        port=5000
    )


@manager.command
def check():
    """ Check Module Available """

    list_module = check_modul_available()
    print "Module Available : "
    for available in list_module:
        print available['name'] +" : "+ available['url_git']


@manager.command
def install(url):
    """ Install module from your git """
    try:
        if os.path.isfile('modules/__init__.py') is False:
            os.mkdir('modules')
            open(os.path.join('modules', '__init__.py'), "a")

        words = url.split('/')
        if '.' in words[-1]:
            word = words[-1].split('.')
            name = word[0]
        else:
            name = words[-1]

        if os.path.exists('modules/{name}'.format(name=name)):
            return "module exist"

        install_git_(url=url)

        print "Module installed"
        time.sleep(0.2)
        data_requirement = open("modules/{direktory}/requirement.json".format(direktory=name),"r")
        requirement_json = json.loads(data_requirement.read())
        add_version(name_module=requirement_json['name'],version_modul=requirement_json['version'],url=url)
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
def installed():
    """print all modul has installed"""
    data = open("manifest.json","r")
    data_json  = json.loads(data.read())
    if data_json['installed_module'] == []:
        return "no module hasn't installed"
    for available in data_json['installed_module']:
        print available['name_module']
@manager.command
def test():
    """unit_testing"""
    print "no problemo"
    pass

def main():
    manager.run()
