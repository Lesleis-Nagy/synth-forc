#
# @author L. Nagy
# @date   11 Jan 2023
#

import os
import json

from logger import log

class Settings:
    r"""
    A class to hold settings information.
    """

    # Possible file names that hold settings information.
    possible_file_names = [os.path.join(os.path.expanduser('~'), '.synth_forc')]

    @staticmethod
    def get_settings():
        r"""
        Static function to retrieve a settings object.
        :return: a Settings object populated from settings or default values.
        """

        # check to see if a settings file exists.
        for file_name in Settings.possible_file_names:
            if os.path.isfile(file_name):
                with open(file_name, "r") as fin:
                    data = json.load(fin)
                    return Settings(data, file_name)

        # The file does not exist, so we create a default settings file and save.
        settings = Settings()

    def __init__(self, data:dict = None, settings_file_name:str = None):
        r"""
        Initialise a Settings object, if data and settings_file_name is given - use that information to initialise
        the object. However, if data and settings_file_name is empty then create a new settings file based on default
        values; this new settings file will be the first one that can be written to on the list of possible settings
        files.
        :param data: the data with which to initialise this settings object.
        :param settings_file_name: the name of the settings file (the first that was successfully loaded) that contained
                                 settings information.
        """

        self.settings_file_name = settings_file_name

        self.smoothing_factor = 3
        self.dpi = 600
        self.major_ticks = 100
        self.minor_ticks = 20
        self.x_limits_from = 0.0
        self.x_limits_to = 200.0
        self.y_limits_from = -200.0
        self.y_limits_to = 200.0
        self.contour_start = 0.1
        self.contour_end = 1.3
        self.contour_step = 0.3

        if data is not None and settings_file_name is not None:
            # Branch to deal with populating settings if file & settings data is given.

            # Get smoothing factor parameter.
            if data.get("smoothing_factor") is not None:
                self.smoothing_factor = data["smoothing_factor"]
            else:
                raise ValueError(f"Settings file is missing 'smoothing_factor' value.")

            # Get dpi parameter.
            if data.get("dpi") is not None:
                self.dpi = data["dpi"]
            else:
                raise ValueError(f"Settings file is missing 'dpi' value.")

            # Get major_ticks parameter.
            if data.get("major_ticks") is not None:
                self.major_ticks = data["major_ticks"]
            else:
                raise ValueError(f"Settings file is missing 'major_ticks' value.")

            # Get minor_ticks parameter.
            if data.get("minor_ticks") is not None:
                self.minor_ticks = data["minor_ticks"]
            else:
                raise ValueError(f"Settings file is missing 'minor_ticks' value.")

            # Get x-limits parameters.
            if data.get("x_limits") is not None:
                x_limits = data["x_limits"]

                if x_limits.get("from") is not None:
                    self.x_limits_from = x_limits["from"]
                else:
                    raise ValueError("Settings file 'x_limits' is missing 'from' value.")

                if x_limits.get("to") is not None:
                    self.x_limits_to = x_limits["to"]
                else:
                    raise ValueError("Settings file 'x_limits' is missing 'to' value.")

            # Get y-limits parameters.
            if data.get("y_limits") is not None:
                y_limits = data["y_limits"]

                if y_limits.get("from") is not None:
                    self.y_limits_from = y_limits["from"]
                else:
                    raise ValueError("Settings file 'y_limits' is missing 'from' value.")

                if y_limits.get("to") is not None:
                    self.y_limits_to = y_limits["to"]
                else:
                    raise ValueError("Settings file 'y_limits' is missing 'to' value.")

            # Get contour parameters.
            if data.get("contour") is not None:
                contour = data["contour"]

                if contour.get("start") is not None:
                    self.contour_start = contour["start"]
                else:
                    raise ValueError("Settings file 'contour' is missing 'start' value.")

                if contour.get("end") is not None:
                    self.contour_end = contour["end"]
                else:
                    raise ValueError("Settings file 'contour' is missing 'end' value.")

                if contour.get("step") is not None:
                    self.contour_step = contour["step"]
                else:
                    raise ValueError("Settings file 'contour' is missing 'step' value.")
        else:
            # Branch to deal with default settings if not settings file & settings data is given.
            settings_file_initialised = False
            for file_name in Settings.possible_file_names:
                try:
                    with open(file_name, "w") as fout:
                        fout.write(json.dumps(self.as_dict()))
                        self.settings_file_name = file_name
                        settings_file_initialised = True
                        break
                except IOError as e:
                    pass

            if not settings_file_initialised:
                raise IOError("Could not initialise a settings file.")

    def as_dict(self):
        r"""
        Return a python dictionary representation of this object.
        :return: a python dictionary representation of this object.
        """
        return {
            'smoothing_factor': self.smoothing_factor,
            'dpi': self.dpi,
            'major_ticks': self.major_ticks,
            'minor_ticks': self.minor_ticks,
            'x_limits': {
                'from': self.x_limits_from,
                'to': self.x_limits_to
            },
            'y_limits': {
                'from': self.y_limits_from,
                'to': self.y_limits_to
            },
            'contour': {
                'start': self.contour_start,
                'end': self.contour_end,
                'step': self.contour_step
            }
        }

    def save(self):
        r"""
        Save this settings object data to the file associated with the settings.
        :return: None
        """
        with open(self.settings_file_name, "w") as fout:
            fout.write(json.dumps(self.as_dict()))

    def __str__(self):
        r"""
        Create a string representation of this object.
        :return: a string representation of this object.
        """
        return
