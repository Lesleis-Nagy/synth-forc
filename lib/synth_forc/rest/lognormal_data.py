r"""
A service to retrieve FORC data.
"""
import json
import os

import falcon

from synth_forc import GLOBAL
from synth_forc.cli.response import ResponseStatusEnum
from synth_forc.rest.config import read_config_from_environ
from synth_forc.spawn import generate_lognormal_forc_images
from synth_forc.utilities import lognormal_forc_file_name
from synth_forc.utilities import lognormal_forc_loop_file_name
from synth_forc.utilities import lognormal_forc_output_json_file_name
from synth_forc.logger import get_logger


class LogNormalRequestParameters:

    def __init__(self, req):

        config = read_config_from_environ()
        logger = get_logger()

        str_arat_shape = req.params.get("aspect_ratio_shape")
        str_arat_loc = req.params.get("aspect_ratio_location")
        str_arat_scale = req.params.get("aspect_ratio_scale")
        str_size_shape = req.params.get("size_shape")
        str_size_loc = req.params.get("size_location")
        str_size_scale = req.params.get("size_scale")

        str_smoothing_factor = req.params.get("smoothing_factor", GLOBAL.SMOOTHING_FACTOR)
        str_major_ticks = req.params.get("major_ticks", "100")
        str_minor_ticks = req.params.get("minor_ticks", "20")
        str_x_limits_from = req.params.get("x_limits_from", "0.0")
        str_x_limits_to = req.params.get("x_limits_to", "200.0")
        str_y_limits_from = req.params.get("y_limits_from", "-200.0")
        str_y_limits_to = req.params.get("y_limits_to", "200.0")
        str_contour_start = req.params.get("contour_start", "0.1")
        str_contour_end = req.params.get("contour_end", "1.3")
        str_contour_step = req.params.get("contour_step", "0.3")

        self.arat_shape = float(str_arat_shape)
        self.arat_loc = float(str_arat_loc)
        self.arat_scale = float(str_arat_scale)
        self.size_shape = float(str_size_shape)
        self.size_loc = float(str_size_loc)
        self.size_scale = float(str_size_scale)
        self.smoothing_factor = int(str_smoothing_factor)

        self.major_ticks = int(str_major_ticks)
        self.minor_ticks = int(str_minor_ticks)
        self.x_limits_from = float(str_x_limits_from)
        self.x_limits_to = float(str_x_limits_to)
        self.y_limits_from = float(str_y_limits_from)
        self.y_limits_to = float(str_y_limits_to)
        self.contour_start = float(str_contour_start)
        self.contour_end = float(str_contour_end)
        self.contour_step = float(str_contour_step)

        self.forc_jpg = lognormal_forc_file_name(self.arat_shape, self.arat_loc, self.arat_scale,
                                                 self.size_shape, self.size_loc, self.size_scale,
                                                 self.smoothing_factor, '.jpg')

        self.forc_png = lognormal_forc_file_name(self.arat_shape, self.arat_loc, self.arat_scale,
                                                 self.size_shape, self.size_loc, self.size_scale,
                                                 self.smoothing_factor, '.png')

        self.forc_pdf = lognormal_forc_file_name(self.arat_shape, self.arat_loc, self.arat_scale,
                                                 self.size_shape, self.size_loc, self.size_scale,
                                                 self.smoothing_factor, '.pdf')

        self.forc_loop_jpg = lognormal_forc_loop_file_name(self.arat_shape, self.arat_loc, self.arat_scale,
                                                           self.size_shape, self.size_loc, self.size_scale,
                                                           '.jpg')

        self.forc_loop_png = lognormal_forc_loop_file_name(self.arat_shape, self.arat_loc, self.arat_scale,
                                                           self.size_shape, self.size_loc, self.size_scale,
                                                           '.png')

        self.forc_loop_pdf = lognormal_forc_loop_file_name(self.arat_shape, self.arat_loc, self.arat_scale,
                                                           self.size_shape, self.size_loc, self.size_scale,
                                                           '.pdf')

        self.forc_output_json_data = lognormal_forc_output_json_file_name(self.arat_shape, self.arat_loc,
                                                                          self.arat_scale,
                                                                          self.size_shape, self.size_loc,
                                                                          self.size_scale)

        self.forc_jpg_abs_path = os.path.join(config.image_directory, self.forc_jpg)
        self.forc_png_abs_path = os.path.join(config.image_directory, self.forc_png)
        self.forc_pdf_abs_path = os.path.join(config.image_directory, self.forc_pdf)
        self.forc_loop_jpg_abs_path = os.path.join(config.image_directory, self.forc_loop_jpg)
        self.forc_loop_png_abs_path = os.path.join(config.image_directory, self.forc_loop_png)
        self.forc_loop_pdf_abs_path = os.path.join(config.image_directory, self.forc_loop_pdf)
        self.forc_output_json_abs_path = os.path.join(config.image_directory, self.forc_output_json_data)

        logger.debug(f"FORC jpg name: {self.forc_jpg}")
        logger.debug(f"FORC png name: {self.forc_png}")
        logger.debug(f"FORC pdf name: {self.forc_pdf}")

        logger.debug(f"FORC jpg file absolut path: {self.forc_jpg_abs_path}")
        logger.debug(f"FORC png file absolut path: {self.forc_png_abs_path}")
        logger.debug(f"FORC pdf file absolut path: {self.forc_pdf_abs_path}")


