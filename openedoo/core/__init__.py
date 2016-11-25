from openedoo.core.libs import blueprint, render_template, response, request, abort
import json

core = blueprint('newbot_member', __name__)

from flask import jsonify, abort, Flask, g, request, Response
import json

@core.route('/')
def newbot():
	return "cumming soon"
