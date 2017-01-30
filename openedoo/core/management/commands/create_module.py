from flask_script import Manager, Command, Option
from openedoo.core.libs.get_requirement import *
import time
import sys

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

class Create(Command):
    help_args = ('-h', '--help')
    help = "Create Module"
    option_list = (
        Option("-r","--remote", dest='remote_git', help='remote git url'),
        Option("-n","--name", required=True, dest='name', help='module name')
    )
    def create_file_init(self,dir=None, file=None, apps=None):
        try:
            with open(os.path.join(dir, file), "a") as f:
                f.write("from openedoo.core.libs import blueprint\n\n{dir} = blueprint('{dir}', __name__)\n\n".format(dir=apps))
                f.write("@{}.route('/', methods=['POST', 'GET'])".format(apps))
                f.write("\ndef index():\n\treturn \"Hello World\"")
                f.close()
        except Exception as e:
            raise "error creating "+name

    def run(self,name=None, remote_git=None):
        """Create your app module"""
        if os.path.isfile('modules/__init__.py') is False:
            os.mkdir('modules')
            open(os.path.join('modules', '__init__.py'), "a")
        dir = os.path.join('modules', str("{}".format(name)))
        try:
            os.mkdir(dir)
            try:
                with open(os.path.join(BASE, "route.py"), "a") as f:
                    f.write("\n \nfrom modules.{module} import {module}".format(module=name))
                    f.write("\napp.register_blueprint({modulename}, url_prefix='/{modulename}')".format(modulename=name))
                    f.close()
                    print("/route.py edited")
                time.sleep(0.2)
                create_requirement(name_module=name,url_endpoint="/{name}".format(name=name))

            except Exception as e:
                print e
                print "Error Writing __init__.py"

            try:
                add_manifest(name_module=name,version_modul='0.1')
                self.create_file_init(dir, file="__init__.py", apps=name)
                print(name+'/__init__.py created')

                if remote_git is not None:
                    repo = git.Repo.init(dir)
                    origin = repo.create_remote('origin', remote_git)
                    origin.fetch()
                    print "... Git init finished ..."
                    print "... Git remote finished ..."
                else:
                    git.Repo.init(dir)
                    print "... Git init finished ..."
                print "...... Successfully created app {}.......".format(name)
            except Exception as e:
                print "error write "+e
        except BaseException as e:
            print e
            print "error >> \"{} is Exist\"".format(name)
            sys.exit(0)
