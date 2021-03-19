from flask import Blueprint, request
from .urls import urls

blueprint_app = Blueprint("user", __name__, url_prefix="/api/user")

for url, view_func, methods in urls:
    blueprint_app.add_url_rule(url, view_func=view_func, methods=methods)
