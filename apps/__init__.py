from flask import Flask

from db import init_db
from contrib.registers import *


def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object('config.Config')

    db = init_db(app)

    register_blueprints(app)
    register_extensions(app)
    register_error_handler(app)

    return app