def generate_lognormal_data(params: LogNormalRequestParameters):
    r"""
    Helper function for HTTP GET calls (see classes GetForcPNG, GetForcPDF, GetForcJPG, GetForcLoopPNG, GetForcLoopPDF,
    GetForcLoopJPG).
    :param params: the log normal parameters object.
    """

    logger = get_logger()

    try:

        # Check if all required files are present.
        if os.path.isfile(params.forc_jpg_abs_path) \
                and os.path.isfile(params.forc_png_abs_path) \
                and os.path.isfile(params.forc_pdf_abs_path) \
                and os.path.isfile(params.forc_loop_jpg_abs_path) \
                and os.path.isfile(params.forc_loop_png_abs_path) \
                and os.path.isfile(params.forc_loop_pdf_abs_path) \
                and os.path.isfile(params.forc_output_json_abs_path):

            return falcon.HTTP_OK

        else:

            # Generate images & data.

            config = read_config_from_environ()

            stdout, stderr = generate_lognormal_forc_images(
                config.sqlite_file,
                params.arat_shape,
                params.arat_loc,
                params.arat_scale,
                params.size_shape,
                params.size_loc,
                params.size_scale,
                params.major_ticks,
                params.minor_ticks,
                params.x_limits_from,
                params.x_limits_to,
                params.y_limits_from,
                params.y_limits_to,
                params.contour_start,
                params.contour_end,
                params.contour_step,
                params.forc_png_abs_path,
                params.forc_pdf_abs_path,
                params.forc_jpg_abs_path,
                params.forc_loop_png_abs_path,
                params.forc_loop_pdf_abs_path,
                params.forc_loop_jpg_abs_path,
                params.smoothing_factor,
                config.logging.file,
                config.logging.level)

        # Check the stderr.

        if stderr != "":
            logger.debug(f"Standard error after running the FORC tool was not empty!")
            logger.debug(stderr)
            return falcon.HTTP_500

        # Check the standard output for errors.

        json_stdout = json.loads(stdout)
        if json_stdout.get("status") == ResponseStatusEnum.EMPTY_LOOPS.value:
            return falcon.HTTP_404
        elif json_stdout.get("status") == ResponseStatusEnum.EXCEPTION.value:
            logger.debug(f"Error occurred when trying to run FORC tool: {json_stdout}")
            return falcon.HTTP_500

        # Write the json file out.
        with open(params.forc_output_json_abs_path, "w") as fout:
            fout.write(json.dumps(json_stdout))

        # Check that output files are created.

        if not os.path.isfile(params.forc_png_abs_path):
            logger.debug(f"After running generate_lognormal_data(), {params.forc_png_abs_path} is missing.")
            return falcon.HTTP_500

        if not os.path.isfile(params.forc_pdf_abs_path):
            logger.debug(f"After running generate_lognormal_data(), {params.forc_pdf_abs_path} is missing.")
            return falcon.HTTP_500

        if not os.path.isfile(params.forc_jpg_abs_path):
            logger.debug(f"After running generate_lognormal_data(), {params.forc_jpg_abs_path} is missing.")
            return falcon.HTTP_500

        if not os.path.isfile(params.forc_loop_png_abs_path):
            logger.debug(f"After running generate_lognormal_data(), {params.forc_loop_png_abs_path} is missing.")
            return falcon.HTTP_500

        if not os.path.isfile(params.forc_loop_pdf_abs_path):
            logger.debug(f"After running generate_lognormal_data(), {params.forc_loop_pdf_abs_path} is missing.")
            return falcon.HTTP_500

        if not os.path.isfile(params.forc_loop_jpg_abs_path):
            logger.debug(f"After running generate_lognormal_data(), {params.forc_loop_jpg_abs_path} is missing.")
            return falcon.HTTP_500

        if not os.path.isfile(params.forc_output_json_abs_path):
            logger.debug(f"After running generate_lognormal_data(), {params.forc_output_json_abs_path} is missing.")
            return falcon.HTTP_500

        return falcon.HTTP_OK

    except Exception:
        logger.debug("Exception occurred.", exc_info=True)
        return falcon.HTTP_500
