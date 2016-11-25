from openedoo import app

from openedoo.module_member import member
app.register_blueprint(member)

from openedoo.core import core
app.register_blueprint(core, url_prefix='/')
