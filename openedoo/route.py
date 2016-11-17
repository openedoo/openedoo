from openedoo import app

from .hello import hello
app.register_blueprint(hello, url_prefix='/hello')