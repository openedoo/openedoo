#!/bin/python

import os
import sys
from manager import Manager

manager = Manager()

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

def file(dir, name):
    try:
        with open(os.path.join(dir, name), "a") as f:
            dir_name = os.path.basename(os.path.normpath(dir))
            f.write("from flask import Blueprint\n\n{dir} = Blueprint('{dir}', __name__)\n\n".format(dir=dir_name))
            f.write("@{}.route('/', methods=['POST', 'GET'])".format(dir_name))
            f.write("\ndef index():\n\treturn \"Hello World\"")
            f.close()
    except Exception as e:
        raise "error creating "+name


@manager.command
def create(name):
    """Create your app module"""
    dir = os.path.join(BASE, str(name))
    try:
        os.mkdir(dir)
        try:
            with open(os.path.join(BASE, "__init__.py"), "a") as f:
                f.write("\n \nfrom openedoo.{modul} import {modul}".format(modul=name))
                f.write("\napp.register_blueprint({modulename}, url_prefix='/{modulename}')".format(modulename=name))
                f.close()
        except Exception as e:
            print "Error Writing __init__.py"

        try:
            file(dir, "__init__.py")
            print "...... Successfully created app {}.......".format(name)
        except Exception as e:
            print "error write "+e
    except BaseException:
        print "error >> \"{} is Exist\"".format(name)
        sys.exit(0)

@manager.command
def runserver():
    """Run your app"""
    from openedoo import app
    app.debug = True
    app.run(host='0.0.0.0', port=9888)

@manager.command
def migrate():
    """Migrate your database"""

    from flask.ext.script import Manager
    from flask.ext.migrate import Migrate, MigrateCommand
    from openedoo import app
    from openedoo.core.libs.db.db_query import Base

    migrate = Migrate(app, Base)

    manager = Manager(app)
    manager.add_command('dbase', MigrateCommand)


@manager.command
def test():
    from openedoo.core.libs import test
    print test.coba

def main():
    manager.main()

if __name__ == '__main__':
    manager.main()
