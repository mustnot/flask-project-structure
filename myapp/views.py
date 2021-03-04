from .models import User

from flask import request, jsonify


def index():
    return "This is Sample Blueprint Index Function"


def login():
    user = User(**request.form)
    return jsonify(user.dict())