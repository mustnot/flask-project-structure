import sys

sys.path.append('.')

import json
import unittest


class Testing(unittest.TestCase):
    def setUp(self):
        from apps import create_app

        app = create_app()
        app.config.from_object("config.TestingConfig")
        self.app = app.test_client()

    def test_index(self):
        rv = self.app.get("/api/user/")
        assert b"this is user app index enpoint" == rv.data


if __name__ == "__main__":
    unittest.main()