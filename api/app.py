import gevent.monkey

gevent.monkey.patch_all()

from config import *
from common import blueprint_app


def create_app():
    from flask import Flask, jsonify
    from flask_cors import CORS

    app = Flask(__name__)
    CORS(app)

    # Register Blueprint APPS
    for module in INSTALL_APPS:
        app.register_blueprint(blueprint_app(module))

    # Register Custom ErrorHandler
    from werkzeug.exceptions import HTTPException
    from common.exceptions import Messages, ErrorCode

    @app.errorhandler(ErrorCode)
    @app.errorhandler(HTTPException)
    def error_handler(error):
        if error.code not in Messages:
            error.code = 500

        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response

    return app


app = create_app()