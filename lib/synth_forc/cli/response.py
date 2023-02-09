import json
from enum import Enum

import cerberus


class Response:
    class Status(Enum):
        SUCCESS = "SUCCESS"
        EMPTY_LOOPS = "EMPTY_LOOPS"
        EXCEPTION = "EXCEPTION",
        EMPTY_BINS = "EMPTY_BINS"

    validator = cerberus.Validator({
        "status": {"type": "string",
                   "allowed": [Status.SUCCESS.value,
                               Status.EMPTY_LOOPS.value,
                               Status.EXCEPTION.value,
                               Status.EMPTY_BINS.value],
                   "required": True},
        "message": {"type": "string", "required": True},
        "forc_png": {"type": "string", "required": True},
        "forc_loop_png": {"type": "string", "required": True},
        "exception": {"type": "string", "required": False},

    })

    def __init__(self, **kwargs):
        r"""
        Create a new instance of this class.
        :param args: kwargs must either be:
                     json =
        """

        if kwargs.get("json") is not None:
            # If a 'json' parameter is given, try to populate the class from the information in the JSON.
            if isinstance(kwargs.get("json"), str):
                self._class_from_json(kwargs.get("json"))

        elif kwargs.get("data") is not None:
            # If a 'data' parameter is given, try to populate the class from the input dictionary.
            if isinstance(kwargs.get("data"), dict):
                self._class_from_dict(kwargs.get("data"))

        else:
            # Otherwise, attempt to populate the class from named parameters.

            # Handle the 'status' argument.
            if kwargs.get("status") is not None:
                if isinstance(kwargs.get("status"), Response.Status):
                    self.status = kwargs.get("status")
                elif isinstance(kwargs.get("status"), str):
                    self.status = Response.Status(kwargs.get("status"))
            else:
                raise RuntimeError("Could not create Response class, missing 'status'.")

            # Handle the 'message' argument.
            if kwargs.get("message") is not None:
                self.message = kwargs.get("message")
            else:
                raise RuntimeError("Could not create Response class, missing 'message'.")

            # Handle the 'forc_png' argument.
            if kwargs.get("forc_png") is not None:
                self.forc_png = kwargs.get("forc_png")
            else:
                raise RuntimeError("Could not create Response class, missing 'forc_png'.")

            # Handle the 'forc_loop_png' argument.
            if kwargs.get("forc_loop_png") is not None:
                self.forc_loop_png = kwargs.get("forc_loop_png")
            else:
                raise RuntimeError("Could not create Response class, missing 'forc_loop_png'.")

            # Handle the 'exception' argument.
            if kwargs.get("exception") is not None:
                self.exception = kwargs.get("exception")
            else:
                self.exception = None

    def _class_from_json(self, json_str: str):
        json_dict: dict = json.loads(json_str)
        self._class_from_dict(json_dict)

    def _class_from_dict(self, data: dict):
        if not Response.validator.validate(data):
            raise ValueError("FORC loops CLI JSON response was not valid.")
        else:
            self.status = Response.Status(data.get("status"))
            self.message = data.get("message")
            self.forc_png = data.get("forc_png")
            self.forc_loop_png = data.get("forc_loop_png")
            self.exception = data.get("exception")

    def __str__(self):
        r"""
        Create a JSON string representation of this class.
        """
        if self.exception is not None:
            return json.dumps(
                {
                    "status": self.status.value,
                    "message": self.message,
                    "forc_png": self.forc_png,
                    "forc_loop_png": self.forc_loop_png,
                    "exception": self.exception
                }
            )
        else:
            return json.dumps(
                {
                    "status": self.status.value,
                    "message": self.message,
                    "forc_png": self.forc_png,
                    "forc_loop_png": self.forc_loop_png
                }
            )
