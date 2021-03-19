from .views import index, signup, login, logout, delete


urls = [
    ("/", index, ["GET"]),
    ("/signup", signup, ["POST"]),
    ("/login", login, ["POST"]),
    ("/logout", logout, ["POST"]),
    ("/<string:username>", delete, ["DELETE"]),
]