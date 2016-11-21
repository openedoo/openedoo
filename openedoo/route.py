from openedoo import app

from openedoo.module_member import member
app.register_blueprint(member, url_prefix='/beta/member')
