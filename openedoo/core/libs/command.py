#!/bin/python

import os
import sys
from flask_script import Server, Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from openedoo import app
from openedoo.core.db.db_tables import Base

manager = Manager(app)

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

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

@manager.command
def runserver():
    app.run(
        host='0.0.0.0',
        port=5000
    )
manager.add_command('shell', Shell())
migrate = Migrate(app, Base)
manager.add_command('db', MigrateCommand)


def main():
    manager.run()
