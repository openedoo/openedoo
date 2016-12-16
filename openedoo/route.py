from openedoo import app

from openedoo.module_member import member
app.register_blueprint(member, url_prefix='/beta/member')

from openedoo.core import core
app.register_blueprint(core, url_prefix='/')

from openedoo.module_tryout import tryout
app.register_blueprint(tryout, url_prefix='/tryout')

 








