import os
import yaml

import schematics

from synth_forc import GLOBAL


class Logging(schematics.models.Model):
    r"""
    Class to hold logging information.
    """
    file = schematics.types.StringType(default=None)
    level = schematics.types.StringType(choices=["critical",
                                                 "error",
                                                 "warning",
                                                 "warn",
                                                 "info",
                                                 "debug"],
                                        default="error")
    log_to_stdout = schematics.types.BooleanType(default=False, serialized_name="log-to-stdout")


class Configuration(schematics.models.Model):
    r"""
    Class to hold configuration information.
    """
    image_directory = schematics.types.StringType(required=True, serialized_name="image-directory")

    sqlite_file = schematics.types.StringType(required=True, serialized_name="sqlite-file")

    logging = schematics.types.ModelType(Logging, default=Logging())


def read_config_from_environ() -> Configuration:
    r"""
    Reads configuration information by looking for an environment variable that points to a config file.
    """
    config_file = os.environ.get(GLOBAL.SYNTH_FORC_WEB_CONFIG)
    if config_file is None:
        raise ValueError(f"{GLOBAL.SYNTH_FORC_WEB_CONFIG} variable is not set.")
    else:
        if not os.path.isfile(config_file):
            raise FileNotFoundError(f"Configuration file {config_file} is missing.")
        else:
            with open(config_file, "r") as fin:
                config_dict = yaml.load(fin, Loader=yaml.FullLoader)
                config = Configuration(config_dict)
                config.validate()

            return config
