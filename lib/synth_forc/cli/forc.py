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
# File: forc.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import sys

import typer

from synth_forc.synthforc_db import SynthForcDB
from synth_forc.plotting.forc import generate_forc_plot

app = typer.Typer()


@app.command()
def draw_forc(input_data_file: str, aspect_ratio: float, size: float, output_file: str, annotation=None):
    r"""
    Create a drawing of a FORC diagram based on data read from `input_data_file`.
    :param input_data_file: the input data file containing direction averaged FORC data.
    :param aspect_ratio: the aspect ratio of the grain.
    :param size: the size of the grain.
    :param output_file: the output file.
    :param annotation: some useful annotation.
    :return:
    """
    synthforc_db = SynthForcDB(input_data_file)

    forc_loops = synthforc_db.single_forc_loops_by_aspect_ratio_and_size(aspect_ratio, size)
    if forc_loops.shape[0] == 0:
        print(f"No loops found for aspect ratio {aspect_ratio} and size {size}")
        sys.exit(1)
    print(f"Generating FORC plot: {output_file}")
    generate_forc_plot(forc_loops, [output_file], annotate=[f"Aspect ratio: {aspect_ratio:8.6f}", f"Size: {size}"])


def main():
    app()


if __name__ == "__main__":
    main()
