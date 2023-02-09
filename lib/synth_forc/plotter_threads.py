import json

from PyQt6.QtCore import QRunnable, QMetaObject, Qt, Q_ARG

from subprocess import Popen
from subprocess import PIPE


class ImageGenerationException(Exception):
    def __init__(self, json, stderr):
        self.json = json
        self.stderr = stderr


class GenerateForcImages(QRunnable):
    r"""
    Generate a FORC image.
    """

    def __init__(self, thread_id, data_file, ar_shape, ar_location, ar_scale, size_shape, size_location, size_scale,
                 forc_plot_png, forc_plot_pdf, forc_plot_jpg, forc_loops_plot_png, forc_loops_plot_pdf,
                 forc_loops_plot_jpg, smoothing_factor, dpi, parent):
        super().__init__()

        self.thread_id = thread_id
        self.data_file = data_file
        self.ar_shape = ar_shape
        self.ar_location = ar_location
        self.ar_scale = ar_scale
        self.size_shape = size_shape
        self.size_location = size_location
        self.size_scale = size_scale
        self.forc_plot_png = forc_plot_png
        self.forc_plot_pdf = forc_plot_pdf
        self.forc_plot_jpg = forc_plot_jpg
        self.forc_loops_plot_png = forc_loops_plot_png
        self.forc_loops_plot_pdf = forc_loops_plot_pdf
        self.forc_loops_plot_jpg = forc_loops_plot_jpg
        self.smoothing_factor = smoothing_factor
        self.dpi = dpi
        self.parent = parent

    def run(self) -> None:
        proc = Popen(
            ["synth-forc-cli",
             "log-normal",
             self.data_file,
             str(self.ar_shape),
             str(self.ar_location),
             str(self.ar_scale),
             str(self.size_shape),
             str(self.size_location),
             str(self.size_scale),
             "--forc-plot-png", self.forc_plot_png,
             "--forc-plot-pdf", self.forc_plot_pdf,
             "--forc-plot-jpg", self.forc_plot_jpg,
             "--forc-loops-plot-png", self.forc_loops_plot_png,
             "--forc-loops-plot-pdf", self.forc_loops_plot_pdf,
             "--forc-loops-plot-jpg", self.forc_loops_plot_jpg,
             "--smoothing-factor", str(self.smoothing_factor),
             "--dpi", str(self.dpi),
             "--json-output"],
            stdout=PIPE, stderr=PIPE, universal_newlines=True)

        stdout, stderr = proc.communicate()

        # QMetaObject.invokeMethod(self.parent,
        #                          "forc_generation_complete",
        #                          Qt.ConnectionType.QueuedConnection,
        #                          Q_ARG(str, json.dumps(
        #                              {"stdout": json.loads(stdout), "stderr": stderr},
        #                          )))

        QMetaObject.invokeMethod(self.parent,
                                 "forc_generation_complete",
                                 Qt.ConnectionType.QueuedConnection,
                                 Q_ARG(str, stdout), Q_ARG(str, stderr))