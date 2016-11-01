
from flask import Blueprint, render_template
device = Blueprint('newbotbaru', __name__)

from app.model.auth import token_auth

@device.route('/')
@token_auth
def newbot():
	return "rendi"


@device.route('/add')
@token_auth
def add_device():
	return "rendi"

@device.route('/edit')
def edit_device():
	return "rendi"

@device.route('/delete')
def delete_device():
	return "rendi"

@device.route('/list')
def list_device():
	return "rendi"