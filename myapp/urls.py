from .views import *


urls = [
    ("/", index, ["GET"]),
    ("/login", login, ["POST"])
]