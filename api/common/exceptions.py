import re
from ast import literal_eval


Messages = {
    202: "Accepted",
    400: "Bad Request",
    401: "Unauthorized",
    403: "Forbidden",
    404: "Not Found",
    409: "Conflict",
    412: "Precondition Failed",
    413: "Payload Too Large",
    423: "Locked",
    429: "Rate Limit",
    500: "Internal Server Error",
}


class ErrorCode(Exception):
    status_code = 500

    def __init__(self, status_code=None):
        Exception.__init__(self)
        if status_code is not None:
            self.status_code = status_code

    def to_dict(self):
        rv = {"code": self.status_code, "message": Messages[self.status_code]}
        return rv
