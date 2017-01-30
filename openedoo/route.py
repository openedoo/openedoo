from openedoo import app

from openedoo.core import core
app.register_blueprint(core, url_prefix='/')

from modules.module_member import module_member
app.register_blueprint(module_member, url_prefix='/member')