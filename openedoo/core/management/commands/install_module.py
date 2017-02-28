from flask_script import Command, Option
from openedoo.core.libs.get_requirement import *
from delete_module import Delete
import sys
import time
import shutil
import threading
from waiting_animated import animated

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

    def _install_git(self,url,name):
        try:
            install_git_(url=url)
            return True
        except Exception as e:
            delete_module.delete_module(name)
            print e
            return False

    def _check_requirement(self,url,name):
        try:
            dependency_module = []
            data_requirement = open("modules/{direktory}/requirement.json".format(direktory=name),"r")
            requirement_json = json.loads(data_requirement.read())
            for dependency in requirement_json['requirement']:
                dependency_module.append(dependency)
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
                    return dependency_module
            except Exception as e:
                print "Error Writing __init__.py"
        except Exception as e:
            print e
            print "Module not found"
            delete_module.delete_module(name)
            del_manifest(name_module=name)

    def process(self,url):
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
            return False
        if self._install_git(url=url,name=name) is False:
            return "Failed install"
        else:
            dependency = self._check_requirement(url,name)
            try:
                for x in dependency:
                    print x['url']
                    self.process(x['url'])
            except:
                pass
                return "Error"

    def animated(self):
        animated()

    def worker(self,url):
        self.process(url)

    def run(self,url):
        words = url.split('/')
        if '.' in words[-1]:
            word = words[-1].split('.')
            name = word[0]
        else:
            name = words[-1]
        print "installing {name}".format(name=name)
        t = threading.Thread(name='animated', target=self.animated())
        w = threading.Thread(name='worker', target=self.worker(url=url))
        w.start()
        t.start()

