
from setuptools import setup

setup (
    name='Openedoo-cli',
    version='0.1',
    py_modules=['openedoo'],
    install_requires=[
	   'flask',
       'flask-script',
	],
    scripts=['openedoo/bin/openedoo.py'],
    entry_points={'console_scripts': [
        'openedoo = openedoo.core.management:openedoo_cli',
    ]},
)
