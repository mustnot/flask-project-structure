from flask import jsonify

error_messages = {
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


def global_error_handler(error):
    if 'code' not in dir(error):
        error.code = 500
    if error.code not in error_messages:
        error.code = 500

    return jsonify({"code": error.code, "message": error_messages[error.code]}), error.code