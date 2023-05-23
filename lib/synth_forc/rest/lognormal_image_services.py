r"""
A service to retrieve a FORC image.
"""
import os
from enum import Enum

import falcon

from synth_forc.logger import get_logger
from synth_forc.rest.lognormal_data import generate_lognormal_data, LogNormalRequestParameters


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


def get_lognormal_image(image_type: ImageType, image_format: ImageFormat, req, resp):
    r"""
    Helper function for HTTP GET calls (see classes GetForcPNG, GetForcPDF, GetForcJPG, GetForcLoopPNG, GetForcLoopPDF,
    GetForcLoopJPG).
    :param image_type: the image type (FORC or LOOP).
    :param image_format: the image format (PNG, PDF or JPG).
    :param req: the request object.
    :param resp: the response object.
    """

    logger = get_logger()

    params = LogNormalRequestParameters(req)

    resp.status = generate_lognormal_data(params)

    if resp.status == falcon.HTTP_OK:
        stream_image(image_type, image_format,
                     params.forc_png_abs_path, params.forc_pdf_abs_path, params.forc_jpg_abs_path,
                     params.forc_loop_png_abs_path, params.forc_loop_pdf_abs_path, params.forc_loop_jpg_abs_path,
                     resp)
    else:
        logger.debug("Some kind of error occurred when attempting to run generate_lognormal_data() function.")
