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
# Authors: Miguel A. Valdez-Grijalva, W. Williams, L. Nagy, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#
# Notes: Based on original code by MA Valdez-Grijalva (see: Earth Planet Sci. Lett. 2018 (501) 103-111).
#        Changes by W. Williams
#        Additional small changes by L. Nagy.
#

import numpy as np
import scipy.linalg
from scipy.interpolate import interp2d
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FormatStrFormatter
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.pyplot import get_cmap
import os

from synth_forc.settings import Settings


def read_frc(forc_loops):
    # find the major loop dimension (i.e. list of field values on major loop)
    minor_loops = forc_loops.groupby(forc_loops.Br)
    minor_loop_lengths = [minor_loop[1].shape[0] for minor_loop in minor_loops]
    max_minor_loop_length = max(minor_loop_lengths)

    # Create a numpy square array of the correct size for data, and fill with zeros
    myFORC = np.zeros((max_minor_loop_length, max_minor_loop_length))

    # Iterate though dataframe and populate numpy array
    field = None

    for i, minor_loop in enumerate(reversed(tuple(minor_loops))):
        df = minor_loop[1]
        df = df.iloc[::-1]
        for j, M in enumerate(df["M"].tolist()):
            myFORC[i][max_minor_loop_length - 1 - j] = M

        # If this is the maximal loop.
        if minor_loop[1].shape[0] == max_minor_loop_length:
            field = df["B"].tolist()

    return myFORC, field


def append_new_line(file_name, text_to_append):
    """Append given text as a new line at the end of file"""
    # Open the file in append & read mode ('a+')
    with open(file_name, "a+") as file_object:
        # Move read cursor to the start of file.
        file_object.seek(0)
        # If file is not empty then append '\n'
        data = file_object.read(100)
        if len(data) > 0:
            file_object.write("\n")
        # Append text at the end of file
        file_object.write(text_to_append)


def forc_distribution(m, Bb, Ba, sf):
    def in_grid(i, j, sf, n):
        grid = []
        for k in range(i - sf, i + sf + 1):
            for l in range(j - sf, j + sf + 1):
                if in_triangle(k, l, n) and in_square(k, l, n):
                    grid.append((k, l))
        return tuple(grid)

    def in_triangle(i, j, n):
        return j >= (n - 1) - i

    def in_square(i, j, n):
        return i <= n - 1 and j <= n - 1

    rho = np.zeros_like(m)
    for i in range(len(m)):
        for j in range(len(m) - i, len(m)):
            grid = in_grid(i, j, sf, len(m))
            data = []
            for indices in grid:
                data.append(
                    np.array([Bb[indices[0]][indices[1]], Ba[indices[0]][indices[1]], m[indices[0]][indices[1]]]))
            data = np.array(data)
            A = np.c_[np.ones(data.shape[0]), data[:, :2], np.prod(data[:, :2], axis=1), data[:, :2] ** 2]
            C, _, _, _ = scipy.linalg.lstsq(A, data[:, 2])
            rho[i][j] = -C[3] / 2.0

    return rho / np.max(rho)


