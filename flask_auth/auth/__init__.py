from flask import Blueprint

auth = Blueprint("auth", __name__)

from flask_auth.auth import controller
