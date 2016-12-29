from openedoo.core.libs import blueprint, render_template, response, request, abort
import json

core = blueprint('newbot_member', __name__)

import json

@core.route('/')
def newbot():
	default_route = {'name' : "openedoo",'version': "0.1.0",'wiki': "https://github.com/openedoo/openedoo/wiki"}
	data = json.dumps(default_route)
	resp = response(data, status=200, mimetype='application/json')
	return resp
