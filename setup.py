
import sys
from distutils.sysconfig import get_python_lib
from setuptools import setup, find_packages

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
setup (
    name='Openedoo-cli',
    version='0.1',
    py_modules=['openedoo'],
    install_requires=[
	   'flask',
       'flask-script',
	],
    license='MIT',
    packages=find_packages(),
    package_dir={'openedoo':'openedoo'},
    include_package_data=True,
    scripts=['openedoo/bin/openedoo.py'],
    entry_points={'console_scripts': [
        'openedoo = openedoo.core.management:openedoo_cli',
    ]},
)
