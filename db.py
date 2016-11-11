"""Migrate your database"""

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from openedoo import app
from openedoo.core.libs.db.db_tables import Base

migrate = Migrate(app, Base)
manager = Manager(app)
manager.add_command('dbase', MigrateCommand)

if __name__ == '__main__':
    manager.run()
