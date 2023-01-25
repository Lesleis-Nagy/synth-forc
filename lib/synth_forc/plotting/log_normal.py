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
# File: log_normal.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import numpy as np
from scipy.stats import lognorm
import matplotlib.pyplot as plt

from synth_forc.settings import Settings


def log_normal_plot(shape, location, scale, outputs, bins=None, x_axis_label=None, y_axis_label=None):
    r"""
    Routine to create a PDF plot of a log normal distribution.
    :param shape: the distribution's shape parameter.
    :param location: the distribution's location parameter.
    :param scale: the distribution's scale parameter.
    :param outputs: the output files.
    :param bins: the bin values
    :param x_axis_label: the x axis label.
    :param y_axis_label: the y axis label.
    :return: None
    """

    settings = Settings.get_settings()

    x = np.linspace(lognorm.ppf(0.01, shape, loc=location, scale=scale),
                    lognorm.ppf(0.99, shape, loc=location, scale=scale),
                    1000)

    rv = lognorm(shape, loc=location, scale=scale)

    fig, ax = plt.subplots()

    if x_axis_label:
        ax.set_xlabel(x_axis_label)
    if y_axis_label:
        ax.set_ylabel(y_axis_label)

    # Plot the background distribution
    ax.plot(x, rv.pdf(x), c="red", linewidth=2)

    # If bins has been give, then plot a bar for each bin.
    if bins is not None:
        mbd = min_bin_distance(bins)
        fractions, _ = log_normal_fractions(shape, location, scale, bins)

        bar_x = [p[0] for p in fractions]
        bar_y = [p[1] for p in fractions]

        ax.bar(bar_x, bar_y, width=mbd - mbd/2, color="black")

    for output in outputs:
        fig.savefig(output, dpi=settings.dpi)
    plt.close()


def log_normal_fractions(shape, location, scale, bins):
    r"""
    Routine to normalise a set of binned values to a log-normal plot.
    :param shape: the distribution's shape parameter.
    :param location: the distribution's location parameter.
    :param scale: the distribution's scale parameter.
    :param bins: the bin values (optional).
    :return:
    """

    rv = lognorm(shape, loc=location, scale=scale)

    bin_min = rv.ppf(0.01)
    bin_max = rv.ppf(0.99)

    fractions = [(bin, rv.pdf(bin)) for bin in bins if bin_min <= bin <= bin_max]
    nval = sum([p[1] for p in fractions])
    normed_fractions = [(p[0], p[1]/nval) for p in fractions]

    return fractions, normed_fractions


def min_bin_distance(bins):
    bins0 = bins[0:-1]
    bins1 = bins[1:]

    return min([abs(v[0] - v[1]) for v in zip(bins0, bins1)])


if __name__ == "__main__":
    log_normal_plot(0.3, 1.0, 90.0, "output.pdf", [45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160, 165, 170, 175, 180, 185, 190, 195, 200])
    log_normal_plot(0.9, 1.0, 0.8, "output2.pdf", [0.166667, 0.25, 0.5, 0.666667, 0.909091, 1, 1.05, 1.1, 1.15, 1.2, 1.25, 1.3, 1.35, 1.4, 1.45, 1.5, 1.55, 1.6, 1.65, 1.7, 1.75, 1.8, 1.85, 1.9, 1.95, 2, 2.25, 2.5, 2.75, 3, 4, 5, 6])

