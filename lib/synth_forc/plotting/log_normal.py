#
# @author L. Nagy
# @date   11 Jan 2023
#

import numpy as np
from scipy.stats import lognorm
import matplotlib.pyplot as plt

def log_normal_plot(shape, location, scale, output, bins=None):
    r"""
    Routine to create a PDF plot of a log normal distribution.
    :param shape: the distribution's shape parameter.
    :param location: the distribution's location parameter.
    :param scale: the distribution's scale parameter.
    :param output: the output PDF file.
    :param bins: the bin values
    :return: None
    """

    x = np.linspace(lognorm.ppf(0.01, shape, loc=location, scale=scale),
                    lognorm.ppf(0.99, shape, loc=location, scale=scale),
                    1000)

    rv = lognorm(shape, loc=location, scale=scale)

    fig, ax = plt.subplots()

    # Plot the background distribution
    ax.plot(x, rv.pdf(x), c="red", linewidth=2)

    # If bins has been give, then plot a bar for each bin.
    if bins is not None:
        mbd = min_bin_distance(bins)
        fractions, _ = log_normal_fractions(shape, location, scale, bins)

        bar_x = [p[0] for p in fractions]
        bar_y = [p[1] for p in fractions]

        ax.bar(bar_x, bar_y, width=mbd - mbd/2, color="black")

    fig.savefig(output, dpi=400)


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

