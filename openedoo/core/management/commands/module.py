from flask_script import Manager, Command
from openedoo.core.libs.get_requirement import *
import sys
import time
import shutil

BASE_DIR = os.path.dirname(os.path.realpath(__name__))
BASE = os.path.join(BASE_DIR, 'openedoo')

def create_file_init(dir=None, file=None, apps=None):
    try:
        with open(os.path.join(dir, file), "a") as f:
            f.write("from openedoo.core.libs import blueprint\n\n{dir} = blueprint('{dir}', __name__)\n\n".format(dir=apps))
            f.write("@{}.route('/', methods=['POST', 'GET'])".format(apps))
            f.write("\ndef index():\n\treturn \"Hello World\"")
            f.close()
    except Exception as e:
        raise "error creating "+name

def delete_module(name):
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
    print name
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

class Modules(Command):

    module = Manager(usage="Manage application modules")

    @module.option("-n","--name", required=True, dest='name', help='module name')
    def update(name=None):
        if name == None:
            return "please insert name modules"
        try:
            direktory = ('modules/{name}/'.format(name=name))
            git_update = git.cmd.Git(direktory)
            print git_update.pull()
        except Exception as e:
            return e

    @module.command
    def available():
        """ Check Module Available """

        list_module = check_modul_available()
        print "Module Available : "
        for available in list_module:
            print available['name'] +" : "+ available['url_git']

    @module.command
    def installed():
        """print all modul has installed"""
        data = open("manifest.json","r")
        #print database_table("module_member")
        data_json  = json.loads(data.read())
        if data_json['installed_module'] == []:
            return "no module hasn't installed"
        for available in data_json['installed_module']:
            print available['name_module']

    @module.option("-r","--remote", dest='remote_git', help='remote git url')
    @module.option("-n","--name", required=True, dest='name', help='module name')
    def create(name=None, remote_git=None):
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
                create_file_init(dir, file="__init__.py", apps=name)
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

    @module.command
    def install(url):
        """ Install module from your git """
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
            delete_module(name)
            del_manifest(name_module=name)

    @module.command
    def remove(name):
        """Delete your app module"""
        if os.path.exists('modules/{name}'.format(name=name))==False:
            return "module not found"
        try:
            delete_module(name)
            del_manifest(name_module=name)
            print "{name} has deleted".format(name=name)
        except Exception as e:
            print "module has deleted"
