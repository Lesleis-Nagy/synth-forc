r"""
A service to retrieve a FORC image.
"""
import json
import os
from enum import Enum

import falcon

from synth_forc import GLOBAL
from synth_forc.cli.response import ResponseStatusEnum
from synth_forc.spawn import generate_lognormal_forc_images
from synth_forc.utilities import lognormal_forc_file_name, lognormal_forc_loop_file_name


class ImageType(Enum):
    FORC = 1
    LOOP = 2


class ImageFormat(Enum):
    PNG = 1
    PDF = 2
    JPG = 3


class GetLogNormalForcPNG:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_lognormal_image(
            ImageType.FORC,
            ImageFormat.PNG,
            self.config,
            self.logger,
            req, resp
        )


class GetLogNormalForcPDF:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_lognormal_image(
            ImageType.FORC,
            ImageFormat.PDF,
            self.config,
            self.logger,
            req, resp
        )


class GetLogNormalForcJPG:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_lognormal_image(
            ImageType.FORC,
            ImageFormat.JPG,
            self.config,
            self.logger,
            req, resp
        )


class GetLogNormalForcLoopsPNG:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_lognormal_image(
            ImageType.LOOP,
            ImageFormat.PNG,
            self.config,
            self.logger,
            req, resp
        )


class GetLogNormalForcLoopsPDF:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_lognormal_image(
            ImageType.LOOP,
            ImageFormat.PDF,
            self.config,
            self.logger,
            req, resp
        )


class GetLogNormalForcLoopsJPG:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_lognormal_image(
            ImageType.LOOP,
            ImageFormat.JPG,
            self.config,
            self.logger,
            req, resp
        )


def stream_image(image_type: ImageType, image_format: ImageFormat,
                 forc_png_abs_path, forc_pdf_abs_path, forc_jpg_abs_path,
                 forc_loop_png_abs_path, forc_loop_pdf_abs_path, forc_loop_jpg_abs_path,
                 resp):
    r"""
    Helper function that will stream one of the input images based on the image_type and image_format parameters.
    :param image_type: the image type (FORC or LOOP).
    :param image_format: the image format (PNG, PDF or JPG).
    :param forc_png_abs_path: the system path to the FORC diagram png image.
    :param forc_pdf_abs_path: the system path to the FORC diagram pdf image.
    :param forc_jpg_abs_path: the system path to the FORC diagram jpg image.
    :param forc_loop_png_abs_path: the system path to the FORC loop png image.
    :param forc_loop_pdf_abs_path: the system path to the FORC loop pdf image.
    :param forc_loop_jpg_abs_path: the system path to the FORC loop jpg image.
    :param resp: HTTP response object.
    """

    if image_type == ImageType.FORC and image_format == ImageFormat.PNG:
        resp.content_type = "image/png"
        resp.stream = open(forc_png_abs_path, 'rb')
        resp.content_length = os.path.getsize(forc_png_abs_path)
    if image_type == ImageType.FORC and image_format == ImageFormat.PDF:
        resp.content_type = "application/pdf"
        resp.stream = open(forc_pdf_abs_path, 'rb')
        resp.content_length = os.path.getsize(forc_pdf_abs_path)
    if image_type == ImageType.FORC and image_format == ImageFormat.JPG:
        resp.content_type = "image/jpg"
        resp.stream = open(forc_jpg_abs_path, 'rb')
        resp.content_length = os.path.getsize(forc_jpg_abs_path)
    if image_type == ImageType.LOOP and image_format == ImageFormat.PNG:
        resp.content_type = "image/png"
        resp.stream = open(forc_loop_png_abs_path, 'rb')
        resp.content_length = os.path.getsize(forc_loop_png_abs_path)
    if image_type == ImageType.LOOP and image_format == ImageFormat.PDF:
        resp.content_type = "application/pdf"
        resp.stream = open(forc_loop_pdf_abs_path, 'rb')
        resp.content_length = os.path.getsize(forc_loop_pdf_abs_path)
    if image_type == ImageType.LOOP and image_format == ImageFormat.JPG:
        resp.content_type = "image/jpg"
        resp.stream = open(forc_loop_jpg_abs_path, 'rb')
        resp.content_length = os.path.getsize(forc_loop_jpg_abs_path)


