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
# File: forc_loops.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023

import os
import matplotlib.pyplot as plt

from synth_forc.settings import Settings


def generate_forc_loops_plot(forc_loops, output_files, dpi=None):

    settings = Settings.get_settings()

    minor_loops = forc_loops.groupby(forc_loops.Br)

    fig, ax = plt.subplots()
    ax.set_xlabel("B (T)")
    ax.set_ylabel("M (A/m)")

    first_loop = True

    for key, minor_loop in minor_loops:
        ax.plot(minor_loop.B, minor_loop.M, c="black", linewidth=0.4)
        if first_loop:
            # Extract the major loop, reverse & flip it to complete the loop's 'top'.
            fl_B = list(reversed(minor_loop.B.tolist()))
            fl_M = [-1.0 * M for M in minor_loop.M.tolist()]
            ax.plot(fl_B, fl_M, c="black", linewidth=0.4)
            first_loop = False

    for output_file in output_files:
        extension = os.path.splitext(output_file)
        if extension[1] in [".png", ".jpg", ".jpeg"]:
            if dpi is not None:
                dpi = dpi
            else:
                dpi = settings.dpi
            fig.savefig(output_file, dpi=dpi)
            plt.close()
        else:
            fig.savefig(output_file)
            plt.close()
