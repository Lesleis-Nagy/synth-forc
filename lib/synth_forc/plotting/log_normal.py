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
from scipy.integrate import quad
import matplotlib.pyplot as plt
from random import uniform

from synth_forc import GLOBAL
from synth_forc.logger import get_logger


class BinsEmptyException(Exception):
    pass


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

    # If bins has been given, then plot a bar for each bin.
    if bins is not None:
        mbd = min_bin_distance(bins)
        lgnorm_weights = log_normal_fractions(shape, location, scale, bins)

        bar_x = [p[0] for p in lgnorm_weights.display]
        bar_y = [p[1] for p in lgnorm_weights.display]

        ax.bar(bar_x, bar_y, width=mbd - mbd / 2, color="black")

    for output in outputs:
        fig.savefig(output, dpi=GLOBAL.DPI)
    plt.close()


class LogNormalWeights:
    def __init__(self, display=None, weights=None):
        self.display = display
        self.weights = weights


def log_normal_fractions(shape, location, scale, bins):
    r"""
    Routine to return a set of log-normal-normalised weight based on a set of binned values.
    :param shape: the distribution's shape parameter.
    :param location: the distribution's location parameter.
    :param scale: the distribution's scale parameter.
    :param bins: the bin values *MUST* be in ascending order.
    :return: a pair of lists:
                0) the first list contains tuples, where the first tuple-value is a bin value from `binned` and the
                   next value is a weight, based on the log-normal distribution.

                1) the second list contains tuples, where the first tuple-value is a bin value from `binned` and the
                   next value is a weight, based on the log-normal distribution but normalized so that all weights
                   sum to 1.
    """
    logger = get_logger()
    logger.debug(f"bins: {bins}")

    # Create the log-normal distribution.
    rv = lognorm(shape, loc=location, scale=scale)

    #bin_min = rv.ppf(0.01)
    #bin_max = rv.ppf(0.99)
    #logger.debug(f"bin_min: {bin_min}")
    #logger.debug(f"bin_max: {bin_max}")

    #bins = [b for b in bins if bin_min <= b <= bin_max]
    #logger.debug(f"bins (updated): {bins}")

    bin_min = min(bins)
    bin_max = max(bins)

    # Process the bins' midpoints.
    n = len(bins)
    if n == 0:
        raise BinsEmptyException()

    elif n == 1:

        # Since there is only one bin value, use that and set the weight to 1 in both instances.
        return LogNormalWeights(
            display=[(bins[0], rv.pdf(bins[0]))],
            weights=[(bins[0], 1.0)]
        )

    elif n == 2:
        # Two bin values is a special case.
        b0 = bins[0]
        b1 = bins[1]
        w0, _ = quad(rv.pdf, b0, (b0 + b1) / 2.0)
        w1, _ = quad(rv.pdf, (b0 + b1) / 2.0, b1)

        return LogNormalWeights (
            display=[(bins[0], rv.pdf(bins[0])), (bins[1], rv.pdf(bins[1]))],
            weights=[(bins[0], w0 / (w0 + w1)), (bins[1], w1 / (w0 + w1))]
        )

    else:
        # Create midpoint values.
        ms = [(m0+m1)/2.0 for (m0, m1) in zip(bins, bins[1:])]

        w0 = [quad(rv.pdf, bins[0], ms[0])[0]]
        ws = [quad(rv.pdf, ms[i-1], ms[i])[0] for i in range(1, n-1)]
        wn = [quad(rv.pdf, ms[n-2], bins[n-1])[0]]

        ws = w0 + ws + wn
        ws_sum = sum(ws)
        ws_normed = [w/ws_sum for w in ws]

        return LogNormalWeights(
            display=[(bin, rv.pdf(bin)) for bin in bins if bin_min <= bin <= bin_max],
            weights=list(zip(bins,ws_normed))
        )


def log_normal_fractions_by_height(shape, location, scale, bins):
    r"""
    Routine to normalise a set of binned values to a log-normal plot.
    :param shape: the distribution's shape parameter.
    :param location: the distribution's location parameter.
    :param scale: the distribution's scale parameter.
    :param bins: the bin values.
    :return:
    """

    rv = lognorm(shape, loc=location, scale=scale)

    bin_min = rv.ppf(0.01)
    bin_max = rv.ppf(0.99)

    fractions = [(bin, rv.pdf(bin)) for bin in bins if bin_min <= bin <= bin_max]
    nval = sum([p[1] for p in fractions])
    normed_fractions = [(p[0], p[1]/nval) for p in fractions]

    if len(normed_fractions) == 0:
        raise BinsEmptyException

    return LogNormalWeights(
        display=fractions,
        weights=normed_fractions
    )

def random_plot(data_lists, metadata, outputs):
    r"""
    Create a bar-plot of some data.
    :param data_lists: a list of lists of pairs (2-tuples) with the first item the x-axis data and the second item the
                       y-axis data.
    :param metadata: a list of metadata that will be used in the plot for each list in data_lists.
    :param outputs: output files to write the data to.
    """

    fig, axs = plt.subplots(1, len(data_lists))

    for idx, data_list in enumerate(data_lists):
        xs = [p[0] for p in data_list]
        ys = [p[1] for p in data_list]

        mditem = metadata[idx]

        axs[idx].set_xlabel(mditem["x-axis-label"])
        if idx == 0:
            axs[idx].set_ylabel(mditem["y-axis-label"])

        axs[idx].bar(xs, ys, width=mditem["width"])

    for output in outputs:
        if output is not None:
            fig.savefig(output, dpi=GLOBAL.DPI)
    plt.close()

def random_fractions_by_height(bins):
    r"""
    Routine to normalise a set of binned values to a log-normal plot.
    :param bins: the bin values.
    :return:
    """

    fractions = [(bin, uniform(0, 1)) for bin in bins]
    nval = sum([p[1] for p in fractions])
    normed_fractions = [(p[0], p[1]/nval) for p in fractions]

    if len(normed_fractions) == 0:
        raise BinsEmptyException

    return LogNormalWeights(
        display=fractions,
        weights=normed_fractions
    )


def min_bin_distance(bins):
    bins0 = bins[0:-1]
    bins1 = bins[1:]

    return min([abs(v[0] - v[1]) for v in zip(bins0, bins1)])
