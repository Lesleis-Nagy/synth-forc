# Copyright 2023 L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
#
# Redistribution and use in source and binary forms, with or without modification, are permitted provided that the
# following conditions are met:
#
#   1. Redistributions of source code must retain the above copyright notice, this list of conditions and the
#      following disclaimer.
#
#   2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the
#      following disclaimer in the documentation and/or other materials provided with the distribution.
#
#   3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote
#      products derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES,
# INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

#
# Project: synth-forc
# File: forc_all.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import sys
import json
import typer

from synth_forc.logger import setup_logger, get_logger
from synth_forc.plotting.log_normal import BinsEmptyException, random_plot
from synth_forc.synthforc_db import SynthForcDB
from synth_forc.plotting.forc import generate_forc_plot
from synth_forc.plotting.forc_loops import generate_forc_loops_plot
from synth_forc.cli.response import Response
from synth_forc.cli.response import ResponseStatusEnum

app = typer.Typer()


@app.command()
def single(
        input_data_file: str = typer.Option(..., help="Input file containing direction averaged FORC data."),
        aspect_ratio: float = typer.Option(..., help="Aspect ratio of the grain."),
        size: float = typer.Option(..., help="Size of the grain."),
        major_ticks: int = typer.Option(100, help="The major ticks used in the FORC plot"),
        minor_ticks: int = typer.Option(20, help="The minor ticks used in the FORC plot"),
        x_limits_from: float = typer.Option(0.0, help="The start of the x-axis number limits."),
        x_limits_to: float = typer.Option(200.0, help="The end of the x-axis number limits."),
        y_limits_from: float = typer.Option(-200.0, help="The start of the y-axis number limits."),
        y_limits_to: float = typer.Option(200.0, help="The end of the y-axis number limits."),
        contour_start: float = typer.Option(0.1, help="Start value of the contours that are displayed in the FORC."),
        contour_end: float = typer.Option(1.3, help="End value of the contours that are displayed in the FORC."),
        contour_step: float = typer.Option(0.3, help="Steps between contour_start & contour_end parameters."),
        forc_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
        forc_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
        forc_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
        forc_loops_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
        forc_loops_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
        forc_loops_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
        smoothing_factor: int = typer.Option(3, help="Smoothing factor."),
        dpi: int = typer.Option(600, help="Resolution of the output image (only applies to PNG and JPG images)."),
        log_file: str = typer.Option(None, help="A log file to send logging data to."),
        log_level: str = typer.Option(None, help="The level at which logging data should be produced."),
        json_output: bool = typer.Option(False, help="Return the output response using JSON.")):
    r"""
    Create a FORC diagram of a single grain based on data read from `input_data_file`.
    """
    setup_logger(log_file, log_level, False)
    logger = get_logger()
    logger.debug("Running single subcommand.")
    try:
        synthforc_db = SynthForcDB(input_data_file)
        forc_loops = synthforc_db.single_forc_loops_by_aspect_ratio_and_size(aspect_ratio, size)
        if forc_loops.shape[0] == 0:
            message = f"No loops found for aspect ratio {aspect_ratio} and size {size}"
            if json_output:
                response = Response()
                response.status = ResponseStatusEnum.EMPTY_LOOPS.value
                response.message = message
                print(json.dumps(response.to_primitive()))
            else:
                print(message)
            sys.exit(1)

        generate_forc_plot(
            forc_loops,
            [f for f in [forc_plot_png, forc_plot_pdf, forc_plot_jpg] if f is not None],
            dpi=dpi,
            smoothing_factor=smoothing_factor,
            major_ticks=major_ticks,
            minor_ticks=minor_ticks,
            x_limits_from=x_limits_from,
            x_limits_to=x_limits_to,
            y_limits_from=y_limits_from,
            y_limits_to=y_limits_to,
            contour_start=contour_start,
            contour_end=contour_end,
            contour_step=contour_step)

        generate_forc_loops_plot(
            forc_loops,
            [f for f in [forc_loops_plot_png, forc_loops_plot_pdf, forc_loops_plot_jpg] if f is not None],
            dpi=dpi)

        message = "Finished!"
        if json_output:
            response = Response()
            response.status = ResponseStatusEnum.SUCCESS.value
            response.forc_png = forc_plot_png
            response.forc_loop_png = forc_loops_plot_png
            response.message = message
            print(json.dumps(response.to_primitive()))
        else:
            print(message)

    except Exception as e:
        logger.debug(str(e))
        message = "Error running code!"
        if json_output:
            response = Response()
            response.status = ResponseStatusEnum.EXCEPTION.value
            response.message = message
            response.exception = str(e)
            print(json.dumps(response.to_primitive()))
        else:
            print(message)
        sys.exit(1)


