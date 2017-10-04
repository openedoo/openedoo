import unittest
from flask_script import Command, Option
from flask_script.commands import InvalidCommand


class UnitTest(Command):
    """Core Unittest Command to test Openedoo modules.

    Example test command for all module:
        $python manage.py module unittest -a

    Example test command for only one specific module:
        $python manage.py module unittest -n module_employee
    """
    help_args = ("-h", "-?", "--help")
    help = "Run python unittest for your Openedoo module."
    option_list = (
        Option("-n", "--name", dest="module_name", help="Test one Openedoo module that is specified by name"),
        Option("-a", "--all", dest="all", action="store_true", help="Test all installed Openedoo module at once")
    )

    def run(self, module_name=None, all=False):
        try:
            if not all and not module_name:
                raise InvalidCommand("At least one option is required.")
            test_loader = unittest.TestLoader()
            test_runner = unittest.TextTestRunner(verbosity=3)
            module = "modules"
            if all:
                tests = test_loader.discover(module)
                return test_runner.run(tests)
            tests = test_loader.discover(module+"."+module_name)
            return test_runner.run(tests)
        except Exception as e:
            print e
