from flask_script import Command, Option
import os
import re
import openedoo
import git
import time
from openedoo.core.libs.get_modul import create_requirement
import json

DIR = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
od_packages = os.path.join(DIR, 'od_packages.json')

def get_root_project():
    try:
        with open('od_packages.json') as data_file:
            data_json = json.loads(data_file.read())
        return data_json['project_root']
    except Exception as e:
        return 'openedoo'

class CreateModule(Command):
    help_args = ('-h', '--help')
    help = "Create Module App"

    option_list = (
        Option("-n", "--name", dest='name', help='project name', required=True),
        Option("-r","--remote", dest='remote_git', help='remote git url')
    )

    def __init__(self):
        pass

    def get_module_name(self):
        return "modules"

    def get_base_path(self):
        BASE_DIR = os.path.dirname(os.path.realpath(__name__))
        BASE = os.path.join(BASE_DIR, get_root_project())
        return BASE

    def add_route(self, name):
        try:
            with open(os.path.join(self.get_base_path(), "route.py"), "a") as f:
                f.write("\n \nfrom modules.{module} import {module}".format(module=name))
                f.write("\napp.register_blueprint({modulename}, url_prefix='/{modulename}')".format(modulename=name))
                f.close()
                print("/route.py edited")
            time.sleep(0.2)
            create_requirement(name_module=name,url_endpoint="/{name}".format(name=name))
        except Exception as e:
            print e
            print "Error Writing route.py"

    def git_init(self, dir):
        git.Repo.init(dir)
        print "... Git init finished ..."

    def git_remote(self, dir, remote_git):
        repo = git.Repo.init(dir)
        origin = repo.create_remote('origin', remote_git)
        origin.fetch()
        print "... Git init finished ..."
        print "... Git remote finished ..."

    def run(self, name=None, remote_git=None):
        """ Create Module App with Openedoo """

        if not os.path.isfile(os.path.join(self.get_module_name(), '__init__.py')):
            os.mkdir(self.get_module_name())
            files = open(os.path.join(self.get_module_name(), '__init__.py'), "a")
            files.close()

        directory = os.path.join(self.get_module_name(), name)

        if os.path.isdir(directory):
            return "Modules is exists"

        tmp_path = None
        template_path = self.get_tmp(tmp_path=tmp_path)
        prefix_length = len(template_path) + 1
        print template_path

        print "create module [%s] in directory: %s" % (name, directory)

        for root, dirs, files in os.walk(template_path):
            #make_dir
            path_rest = root[prefix_length:]
            root_reset = path_rest.replace("module_template", name)
            dir_path = os.path.join(directory, root_reset)

            print dir_path
            if not os.path.exists(dir_path):
                os.mkdir(dir_path)

            for filename in files:
                if filename.endswith(('pyo','swp','.py.class')):
                    continue

                tmp_path = os.path.join(root, filename)
                print "creating " + tmp_path

                with open(tmp_path, 'rb') as tmp_file:
                    content = tmp_file.read()
                    content = re.sub(r"%(?!\(\w+\)s)","%%", content)
                    content %= {"app_name":name}

                dest_path = os.path.join(dir_path, filename.replace("app_name", name))
                with open(dest_path, 'wb') as new_file:
                    new_file.write(content)

        #Add routing
        self.add_route(name=name)

        #git init and remote_git
        if remote_git is None:
            self.git_init(dir=directory)
        else:
            self.git_remote(dir=directory, remote_git=remote_git)

        print "Successfully created module app {}".format(name)

    def get_tmp(self, tmp_path):
        if tmp_path is None:
            return os.path.join(openedoo.__path__[0], "template_conf",  "module_template")
        raise Exception("error in template: " + tmp_path)
