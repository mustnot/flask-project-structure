import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

class DefaultConfig(object):
    ENV = "default"
    SECRET_KEY = os.environ.get("SECRET_KEY", "*r_y%w65qdxpf9thh%$3%eyx1h0l^3@!!flo*um3-@e9!%)4xc")
    DATABASE_URI = os.environ.get("DATABASE_URI", os.path.join("sqlite://", BASE_DIR, "db.sqlite3"))
    INSTALL_BLUEPRINTS = ["myapp"]


class ProductionConfig(DefaultConfig):
    ENV = "production2"
    pass


class DevelopmentConfig(DefaultConfig):
    ENV = "development"
    DEBUG = True
    pass


class TestingConfig(DefaultConfig):
    ENV = "testing"
    TESTING = True
    pass
