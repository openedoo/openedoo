from flask_script import Command, Option
from openedoo import app

class GunicornServer(Command):
    help = "Start the Server with Gunicorn"

    option_list = (
        Option('-h', '--host', dest='host', default='127.0.0.1'),
        Option('-p', '--port', dest='port', type=int, default=5000),
        Option('-w', '--workers', dest='workers', type=int, default=3)
    )
    def run(self, host, port, workers):
        """Start the Server with Gunicorn"""
        from gunicorn.app.base import Application

        class FlaskApplication(Application):
            def init(self, parser, opts, args):
                return {
                    'bind': '{0}:{1}'.format(host, port),
                    'workers': workers
                }

            def load(self):
                return app

        application = FlaskApplication()
        return application.run()
