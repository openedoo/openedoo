from flask_script import Command, Option
from openedoo.core.libs.get_requirement import *
from delete_module import Delete
import sys
import time
import shutil

delete_module = Delete()
BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

class Install(Command):

    help_args = ('-h', '--help')
    help = "Install Module from git"

    def __init__(self, default_url=None):
        self.default_url=default_url

    def get_options(self):
        return [
            Option(dest='url', default=self.default_url),
        ]

    def run(self, url):
        try:
            if os.path.isfile('modules/__init__.py') is False:
                os.mkdir('modules')
                open(os.path.join('modules', '__init__.py'), "a")

            words = url.split('/')
            if '.' in words[-1]:
                word = words[-1].split('.')
                name = word[0]
            else:
                name = words[-1]

            if os.path.exists('modules/{name}'.format(name=name)):
                return "module exist"

            install_git_(url=url)

            print name
            time.sleep(0.2)
            print database_table(module_name=name)

            data_requirement = open("modules/{direktory}/requirement.json".format(direktory=name),"r")
            requirement_json = json.loads(data_requirement.read())
            add_manifest(name_module=requirement_json['name'],version_modul=requirement_json['version'],url=url)
            try:
                with open(os.path.join(BASE, "route.py"), "a") as f:
                    f.write("\nfrom modules.{module_folder} import {module}".format(\
                        module_folder=requirement_json['name'],\
                        module=name))
                    f.write("\napp.register_blueprint({modulename}, url_prefix='{url_endpoint}')".format(\
                        modulename=requirement_json['name'],\
                        url_endpoint=requirement_json['url_endpoint']))
                    f.close()
                    print "Module installed"
            except Exception as e:
                print "Error Writing __init__.py"
        except Exception as e:
            print e
            print "Module not found"
            #a = Module()
            delete_module.delete_module(name)
            del_manifest(name_module=name)
