"""Migrate your database"""

from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from app import app
from app.core.libs.db.db_query import Base

migrate = Migrate(app, Base)
manager = Manager(app)
manager.add_command('dbase', MigrateCommand)

if __name__ == '__main__':
    manager.run()
