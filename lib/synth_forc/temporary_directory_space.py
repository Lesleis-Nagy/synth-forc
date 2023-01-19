import os

from synth_forc.plotting.forc import generate_forc_plot
from synth_forc.plotting.forc_loops import generate_forc_loops_plot
from synth_forc.plotting.log_normal import log_normal_plot

class TemporaryDirectorySpaceManager:
    r"""
    Class to hold temporary workspace items.
    """

    size_distribution_plot_file_name = "size_distribution_plot.png"
    aratio_distribution_plot_file_name = "aratio_distribution_plot.png"
    forc_plot_name = "forc.png"
    forc_loops_plot_name = "forc_loops.png"

    def __init__(self, root_dir):
        self.root_dir = root_dir

        self.size_distribution_plot = None
        self.aratio_distribution_plot = None
        self.forc_plot = None
        self.forc_loops_plot = None

    def create_size_distribution_plot(self, shape, location, scale, bins=None):
        if shape is None or location is None or scale is None:
            pass
        size_distribution_plot = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.size_distribution_plot_file_name)
        log_normal_plot(shape, location, scale, size_distribution_plot, bins)
        self.size_distribution_plot = size_distribution_plot

    def create_aratio_distribution_plot(self, shape, location, scale, bins=None):
        if shape is None or location is None or scale is None:
            pass
        aratio_distribution_plot = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.aratio_distribution_plot_file_name)
        log_normal_plot(shape, location, scale, aratio_distribution_plot, bins)
        self.aratio_distribution_plot = aratio_distribution_plot

    def create_forc_and_forc_loops_plot(self, synthforc_db, ar_shape, ar_location, ar_scale, size_shape, size_location, size_scale):
        if synthforc_db is None or ar_shape is None or ar_location is None or ar_scale is None or size_shape is None or size_location is None or size_scale is None:
            pass
        forc_plot = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_plot_name)
        forc_loops_plot = os.path.join(self.root_dir, TemporaryDirectorySpaceManager.forc_loops_plot_name)

        combined_loops = synthforc_db.combine_loops(ar_shape, ar_location, ar_scale, size_shape, size_location, size_scale)
        generate_forc_plot(combined_loops, forc_plot)
        self.forc_plot = forc_plot

        generate_forc_loops_plot(combined_loops, forc_loops_plot)
        self.forc_loops_plot = forc_loops_plot