def plot_forc_distribution(
        Bb, Ba, rho,
        xlim, ylim,
        major, minor,
        shiftedCMap,
        anotate,
        contour_start=0.1, contour_end=1.1, contour_step=0.3):
    # Normalizing the distribution
    rhomin = np.min(rho)

    for i in range(len(rho)):
        for j in range(len(rho[0])):
            if rho[i][j] < 0.:
                rho[i][j] /= -rhomin

    Bc, Bu = np.meshgrid(np.linspace(0., np.max(Bb), 2 * len(Bb)), np.linspace(np.max(Bb), np.min(Bb), 2 * len(Bb)))

    # Interpolator function
    I = interp2d(Bb[0], Ba[:, 0], rho, kind='cubic', fill_value=np.NaN)

    F = np.zeros_like(Bc)

    for i in range(len(Bc)):
        for j in range(len(Bc)):
            F[i, j] = I(Bu[i, j] + Bc[i, j], Bu[i, j] - Bc[i, j])

    # Plot
    fig, ax = plt.subplots()

    # Contour levels
    levels = np.arange(contour_start, contour_end, contour_step)
    levels = np.concatenate((-1.0 * levels[::-1], levels))

    figure = plt.contourf(Bc, Bu, F, levels=levels, cmap=shiftedCMap, extend='both')
    contours = plt.contour(Bc, Bu, F, levels=levels, colors='k', linewidths=0.2, extend='both')

    # Display parameters
    plt.plot([0., np.max(Bb)], [0., 0.], color='black', linewidth=0.5, linestyle='--')

    fontsize = "medium"
    plt.xlabel(r'$B_c\, (\mathrm{mT})$', fontsize=fontsize)
    plt.ylabel(r'$B_u\, (\mathrm{mT})$', fontsize=fontsize, rotation='vertical')

    plt.xlim(xlim[0], xlim[1])
    plt.ylim(ylim[0], ylim[1])

    majorLocator = MultipleLocator(major)
    majorFormatter = FormatStrFormatter('%d')
    minorLocator = MultipleLocator(minor)
    ax.xaxis.set_major_locator(majorLocator)
    ax.xaxis.set_major_formatter(majorFormatter)
    ax.xaxis.set_minor_locator(minorLocator)
    plt.xticks(rotation=45)

    majorLocator = MultipleLocator(major)
    majorFormatter = FormatStrFormatter('%d')
    minorLocator = MultipleLocator(minor)
    ax.yaxis.set_major_locator(majorLocator)
    ax.yaxis.set_major_formatter(majorFormatter)
    ax.yaxis.set_minor_locator(minorLocator)

    # Add colorbar
    clb = plt.colorbar(figure)
    clb.add_lines(contours)
    clb.set_ticks(levels)

    labels = [r'-1.0 ($\times${:5.3f})'.format(round(abs(rhomin), 3))]
    labels += ['{:4.1f}'.format(l) for l in levels[1:]]
    clb.set_ticklabels(labels)
    clb.ax.set_title(r'$\rho$', y=1.01, x=-0.4)

    ax.set_aspect('equal')
    x = .04
    y = .85
    for names in anotate:
        plt.figtext(x, y, names)
        y -= .03
    plt.tight_layout()
    return fig, ax


def shifted_color_map(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    '''
    Function to offset the "center" of a colormap. Useful for
    data with a negative min and positive max and you want the
    middle of the colormap's dynamic range to be at zero

    Input
    -----
      cmap : The matplotlib colormap to be altered
      start : Offset from lowest point in the colormap's range.
          Defaults to 0.0 (no lower ofset). Should be between
          0.0 and `midpoint`.
      midpoint : The new center of the colormap. Defaults to
          0.5 (no shift). Should be between 0.0 and 1.0. In
          general, this should be  1 - vmax/(vmax + abs(vmin))
          For example if your data range from -15.0 to +5.0 and
          you want the center of the colormap at 0.0, `midpoint`
          should be set to  1 - 5/(5 + 15)) or 0.75
      stop : Offset from highets point in the colormap's range.
          Defaults to 1.0 (no upper ofset). Should be between
          `midpoint` and 1.0.
    '''
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }

    # regular index to compute the colors
    reg_index = np.linspace(start, stop, 257)

    # shifted index to match the data
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False),
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])

    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)

        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))

    newcmap = LinearSegmentedColormap(name, cdict)

    plt.register_cmap(cmap=newcmap)

    return newcmap


def generate_forc_plot(forc_loops, output_files, smoothing_factor=3, dpi=None, annotate=None):
    settings = Settings.get_settings()

    shiftedCMap = shifted_color_map(get_cmap("RdBu_r"), midpoint=(0.5))

    # Read generic FORC format
    mforc, Bfield = read_frc(forc_loops)

    Bfield = [i * 1000 for i in Bfield]
    Bfield.reverse()

    # Calculate forc distribution
    Bb, Ba = np.meshgrid(Bfield, Bfield[::-1])
    rho = forc_distribution(mforc, Bb, Ba, smoothing_factor)

    if annotate is None:
        annotate = []

    # Plot the forc distribution
    fig, ax = plot_forc_distribution(
        Bb, Ba, rho,
        [settings.x_limits_from, settings.x_limits_to], [settings.y_limits_from, settings.y_limits_to],
        settings.major_ticks, settings.minor_ticks,
        shiftedCMap, annotate,
        contour_start=settings.contour_start,
        contour_end=settings.contour_end,
        contour_step=settings.contour_step)

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


