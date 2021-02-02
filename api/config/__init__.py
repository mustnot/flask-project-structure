import os



SECRET_KEY = os.environ.get("SECRET_KEY", "*r_y%w65qdxpf9thh%$3%eyx1h0l^3@!!flo*um3-@e9!%)4xc")


INSTALL_APPS = [
    "apps:main_app"
]


DATABASES = {
    "main": {
        "host": "",
        "port": "",
        "user": "",
        "password": "",
        "db": ""
    }
}
