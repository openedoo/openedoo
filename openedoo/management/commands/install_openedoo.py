from flask_script import Command, Option
import os
import re
import openedoo

class Install(Command):
    help_args = ('-h', '--help')
    help = "Create Project Openedoo"

    def __init__(self):
        pass
    def run(self):
        """Create your project with openedoo"""

        name = 'openedoo_project'

        directory = os.path.join(os.getcwd(), name)
        if os.path.isdir(directory) is False:
            tmp_path = None
            template_path = self.get_tmp(tmp_path=tmp_path)
            prefix_length = len(template_path) + 1
            print template_path

            print "create project [%s] in directory: %s" % (name, directory)

            for root, dirs, files in os.walk(template_path):
                #make dir
                path_rest = root[prefix_length:]
                root_reset = path_rest.replace("project_template", name)
                root_reset = root_reset.replace("project_name", name)
                dir_path = os.path.join(directory, root_reset)


                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)

                for filename in files:
                    if filename.endswith(('pyo', '.pyc', '.py.class')):
                        continue

                    # read template

                    tmp_path = os.path.join(root, filename)

                    with open(tmp_path, 'rb') as tmp_file:
                        content = tmp_file.read()
                        content = re.sub(r"%(?!\(\w+\)s)", "%%", content)
                        content %= {"project_name":name}

                    #write to directory
                    dest_path = os.path.join(dir_path, filename.replace("project_name", name))
                    with open(dest_path, 'wb') as new_file:
                        new_file.write(content)
        else:
            print ""
            print "Error :"
            print ">> \"Error when creating project\""
            print ">> \"{} is exist\"".format(name)
            print ""

    def get_tmp(self, tmp_path):
        if tmp_path is None:
            return os.path.join(openedoo.__path__[0], "template_conf",  "project_template")
        raise Exception("error in template: " + tmp_path)
