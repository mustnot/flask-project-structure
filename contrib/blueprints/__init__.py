from flask import Flask


def register_blueprints(app: Flask) -> Flask:
    with app.app_context():
        for blueprint in app.config.get("INSTALL_BLUEPRINTS"):
            blueprint_app = getattr(__import__("{}".format(blueprint), fromlist=[blueprint]), "blueprint_app")
            app.register_blueprint(blueprint_app)
    return app
