r"""
A service to retrieve a FORC image.
"""
import json
import os
from enum import Enum

import falcon

from synth_forc import GLOBAL
from synth_forc.cli.response import ResponseStatusEnum
from synth_forc.spawn import generate_single_forc_images
from synth_forc.utilities import single_forc_file_name, single_forc_loop_file_name


class ImageType(Enum):
    FORC = 1
    LOOP = 2


class ImageFormat(Enum):
    PNG = 1
    PDF = 2
    JPG = 3


class GetForcPNG:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_single_image(
            ImageType.FORC,
            ImageFormat.PNG,
            self.config,
            self.logger,
            req, resp
        )


class GetForcPDF:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_single_image(
            ImageType.FORC,
            ImageFormat.PDF,
            self.config,
            self.logger,
            req, resp
        )


class GetForcJPG:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_single_image(
            ImageType.FORC,
            ImageFormat.JPG,
            self.config,
            self.logger,
            req, resp
        )


class GetForcLoopPNG:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_single_image(
            ImageType.LOOP,
            ImageFormat.PNG,
            self.config,
            self.logger,
            req, resp
        )


class GetForcLoopPDF:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_single_image(
            ImageType.LOOP,
            ImageFormat.PDF,
            self.config,
            self.logger,
            req, resp
        )


class GetForcLoopJPG:

    def on_get(self, req, resp):
        r"""
        The 'get' http request handler.
        """

        get_single_image(
            ImageType.LOOP,
            ImageFormat.JPG,
            self.config,
            self.logger,
            req, resp
        )


def stream_single_image(image_type: ImageType, image_format: ImageFormat,
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
    :param resp: the HTTP response object.
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


def get_single_image(image_type: ImageType, image_format: ImageFormat, config, logger, req, resp):
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

        aspect_ratio = float(req.params.get("aspect_ratio"))
        size = float(req.params.get("size"))
        smoothing_factor = int(float(req.params.get("smoothing_factor", GLOBAL.SMOOTHING_FACTOR)))

        str_aspect_ratio = f"{aspect_ratio:.{GLOBAL.FLOAT_STR_DP}f}"
        str_size = f"{size:.{GLOBAL.FLOAT_STR_DP}f}"

        forc_jpg = single_forc_file_name(str_aspect_ratio, str_size, smoothing_factor, '.jpg')
        forc_png = single_forc_file_name(str_aspect_ratio, str_size, smoothing_factor, '.png')
        forc_pdf = single_forc_file_name(str_aspect_ratio, str_size, smoothing_factor, '.pdf')
        forc_loop_jpg = single_forc_loop_file_name(str_aspect_ratio, str_size, '.jpg')
        forc_loop_png = single_forc_loop_file_name(str_aspect_ratio, str_size, '.png')
        forc_loop_pdf = single_forc_loop_file_name(str_aspect_ratio, str_size, '.pdf')

        forc_jpg_abs_path = os.path.join(config.image_directory, forc_jpg)
        forc_png_abs_path = os.path.join(config.image_directory, forc_png)
        forc_pdf_abs_path = os.path.join(config.image_directory, forc_pdf)
        forc_loop_jpg_abs_path = os.path.join(config.image_directory, forc_loop_jpg)
        forc_loop_png_abs_path = os.path.join(config.image_directory, forc_loop_png)
        forc_loop_pdf_abs_path = os.path.join(config.image_directory, forc_loop_pdf)

        logger.debug(f"aspect_ratio: {aspect_ratio}")
        logger.debug(f"size: {size}")
        logger.debug(f"str_aspect_ratio: {str_aspect_ratio}")
        logger.debug(f"str_size: {str_size}")

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

            stream_single_image(image_type, image_format,
                                forc_png_abs_path, forc_pdf_abs_path, forc_jpg_abs_path,
                                forc_loop_png_abs_path, forc_loop_pdf_abs_path, forc_loop_jpg_abs_path,
                                resp)

            return

        else:

            # Generate images.

            stdout, stderr = generate_single_forc_images(
                config.sqlite_file,
                aspect_ratio,
                size,
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
                smoothing_factor)

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
            logger.debug(f"Error occured when trying to run FORC tool: {json_stdout}")
            resp.status = falcon.HTTP_500
            return

        # Check that output files are created.
        if not os.path.isfile(forc_png_abs_path):
            logger.debug(f"After running generate_single_forc_images(), {forc_png_abs_path} is missing.")
            resp.status = falcon.HTTP_500
            return

        if not os.path.isfile(forc_pdf_abs_path):
            logger.debug(f"After running generate_single_forc_images(), {forc_pdf_abs_path} is missing.")
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

        stream_single_image(image_type, image_format,
                            forc_png_abs_path, forc_pdf_abs_path, forc_jpg_abs_path,
                            forc_loop_png_abs_path, forc_loop_pdf_abs_path, forc_loop_jpg_abs_path,
                            resp)

        return

    except Exception:
        logger.debug("Exception occurred.", exc_info=True)
        resp.status = falcon.HTTP_500
        return
