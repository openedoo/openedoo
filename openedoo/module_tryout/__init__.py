from openedoo.core.libs import blueprint
import json
import module_tryout

tryout = blueprint('tryout', __name__)

@tryout.route('/', methods=['POST', 'GET'])
def index():
	return "Hello World"