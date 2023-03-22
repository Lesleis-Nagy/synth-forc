import os
import yaml

import schematics


from synth_forc import GLOBAL


class Configuration(schematics.models.Model):

    image_directory = schematics.types.StringType(serialized_name="image-directory")

    sqlite_file = schematics.types.StringType(serialized_name="sqlite-file")


def read_config_from_environ() -> Configuration:
    config_file = os.environ.get(GLOBAL.SYNTH_FORC_WEB_CONFIG)
    if config_file is None:
        raise ValueError(f"{GLOBAL.SYNTH_FORC_WEB_CONFIG} variable is not set.")
    else:
        if os.path.isfile(config_file):
            raise FileNotFoundError(f"Configuration file {config_file} is missing.")
        else:
            with open(config_file, "r") as fin:
                config_dict = yaml.load(fin, Loader=yaml.FullLoader)
                config = Configuration(config_dict)
                config.validate()

            return config
