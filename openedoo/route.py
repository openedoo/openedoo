from openedoo import app
from openedoo.core import core

 
from modules.test import test
app.register_blueprint(test, url_prefix='/test')