
from flask import Blueprint, render_template
import json
from flask import jsonify, abort, Flask, g, request, Response

core = Blueprint('newbot_member', __name__)

from flask import jsonify, abort, Flask, g, request, Response
import json

@core.route('/')
def newbot():
	return "hello world"
