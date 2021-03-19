from flask import Flask


def register_blueprints(app: Flask) -> Flask:
    with app.app_context():
        for blueprint in app.config.get("INSTALL_BLUEPRINTS"):
            blueprint_app = getattr(__import__(blueprint, fromlist=["apps"]), "blueprint_app")
            app.register_blueprint(blueprint_app)
    return app


def register_extensions(app: Flask) -> Flask:
    from contrib.extension import cors

    cors.init_app(app)
    return app


def register_error_handler(app: Flask) -> Flask:
    from contrib.handlers import global_error_handler

    app.register_error_handler(Exception, global_error_handler)
    return app