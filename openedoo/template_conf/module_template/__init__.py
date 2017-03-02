from openedoo.core.libs import Blueprint

%(app_name)s = Blueprint('%(app_name)s', __name__)

@%(app_name)s.route('/', methods=['POST', 'GET'])
def index():
	return "Hello module %(app_name)s"
