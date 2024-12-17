import json


class Response:
    def __init__(self, message, status_code, data=None, error=None) -> dict:
        self.message = message
        self.error = error
        self.data = data
        self.status_code = status_code

    def to_json(self):
        response = {
            "message": self.get_message(),
            "data": self.data,
            "error": self.get_error(),
        }
        return json.dumps(response), self.status_code

    def get_message(self):
        message = None

        if isinstance(self.message, Exception):
            message = type(self.message).__name__

        elif type(self.message) == str:
            message = self.message

        return message

    def get_error(self):
        error = None

        if type(self.error) == dict or type(self.error) == str:
            error = self.error

        elif isinstance(self.error, Exception):
            error = str(self.error)

        return error
