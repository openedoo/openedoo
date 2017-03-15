from flask_script import Command, Option
from openedoo.core.libs.get_requirement import *
import sys
import time
import shutil

class Update(Command):

    help_args = ('-h', '--help')
    help = "Update your module app"

    option_list = (
        Option("-n","--name", required=True, dest='name', help='module name'),
    )
    def run(self, name):
        try:
            directory = ('modules/{name}/'.format(name=name))
            git_update = git.cmd.Git(directory)
            print git_update.pull()
            #print "your update successfully"
        except Exception as e:
            print e
            return e
