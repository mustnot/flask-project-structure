from flask import request, jsonify

from .models import User, UserManager


def index():
    return "this is user app index enpoint"


def signup():
    user_data = UserManager(**request.form)

    user = User(**user_data.dict())
    user.set_password(user_data.form.get("password", ""))
    user.create()

    return jsonify(user_data.dict(exclude={"password"})), 201
