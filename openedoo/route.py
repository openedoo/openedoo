from openedoo import app

from openedoo.core import core
app.register_blueprint(core, url_prefix='/')
