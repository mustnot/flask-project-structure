import sys

sys.path.append(".")

import json
import unittest


class Testing(unittest.TestCase):
    def setUp(self):
        from myproject import create_app

        app = create_app()
        app.config.from_object("myproject.settings.TestingConfig")
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get("/")
        assert b"This is Sample Blueprint Index Function" == rv.data

    def test_login(self):
        from .models import User

        data = {"id": 1, "name": "gildong"}
        rv = self.app.post("/login", data=data)
        assert User(**data).dict() == json.loads(rv.data)


if __name__ == "__main__":
    unittest.main()