from flask import Blueprint

queue = Blueprint("queue", __name__)

from flask_auth.queue import email
