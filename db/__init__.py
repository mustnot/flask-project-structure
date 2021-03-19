from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def init_db(app: Flask) -> SQLAlchemy:
    for database in app.config.get("INSTALL_DATABASES"):
        db = getattr(__import__(database, fromlist=["apps"]), "db")
        db.init_app(app)
        with app.app_context():
            db.create_all()
    return db