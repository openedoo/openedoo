#!/bin/python

import os
import sys
from flask_script import Server, Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from %(project_name)s.db import Query
from %(project_name)s import app,db
from %(project_name)s import config
import unittest
import json
from openedoo.core.libs.get_modul import *
import shutil
import time
import git
from openedoo.core.libs.get_requirement import *
from commands.module import Modules
from commands.gunicornserver import GunicornServer
from commands.install_openedoo import Install
from commands.create_module_app import CreateModule

query = Query()

#manager = Manager(app, usage="Openedoo Command Line", with_default_commands=False)
manager = Manager(app, usage="Openedoo Command Line", with_default_commands=False)
od = Manager(app, usage="Openedoo Command Line", with_default_commands=False)
manager.help_args = ('-?', '--help')
manager.add_command('run', Server())
manager.add_command('shell', Shell())
manager.add_command('db', MigrateCommand)
manager.add_command('gunicornserver', GunicornServer())
manager.add_command('module', Modules.module)

class Management(object):
    @manager.command
    def test():
        """unit_testing"""
        print "no problemo"
        pass

    def execute(self):
        manager.run()
    def migrate():
        #query.drop_table('alembic_version')
        query.create_database(config.database_name)
        migrate = Migrate(app, db)
        return migrate

    migrate = migrate()


class OpenedooCli(object):
    od.help_args = ('-?', '--help')
    od.add_command('install', Install())

    def execute(self):
        od.run()
        
def execute_cli():
    manage = Management()
    manage.execute()
def openedoo_cli():
    manage = OpenedooCli()
    manage.execute()
