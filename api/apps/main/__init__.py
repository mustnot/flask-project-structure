from flask import Blueprint
from .urls import urls

main_app = Blueprint("main", __name__, url_prefix="/")

for url, view_func, methods in urls:
    main_app.add_url_rule(url, view_func=view_func, methods=methods)