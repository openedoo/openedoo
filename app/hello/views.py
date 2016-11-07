from flask import Blueprint, render_template
from flask import request
from flask import Response
import json

hello = Blueprint('hello', __name__)


@hello.route('/', methods=['POST', 'GET'])
def index():
    return "Hello Hello Hello"

@hello.route('/add/', methods=['POST', 'GET'])
def add():
    if request.method == 'POST':
        loadjson = request.get_json(force=False)

        name = loadjson['name']
        dumpjson = json.dumps(loadjson)
        response = Response(dumpjson, status=201, mimetype='application/json')
        return response
    else:
        return "Coba"
