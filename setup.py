from setuptools import setup, find_packages
import os
import sys
from distutils.sysconfig import get_python_lib

overlay_warning = False
if "install" in sys.argv:
    lib_paths = [get_python_lib()]
    if lib_paths[0].startswith("/usr/lib/"):
        # We have to try also with an explicit prefix of /usr/local in order to
        # catch Debian's custom user site-packages directory.
        lib_paths.append(get_python_lib(prefix="/usr/local"))
    for lib_path in lib_paths:
        existing_path = os.path.abspath(os.path.join(lib_path, "openedoo"))
        if os.path.exists(existing_path):
            # We note the need for the warning here, but present it after the
            # command is run, so it's more likely to be seen.
            overlay_warning = True
            break

EXCLUDE_FROM_PACKAGES = ['openedoo.template_conf.project_template',
                         'openedoo.template_conf.module_template',
                         'openedoo.bin']

setup (
    name='openedoo',
    version='1.1.0.19',
    url='http://openedoo.org',
    author='Openedoo Official',
    license='MIT',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    description=('openedoo is backend service for education base on flask'),
    long_description = open('README.rst').read(),
    include_package_data=True,
    scripts=['openedoo/bin/openedoo-cli.py'],
    entry_points={'console_scripts': [
        'openedoo = openedoo.core.management:openedoo_cli',
    ]},
    install_requires=[
	   'flask',
       'flask-script',
       'sqlalchemy',
       'MySQL-python',
       'redis',
       'Werkzeug',
       'itsdangerous',
       'click',
       'Jinja2',
       'alembic',
       'flask-migrate',
       'Flask-Script',
       'GitPython',
       'gitdb2',
       'smmap2',
       'pyserial'
	],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)

if overlay_warning:
    sys.stderr.write("""
========
WARNING!
========
You have just installed Openedoo over top of an existing
installation, without removing it first. Because of this,
your install may now include extraneous files from a
previous version that have since been removed from
Django. This is known to cause a variety of problems. You
should manually remove the
%(existing_path)s
directory and re-install Openedoo.
""" % {"existing_path": existing_path})
