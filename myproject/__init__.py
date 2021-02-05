import os
from flask import Flask

from .contrib.register import *

def create_app() -> Flask:
    app = Flask(__name__)
    app.config.from_object(os.environ.get("PROJECT_CONFIG", "myproject.settings.DefaultConfig"))

    register_blueprints(app)
    register_extensions(app)
    register_error_handler(app)

    return app

if __name__ == "__main__":
    app = create_app()