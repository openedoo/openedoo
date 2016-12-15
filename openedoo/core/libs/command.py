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

query = query()

manager = Manager(app)

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

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
    dir = os.path.join(BASE, str("module_{}".format(name)))
    try:
        os.mkdir(dir)
        try:
            with open(os.path.join(BASE, "route.py"), "a") as f:
                f.write("\n \nfrom openedoo.module_{modul} import {modul}".format(modul=name))
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

GITHUB_REPOS_API = 'https://api.github.com/repos/'

import base64
import json
import urllib2
import sys
import os

def write_file(item, dir_name):
    name = item['name']
    req = urllib2.Request(item['url'], headers={'User-Agent' : "Magic Browser"})
    res = urllib2.urlopen(req).read()
    coded_string = json.loads(res)['content']
    contents = base64.b64decode(coded_string)
    print os.path.join(dir_name, name)
    f = open(os.path.join(dir_name, name), 'w')
    f.write(contents)
    f.close

def write_files(url, dir_name, recursive=True):
    print 'url', url
    os.makedirs(dir_name)
    github_dir = json.loads(urllib2.urlopen(url).read())
    for item in github_dir:
        if item['type'] == 'file':
            write_file(item, dir_name)
        elif item['type'] == 'dir':
            write_files(item['url'], dir_name=os.path.join(dir_name, item['name']))

@manager.command
def runserver():
    app.run(
        host='0.0.0.0',
        port=5000
    )


@manager.command
def checkmodule():
    """ Check Module Available """

    list_module = check_modul_available()
    print "Module Available : "
    for available in list_module:
        print available['name']

@manager.command
def install(name):
    """ Install modul """
    data = find_modul(modul_name=name)
    try:
        install_git(url=data['url_git'],name_modul=name)
        print "Modul installed"
    except Exception:
        print "Modul not found"


@manager.command
def test():
    print "no problemo"
    pass

def main():
    manager.run()
