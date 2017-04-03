#!/bin/python

import os
import sys
from flask_script import Server, Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from openedoo.core.db import Query
from openedoo import db,app
from openedoo import config
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
from commands.version import Version
from commands.testing_openedoo import Testing
from commands.create_module_app import CreateModule
from openedoo import config

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
#manager.add_command('create', CreateModule())

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
    od.add_command('version', Version())
    od.add_command('test', Version())

    def execute(self):
        od.run()

def execute_cli():
    manage = Management()
    #manage = OpenedooCli()
    manage.execute()

def openedoo_cli():
    manage = OpenedooCli()
    manage.execute()
