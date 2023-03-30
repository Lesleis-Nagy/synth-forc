class ConfigurationManager:
    r"""
    A configuration object for every request.
    """
    def __init__(self, config):
        self.config = config

    def process_resource(self, req, resp, resource, params):
        resource.config = self.config


class LoggerManager:
    r"""
    A logging object for every request.
    """
    def __init__(self, logger):
        self.logger = logger

    def process_resource(self, req, resp, resource, params):
        resource.logger = self.logger
