from flask_script import Command, Option
import os
from openedoo.core.libs.get_requirement import *
import shutil

class Delete(Command):

    def __init__(self, default_name=None):
        self.default_name=default_name

    def get_options(self):
        return [
            Option(dest='name', default=self.default_name),
        ]

    def delete_module(self,name):
        try:
            file = open("{direktory}/route.py".format(direktory=BASE),"r+")
            readfile = file.readlines()
            file.seek(0)
            #delete = ("\n \nfrom openedoo.{module} import {module}".format(module=name))
            for line in readfile:
                if str(name) not in line:
                    file.writelines(line)
            file.truncate()
            file.close()
            print BASE_DIR
            shutil.rmtree('{dir_file}/modules/{name}'.format(dir_file=BASE_DIR,name=name))

            file = open("{direktory}/tables.py".format(direktory=BASE),"r+")
            readfile = file.readlines()
            file.seek(0)
            #delete = ("\n \nfrom openedoo.{module} import {module}".format(module=name))
            for line in readfile:
                if str(name) not in line:
                    file.writelines(line)
            file.truncate()
            file.close()
        except Exception as e:
            print e

    def run(self, name):
        """Delete your app module"""
        if os.path.exists('modules/{name}'.format(name=name))==False:
            return "module not found"

        self.delete_module(name)
        del_manifest(name_module=name)
        print "... {name} has deleted ...".format(name=name)
