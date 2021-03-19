import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class DefaultConfig(object):
    ENV = "default"
    SECRET_KEY = os.environ.get("SECRET_KEY", "*r_y%w65qdxpf9thh%$3%eyx1h0l^3@!!flo*um3-@e9!%)4xc")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI", "sqlite:///../db.sqlite3")
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    INSTALL_BLUEPRINTS = ["apps.user"]
    INSTALL_DATABASES = ["apps.user.models"]


class ProductionConfig(DefaultConfig):
    ENV = "production"


class DevelopmentConfig(DefaultConfig):
    ENV = "development"
    DEBUG = True


class TestingConfig(DefaultConfig):
    ENV = "testing"
    TESTING = True


def get_config() -> object:
    config_name = os.environ.get("PROJECT_CONF", "DefaultConfig")
    config = getattr(__import__("config", fromlist=["config"]), config_name)
    return config


Config = get_config()