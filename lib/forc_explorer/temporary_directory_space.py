import os

from forc_explorer.plotting.log_normal import log_normal_plot

class TemporaryDirectorySpaceManager:
    r"""
    Class to hold temporary workspace items.
    """

    size_distribution_plot_file_name = "size_distribution_plot.png"
    aratio_distribution_plot_file_name = "aratio_distribution_plot.png"

    def __init__(self, root_dir):
        self.root_dir = root_dir

        self.size_distribution_plot = None
        self.aratio_distribution_plot = None

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