@app.command()
def log_normal(
        input_data_file: str = typer.Option(..., help="Input file containing direction averaged FORC data."),
        ar_shape: float = typer.Option(..., help="Shape parameter of the aspect ratio distribution."),
        ar_location: float = typer.Option(..., help="Location parameter of the aspect ratio distribution."),
        ar_scale: float = typer.Option(..., help="Scale parameter of the aspect ratio distribution."),
        size_shape: float = typer.Option(..., help="Shape parameter of the size distribution."),
        size_location: float = typer.Option(..., help="Location parameter of the size distribution."),
        size_scale: float = typer.Option(..., help="Scale parameter of the size distribution."),
        major_ticks: int = typer.Option(100, help="The major ticks used in the FORC plot"),
        minor_ticks: int = typer.Option(20, help="The minor ticks used in the FORC plot"),
        x_limits_from: float = typer.Option(0.0, help="The start of the x-axis number limits."),
        x_limits_to: float = typer.Option(200.0, help="The end of the x-axis number limits."),
        y_limits_from: float = typer.Option(-200.0, help="The start of the y-axis number limits."),
        y_limits_to: float = typer.Option(200.0, help="The end of the y-axis number limits."),
        contour_start: float = typer.Option(0.1, help="Start value of the contours shown in the FORC."),
        contour_end: float = typer.Option(1.3, help="End value of the contours shown in the FORC."),
        contour_step: float = typer.Option(0.3, help="Steps between contour_start & contour_end parameters."),
        forc_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
        forc_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
        forc_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
        forc_loops_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
        forc_loops_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
        forc_loops_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
        smoothing_factor: int = typer.Option(3, help="Smoothing factor."),
        dpi: int = typer.Option(600, help="Resolution of the output image (PNG & JPG only)."),
        log_file: str = typer.Option(None, help="A log file to send logging data to."),
        log_level: str = typer.Option(None, help="The level at which logging data should be produced."),
        json_output: bool = typer.Option(False, help="Return the output response using JSON.")):
    r"""
    Create a FORC diagram based on a size and aspect ratio distribution.
    """
    setup_logger(log_file, log_level, False)
    logger = get_logger()
    logger.debug("Running log_normal subcommand.")
    try:
        synthforc_db = SynthForcDB(input_data_file)

        combined_loops = synthforc_db.combine_loops(ar_shape,
                                                    ar_location,
                                                    ar_scale,
                                                    size_shape,
                                                    size_location,
                                                    size_scale)

        if combined_loops.shape[0] == 0:
            message = f"No loops found for input distributions."
            if json_output:
                response = Response()
                response.status = ResponseStatusEnum.EMPTY_LOOPS.value
                response.message = message
                print(json.dumps(response.to_primitive()))
            else:
                print(message)
            sys.exit(1)

        generate_forc_plot(
            combined_loops,
            [f for f in [forc_plot_png, forc_plot_pdf, forc_plot_jpg] if f is not None],
            dpi=dpi,
            smoothing_factor=smoothing_factor,
            major_ticks=major_ticks,
            minor_ticks=minor_ticks,
            x_limits_from=x_limits_from,
            x_limits_to=x_limits_to,
            y_limits_from=y_limits_from,
            y_limits_to=y_limits_to,
            contour_start=contour_start,
            contour_end=contour_end,
            contour_step=contour_step)

        generate_forc_loops_plot(
            combined_loops,
            [f for f in [forc_loops_plot_png, forc_loops_plot_pdf, forc_loops_plot_jpg] if f is not None],
            dpi=dpi)

        message = "Finished!"
        if json_output:
            response = Response()
            response.status = ResponseStatusEnum.SUCCESS.value
            response.forc_png = forc_plot_png
            response.forc_loop_png = forc_loops_plot_png
            response.message = message
            print(json.dumps(response.to_primitive()))
        else:
            print(message)

    except BinsEmptyException as e:
        message = "Empty bins when calculating distribution weights."
        if json_output:
            response = Response()
            response.status = ResponseStatusEnum.EMPTY_BINS.value
            response.message = message
            response.exception = str(e)
            print(json.dumps(response.to_primitive()))
        else:
            print(message)
        sys.exit(1)

    except Exception as e:
        logger.debug(str(e))
        message = "Error running code!"
        if json_output:
            response = Response()
            response.status = ResponseStatusEnum.EXCEPTION.value
            response.message = message
            response.exception = str(e)
            print(json.dumps(response.to_primitive()))
        else:
            print(message)
        sys.exit(1)