def get_lognormal_image(image_type: ImageType, image_format: ImageFormat, config, logger, req, resp):
    r"""
    Helper function for HTTP GET calls (see classes GetForcPNG, GetForcPDF, GetForcJPG, GetForcLoopPNG, GetForcLoopPDF,
    GetForcLoopJPG).
    :param image_type: the image type (FORC or LOOP).
    :param image_format: the image format (PNG, PDF or JPG).
    :param config: system configuration information.
    :param logger: system logger.
    :param req: the request object.
    :param resp: the response object.
    """
    try:

        # Required.

        arat_shape = float(req.params.get("aspect_ratio_shape"))
        arat_loc = float(req.params.get("aspect_ratio_location"))
        arat_scale = float(req.params.get("aspect_ratio_scale"))
        size_shape = float(req.params.get("size_shape"))
        size_loc = float(req.params.get("size_location"))
        size_scale = float(req.params.get("size_scale"))
        smoothing_factor = int(req.params.get("smoothing_factor", GLOBAL.SMOOTHING_FACTOR))

        str_arat_shape = f"{arat_shape:.{GLOBAL.FLOAT_STR_DP}f}"
        str_arat_loc = f"{arat_loc:.{GLOBAL.FLOAT_STR_DP}f}"
        str_arat_scale = f"{arat_scale:.{GLOBAL.FLOAT_STR_DP}f}"

        str_size_shape = f"{size_shape:.{GLOBAL.FLOAT_STR_DP}f}"
        str_size_loc = f"{size_loc:.{GLOBAL.FLOAT_STR_DP}f}"
        str_size_scale = f"{size_scale:.{GLOBAL.FLOAT_STR_DP}f}"

        forc_jpg = lognormal_forc_file_name(str_arat_shape, str_arat_loc, str_arat_shape,
                                            str_size_shape, str_size_loc, str_size_scale,
                                            smoothing_factor, '.jpg')
        forc_png = lognormal_forc_file_name(str_arat_shape, str_arat_loc, str_arat_shape,
                                            str_size_shape, str_size_loc, str_size_scale,
                                            smoothing_factor, '.png')
        forc_pdf = lognormal_forc_file_name(str_arat_shape, str_arat_loc, str_arat_shape,
                                            str_size_shape, str_size_loc, str_size_scale,
                                            smoothing_factor, '.pdf')

        forc_loop_jpg = lognormal_forc_loop_file_name(str_arat_shape, str_arat_loc, str_arat_shape,
                                                      str_size_shape, str_size_loc, str_size_scale,
                                                      '.jpg')
        forc_loop_png = lognormal_forc_loop_file_name(str_arat_shape, str_arat_loc, str_arat_shape,
                                                      str_size_shape, str_size_loc, str_size_scale,
                                                      '.png')
        forc_loop_pdf = lognormal_forc_loop_file_name(str_arat_shape, str_arat_loc, str_arat_shape,
                                                      str_size_shape, str_size_loc, str_size_scale,
                                                      '.pdf')

        forc_jpg_abs_path = os.path.join(config.image_directory, forc_jpg)
        forc_png_abs_path = os.path.join(config.image_directory, forc_png)
        forc_pdf_abs_path = os.path.join(config.image_directory, forc_pdf)
        forc_loop_jpg_abs_path = os.path.join(config.image_directory, forc_loop_jpg)
        forc_loop_png_abs_path = os.path.join(config.image_directory, forc_loop_png)
        forc_loop_pdf_abs_path = os.path.join(config.image_directory, forc_loop_pdf)

        logger.debug(f"FORC jpg name: {forc_jpg}")
        logger.debug(f"FORC png name: {forc_png}")
        logger.debug(f"FORC pdf name: {forc_pdf}")

        logger.debug(f"FORC jpg file absolut path: {forc_jpg_abs_path}")
        logger.debug(f"FORC png file absolut path: {forc_png_abs_path}")
        logger.debug(f"FORC pdf file absolut path: {forc_pdf_abs_path}")

        # Optional.

        major_ticks = int(req.params.get("major_ticks", 100))
        minor_ticks = int(req.params.get("minor_ticks", 20))
        x_limits_from = float(req.params.get("x_limits_from", 0.0))
        x_limits_to = float(req.params.get("x_limits_to", 200.0))
        y_limits_from = float(req.params.get("y_limits_from", -200.0))
        y_limits_to = float(req.params.get("y_limits_to", 200.0))
        contour_start = float(req.params.get("contour_start", 0.1))
        contour_end = float(req.params.get("contour_end", 1.3))
        contour_step = float(req.params.get("contour_step", 0.3))

        logger.debug(f"major_ticks: {major_ticks}")
        logger.debug(f"minor_ticks: {minor_ticks}")
        logger.debug(f"x_limits_from: {x_limits_from}")
        logger.debug(f"x_limits_to: {x_limits_to}")
        logger.debug(f"y_limits_from: {y_limits_from}")
        logger.debug(f"y_limits_to: {y_limits_to}")
        logger.debug(f"contour_start: {contour_start}")
        logger.debug(f"contour_end: {contour_end}")
        logger.debug(f"contour_step: {contour_step}")

        # Check if all required files are present.
        if os.path.isfile(forc_jpg_abs_path) \
                and os.path.isfile(forc_png_abs_path) \
                and os.path.isfile(forc_pdf_abs_path) \
                and os.path.isfile(forc_loop_jpg_abs_path) \
                and os.path.isfile(forc_loop_png_abs_path) \
                and os.path.isfile(forc_loop_pdf_abs_path):

            stream_image(image_type, image_format,
                         forc_png_abs_path, forc_pdf_abs_path, forc_jpg_abs_path,
                         forc_loop_png_abs_path, forc_loop_pdf_abs_path, forc_loop_jpg_abs_path,
                         resp)

            return

        else:

            # Generate images.

            stdout, stderr = generate_lognormal_forc_images(
                config.sqlite_file,
                arat_shape,
                arat_loc,
                arat_scale,
                size_shape,
                size_loc,
                size_scale,
                major_ticks,
                minor_ticks,
                x_limits_from,
                x_limits_to,
                y_limits_from,
                y_limits_to,
                contour_start,
                contour_end,
                contour_step,
                forc_png_abs_path,
                forc_pdf_abs_path,
                forc_jpg_abs_path,
                forc_loop_png_abs_path,
                forc_loop_pdf_abs_path,
                forc_loop_jpg_abs_path,
                smoothing_factor,
                config.logging.file,
                config.logging.level)

        # Check the stderr.

        if stderr != "":
            logger.debug(f"Standard error after running the FORC tool was not empty!")
            logger.debug(stderr)
            resp.status = falcon.HTTP_500
            return

        # Check the standard output for errors.

        json_stdout = json.loads(stdout)
        if json_stdout.get("status") == ResponseStatusEnum.EMPTY_LOOPS.value:
            resp.status = falcon.HTTP_404
            return
        elif json_stdout.get("status") == ResponseStatusEnum.EXCEPTION.value:
            logger.debug(f"Error occurred when trying to run FORC tool: {json_stdout}")
            resp.status = falcon.HTTP_500
            return

        # Check that output files are created.
        if not os.path.isfile(forc_png_abs_path):
            logger.debug(f"After running generate_lognormal_forc_images(), {forc_png_abs_path} is missing.")
            resp.status = falcon.HTTP_500
            return

        if not os.path.isfile(forc_pdf_abs_path):
            logger.debug(f"After running generate_lognormal_forc_images(), {forc_pdf_abs_path} is missing.")
            resp.status = falcon.HTTP_500
            return

        if not os.path.isfile(forc_jpg_abs_path):
            logger.debug(f"After running generate_single_forc_images(), {forc_jpg_abs_path} is missing.")
            resp.status = falcon.HTTP_500
            return

        if not os.path.isfile(forc_loop_png_abs_path):
            logger.debug(f"After running generate_single_forc_images(), {forc_loop_png_abs_path} is missing.")
            resp.status = falcon.HTTP_500
            return

        if not os.path.isfile(forc_loop_pdf_abs_path):
            logger.debug(f"After running generate_single_forc_images(), {forc_loop_pdf_abs_path} is missing.")
            resp.status = falcon.HTTP_500
            return

        if not os.path.isfile(forc_loop_jpg_abs_path):
            logger.debug(f"After running generate_single_forc_images(), {forc_loop_jpg_abs_path} is missing.")
            resp.status = falcon.HTTP_500
            return

        stream_image(image_type, image_format,
                     forc_png_abs_path, forc_pdf_abs_path, forc_jpg_abs_path,
                     forc_loop_png_abs_path, forc_loop_pdf_abs_path, forc_loop_jpg_abs_path,
                     resp)

        return

    except Exception:
        logger.debug("Exception occurred.", exc_info=True)
        resp.status = falcon.HTTP_500
        return
