from flask import Blueprint
from .urls import urls

blueprint_app = Blueprint("sample", __name__, url_prefix="/")

for url, view_func, methods in urls:
    blueprint_app.add_url_rule(url, view_func=view_func, methods=methods)