@app.command()
def random(
        input_data_file: str = typer.Option(..., help="Input file containing direction averaged FORC data."),
        major_ticks: int = typer.Option(100, help="The major ticks used in the FORC plot"),
        minor_ticks: int = typer.Option(20, help="The minor ticks used in the FORC plot"),
        x_limits_from: float = typer.Option(0.0, help="The start of the x-axis number limits."),
        x_limits_to: float = typer.Option(200.0, help="The end of the x-axis number limits."),
        y_limits_from: float = typer.Option(-200.0, help="The start of the y-axis number limits."),
        y_limits_to: float = typer.Option(200.0, help="The end of the y-axis number limits."),
        contour_start: float = typer.Option(0.1, help="Start value of the contours shown in the FORC."),
        contour_end: float = typer.Option(1.3, help="End value of the contours shown in the FORC."),
        contour_step: float = typer.Option(0.3, help="Steps between contour_start & contour_end parameters."),
        forc_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
        forc_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
        forc_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
        forc_loops_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
        forc_loops_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
        forc_loops_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
        random_plot_png: str = typer.Option(None, help="Name of the distribution PNG corresponding to the forc plot"),
        random_plot_pdf: str = typer.Option(None, help="Name of the distribution PDF corresponding to the forc plot"),
        random_plot_jpg: str = typer.Option(None, help="Name of the distribution PNG corresponding to the forc plot"),
        smoothing_factor: int = typer.Option(3, help="Smoothing factor."),
        dpi: int = typer.Option(600, help="Resolution of the output image (PNG & JPG only)."),
        log_file: str = typer.Option(None, help="A log file to send logging data to."),
        log_level: str = typer.Option(None, help="The level at which logging data should be produced."),
        json_output: bool = typer.Option(False, help="Return the output response using JSON.")):
    r"""
    Create a FORC diagram based on a size and aspect ratio distribution.
    """
    setup_logger(log_file, log_level, False)
    logger = get_logger()
    logger.debug("Running log_normal subcommand.")
    try:
        synthforc_db = SynthForcDB(input_data_file)

        combined_loops, ar_fractions, size_fractions = synthforc_db.combine_loops_random()

        if combined_loops.shape[0] == 0:
            message = f"No loops found for input distributions."
            if json_output:
                response = Response()
                response.status = ResponseStatusEnum.EMPTY_LOOPS.value
                response.message = message
                print(json.dumps(response.to_primitive()))
            else:
                print(message)
            sys.exit(1)

        generate_forc_plot(
            combined_loops,
            [f for f in [forc_plot_png, forc_plot_pdf, forc_plot_jpg] if f is not None],
            dpi=dpi,
            smoothing_factor=smoothing_factor,
            major_ticks=major_ticks,
            minor_ticks=minor_ticks,
            x_limits_from=x_limits_from,
            x_limits_to=x_limits_to,
            y_limits_from=y_limits_from,
            y_limits_to=y_limits_to,
            contour_start=contour_start,
            contour_end=contour_end,
            contour_step=contour_step)

        random_plot(
            [ar_fractions, size_fractions],
            [{"width": 0.04, "x-axis-label": "aspect ratio", "y-axis-label": "probability"},
             {"width":  1.5, "x-axis-label":         "size", "y-axis-label": "probability"}
            ],
            [random_plot_png, random_plot_pdf, random_plot_jpg]
        )

        generate_forc_loops_plot(
            combined_loops,
            [f for f in [forc_loops_plot_png, forc_loops_plot_pdf, forc_loops_plot_jpg] if f is not None],
            dpi=dpi)

        message = "Finished!"
        if json_output:
            response = Response()
            response.status = ResponseStatusEnum.SUCCESS.value
            response.forc_png = forc_plot_png
            response.forc_loop_png = forc_loops_plot_png
            response.message = message
            print(json.dumps(response.to_primitive()))
        else:
            print(message)

    except BinsEmptyException as e:
        message = "Empty bins when calculating distribution weights."
        if json_output:
            response = Response()
            response.status = ResponseStatusEnum.EMPTY_BINS.value
            response.message = message
            response.exception = str(e)
            print(json.dumps(response.to_primitive()))
        else:
            print(message)
        sys.exit(1)

    except Exception as e:
        logger.debug(str(e))
        message = "Error running code!"
        if json_output:
            response = Response()
            response.status = ResponseStatusEnum.EXCEPTION.value
            response.message = message
            response.exception = str(e)
            print(json.dumps(response.to_primitive()))
        else:
            print(message)
        sys.exit(1)

def main():
    app()


if __name__ == "__main__":
    main()
