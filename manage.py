#!/bin/python

import os
import sys
from manager import Manager

manager = Manager()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))
BASE = os.path.join(BASE_DIR, 'app')

def file(dir, name):
    try:
        file = open(os.path.join(dir, name), "a")
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
                f.write("\n \n from app.{modul}.{modul} import {modul}".format(modul=name))
                f.write("\n app.register_blueprint({modulename}, url_prefix='/{modulename}')".format(modulename=name))
                f.close()
        except Exception as e:
            print "Error Writing __init__.py"

        try:
            file(dir, "__init__.py")
            file(dir, str("{0}.py".format(name)))

            print "...... Successfully created app ......."+name
        except Exception as e:
            print "error write "+e
    except BaseException:
        print "error >> \"App is Exist\""
        sys.exit(0)

@manager.command
def runserver():
    """Run your app"""
    from app import app
    app.debug = True
    app.run(host='0.0.0.0', port=9888)

@manager.command
def migrate():
    """Migrate your database"""

    from flask.ext.script import Manager
    from flask.ext.migrate import Migrate, MigrateCommand
    from app import app
    from app.core.libs.db.db_query import Base

    migrate = Migrate(app, Base)

    manager = Manager(app)
    manager.add_command('dbase', MigrateCommand)

if __name__ == '__main__':
    manager.main()
