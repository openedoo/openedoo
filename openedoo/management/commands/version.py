from flask_script import Command, Option
import openedoo

class Version(Command):
    help_args = ('-h', '--help')
    help = "version Openedoo"
    def __init__(self):
        pass
    def run(self):
        print "openedoo v0.3"
        pass