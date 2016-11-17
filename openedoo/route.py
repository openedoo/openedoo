from openedoo import app

from openedoo.module_hello import hello
app.register_blueprint(hello, url_prefix='/hello')
