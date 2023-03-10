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
# File: temporary_directory_space.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import os

from PIL import Image

from synth_forc.plotting.forc import generate_forc_plot
from synth_forc.plotting.forc_loops import generate_forc_loops_plot
from synth_forc.plotting.log_normal import log_normal_plot
from synth_forc.logger import get_logger

class TemporaryDirectorySpaceManager:
    r"""
    Class to manage temporary workspace items.
    """

    # Default name of the size-distribution graph png file.
    size_distribution_plot_file_name_png = "size_distribution_plot.png"
    # Default name of the size-distribution graph pdf file.
    size_distribution_plot_file_name_pdf = "size_distribution_plot.pdf"
    # Default name of the size-distribution graph jpg file.
    size_distribution_plot_file_name_jpg = "size_distribution_plot.jpg"

    # Default name of the aspect-ratio-distribution graph png file.
    aratio_distribution_plot_file_name_png = "aratio_distribution_plot.png"
    # Default name of the aspect-ratio-distribution graph pdf file.
    aratio_distribution_plot_file_name_pdf = "aratio_distribution_plot.pdf"
    # Default name of the aspect-ratio-distribution graph jpg file.
    aratio_distribution_plot_file_name_jpg = "aratio_distribution_plot.jpg"

    # Default name of the FORC diagram png file.
    forc_plot_name_png = "forc.png"
    # Default name of the FORC diagram pdf file.
    forc_plot_name_pdf = "forc.pdf"
    # Default name of the FORC diagram jpg file.
    forc_plot_name_jpg = "forc.jpg"

    # Default name of the FORC hysteresis loops png file.
    forc_loops_plot_name_png = "forc_loops.png"
    # Default name of the FORC hysteresis loops pdf file.
    forc_loops_plot_name_pdf = "forc_loops.pdf"
    # Default name of the FORC hysteresis loops jpg file.
    forc_loops_plot_name_jpg = "forc_loops.jpg"

    # Empty image name
    empty_name_png = "empty.png"

    def __init__(self, root_dir):
        r"""
        Initialise the temporary file/directory manager object.
        :param root_dir: the name of the temporary directory being managed.
        """

        self.logger = get_logger()

        self.root_dir = root_dir

        self.logger.debug(f"Temporary root dir: {self.root_dir}")

        self.size_distribution_plot_png = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.size_distribution_plot_file_name_png)
        self.size_distribution_plot_pdf = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.size_distribution_plot_file_name_pdf)
        self.size_distribution_plot_jpg = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.size_distribution_plot_file_name_jpg)

        self.aratio_distribution_plot_png = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.aratio_distribution_plot_file_name_png)
        self.aratio_distribution_plot_pdf = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.aratio_distribution_plot_file_name_pdf)
        self.aratio_distribution_plot_jpg = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.aratio_distribution_plot_file_name_jpg)

        self.forc_plot_png = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_plot_name_png)
        self.forc_plot_pdf = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_plot_name_pdf)
        self.forc_plot_jpg = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_plot_name_jpg)

        self.forc_loops_plot_png = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_loops_plot_name_png)
        self.forc_loops_plot_pdf = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_loops_plot_name_pdf)
        self.forc_loops_plot_jpg = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_loops_plot_name_jpg)

        image = Image.new('RGB', (3840, 2880), color="white")
        self.empty_image_png = os.path.join(root_dir, TemporaryDirectorySpaceManager.empty_name_png)
        image.save(self.empty_image_png, "PNG")

    def create_size_distribution_plot(self, shape, location, scale, bins=None):

        if shape is None or location is None or scale is None:
            return

        size_distribution_plot_png = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.size_distribution_plot_file_name_png)
        size_distribution_plot_pdf = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.size_distribution_plot_file_name_pdf)
        size_distribution_plot_jpg = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.size_distribution_plot_file_name_jpg)

        log_normal_plot(shape, location, scale, [
            size_distribution_plot_png,
            size_distribution_plot_pdf,
            size_distribution_plot_jpg
        ], bins, x_axis_label="size (nm)", y_axis_label="probability")

        self.size_distribution_plot_png = size_distribution_plot_png
        self.size_distribution_plot_pdf = size_distribution_plot_pdf
        self.size_distribution_plot_jpg = size_distribution_plot_jpg

    def create_aratio_distribution_plot(self, shape, location, scale, bins=None):

        if shape is None or location is None or scale is None:
            return

        aratio_distribution_plot_png = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.aratio_distribution_plot_file_name_png)
        aratio_distribution_plot_pdf = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.aratio_distribution_plot_file_name_pdf)
        aratio_distribution_plot_jpg = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.aratio_distribution_plot_file_name_jpg)

        log_normal_plot(shape, location, scale, [
            aratio_distribution_plot_png,
            aratio_distribution_plot_pdf,
            aratio_distribution_plot_jpg
        ], bins, x_axis_label="aspect ratio", y_axis_label="probability")

        self.aratio_distribution_plot_png = aratio_distribution_plot_png
        self.aratio_distribution_plot_pdf = aratio_distribution_plot_pdf
        self.aratio_distribution_plot_jpg = aratio_distribution_plot_jpg

    # def create_forc_and_forc_loops_plot(self, synthforc_db, ar_shape, ar_location, ar_scale, size_shape, size_location, size_scale, smoothing_factor):
    #     if synthforc_db is None or ar_shape is None or ar_location is None or ar_scale is None or size_shape is None or size_location is None or size_scale is None or smoothing_factor is None:
    #         return
    #
    #     forc_plot_png = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_plot_name_png)
    #     forc_plot_pdf = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_plot_name_pdf)
    #     forc_plot_jpg = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_plot_name_jpg)
    #
    #     forc_loops_plot_png = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_loops_plot_name_png)
    #     forc_loops_plot_pdf = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_loops_plot_name_pdf)
    #     forc_loops_plot_jpg = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_loops_plot_name_jpg)
    #
    #     combined_loops = synthforc_db.combine_loops(ar_shape, ar_location, ar_scale, size_shape, size_location, size_scale)
    #     generate_forc_plot(combined_loops, [
    #         forc_plot_png,
    #         forc_plot_pdf,
    #         forc_plot_jpg
    #     ], smoothing_factor=smoothing_factor)
    #
    #     self.forc_plot_png = forc_plot_png
    #     self.forc_plot_pdf = forc_plot_pdf
    #     self.forc_plot_jpg = forc_plot_jpg
    #
    #     generate_forc_loops_plot(combined_loops, [
    #         forc_loops_plot_png,
    #         forc_loops_plot_pdf,
    #         forc_loops_plot_jpg
    #     ])
    #
    #     self.forc_loops_plot_png = forc_loops_plot_png
    #     self.forc_loops_plot_pdf = forc_loops_plot_pdf
    #     self.forc_loops_plot_jpg = forc_loops_plot_jpg
