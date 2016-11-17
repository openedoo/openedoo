from openedoo.core.libs import blueprint

coba = blueprint('coba', __name__)

@coba.route('/', methods=['POST', 'GET'])
def index():
	return "Hello World"