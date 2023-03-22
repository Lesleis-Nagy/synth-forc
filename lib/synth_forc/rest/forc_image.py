r"""
A service to retrieve a FORC image.
"""

import falcon


class ForcImage:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """
