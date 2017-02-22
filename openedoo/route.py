from openedoo import app
from openedoo.core import core




from modules.a import a
app.register_blueprint(a, url_prefix='/a')
