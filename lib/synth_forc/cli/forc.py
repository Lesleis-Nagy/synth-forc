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

from synth_forc.plotting.log_normal import BinsEmptyException
from synth_forc.synthforc_db import SynthForcDB
from synth_forc.plotting.forc import generate_forc_plot
from synth_forc.plotting.forc_loops import generate_forc_loops_plot
from synth_forc.cli.response import Response
from synth_forc.cli.response import ResponseStatusEnum


app = typer.Typer()


@app.command()
def single(input_data_file: str = typer.Argument(..., help="Input file containing direction averaged FORC data."),
           aspect_ratio: float = typer.Argument(..., help="Aspect ratio of the grain."),
           size: float = typer.Argument(..., help="Size of the grain."),
           forc_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
           forc_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
           forc_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
           forc_loops_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
           forc_loops_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
           forc_loops_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
           smoothing_factor: int = typer.Option(3, help="Smoothing factor."),
           dpi: int = typer.Option(600, help="Resolution of the output image (only applies to PNG and JPG images)."),
           json_output: bool = typer.Option(False, help="Return the output response using JSON."),
           annotation=typer.Option(None, help="Some useful annotations.")):
    r"""
    Create a FORC diagram of a single grain based on data read from `input_data_file`.
    """
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

        generate_forc_plot(forc_loops, [
            forc_plot_png,
            forc_plot_pdf,
            forc_plot_jpg
        ], smoothing_factor=smoothing_factor, dpi=dpi, annotate=annotation)

        generate_forc_loops_plot(forc_loops, [
            forc_loops_plot_png,
            forc_loops_plot_pdf,
            forc_loops_plot_jpg
        ], dpi=dpi)

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

    finally:

        sys.exit(0)


@app.command()
def log_normal(input_data_file: str = typer.Argument(..., help="Input file containing direction averaged FORC data."),
               ar_shape: float = typer.Argument(..., help="Shape parameter of the aspect ratio distribution."),
               ar_location: float = typer.Argument(..., help="Location parameter of the aspect ratio distribution."),
               ar_scale: float = typer.Argument(..., help="Scale parameter of the aspect ratio distribution."),
               size_shape: float = typer.Argument(..., help="Shape parameter of the size distribution."),
               size_location: float = typer.Argument(..., help="Location parameter of the size distribution."),
               size_scale: float = typer.Argument(..., help="Scale parameter of the size distribution."),
               forc_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
               forc_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
               forc_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
               forc_loops_plot_png: str = typer.Option(None, help="Name of the forc plot output PNG file."),
               forc_loops_plot_pdf: str = typer.Option(None, help="Name of the forc plot output PDF file."),
               forc_loops_plot_jpg: str = typer.Option(None, help="Name of the forc plot output JPG file."),
               smoothing_factor: int = typer.Option(3, help="Smoothing factor."),
               dpi: int = typer.Option(600, help="Resolution of the output image (PNG & JPG only)."),
               json_output: bool = typer.Option(False, help="Return the output response using JSON.")):
    r"""
    Create a FORC diagram based on a size and aspect ratio distribution.
    """

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

        generate_forc_plot(combined_loops, [
            forc_plot_png,
            forc_plot_pdf,
            forc_plot_jpg
        ], dpi=dpi, smoothing_factor=smoothing_factor)

        generate_forc_loops_plot(combined_loops, [
            forc_loops_plot_png,
            forc_loops_plot_pdf,
            forc_loops_plot_jpg
        ], dpi=dpi)

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


def main():
    app()


if __name__ == "__main__":
    main()
