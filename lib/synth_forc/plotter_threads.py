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

    def __init__(self, thread_id: int, parent, logger):
        super().__init__()

        self.thread_id = thread_id
        self.parent = parent
        self.logger = logger

    # self.db_file, ar_shape, ar_location, ar_scale, size_shape, size_location, size_scale,
    # self.temp_dir_space_manager.forc_plot_png,
    # self.temp_dir_space_manager.forc_plot_pdf,
    # self.temp_dir_space_manager.forc_plot_jpg,
    # self.temp_dir_space_manager.forc_loops_plot_png,
    # self.temp_dir_space_manager.forc_loops_plot_pdf,
    # self.temp_dir_space_manager.forc_loops_plot_jpg,
    # smoothing_factor, self.settings.dpi, self

    def run(self) -> None:
        logger = self.logger

        db_file = self.parent.db_file
        ar_shape = float(self.parent.txt_aratio_distr_shape.text())
        ar_location = float(self.parent.txt_aratio_distr_location.text())
        ar_scale = float(self.parent.txt_aratio_distr_scale.text())
        size_shape = float(self.parent.txt_size_distr_shape.text())
        size_location = float(self.parent.txt_size_distr_location.text())
        size_scale = float(self.parent.txt_size_distr_scale.text())
        smoothing_factor = str(self.parent.txt_smoothing_factor.text())
        dpi = str(self.parent.settings.dpi)
        forc_plot_png = self.parent.temp_dir_space_manager.forc_plot_png
        forc_plot_pdf = self.parent.temp_dir_space_manager.forc_plot_pdf
        forc_plot_jpg = self.parent.temp_dir_space_manager.forc_plot_jpg
        forc_loops_plot_png = self.parent.temp_dir_space_manager.forc_loops_plot_png
        forc_loops_plot_pdf = self.parent.temp_dir_space_manager.forc_loops_plot_pdf
        forc_loops_plot_jpg = self.parent.temp_dir_space_manager.forc_loops_plot_jpg

        logger.debug(f"db_file: '{db_file}'")
        logger.debug(f"ar_shape: '{ar_shape}'")
        logger.debug(f"ar_location: '{ar_location}'")
        logger.debug(f"ar_scale: '{ar_scale}'")
        logger.debug(f"size_shape: '{size_shape}'")
        logger.debug(f"size_location: '{size_location}'")
        logger.debug(f"size_scale: '{size_scale}'")
        logger.debug(f"smoothing_factor: '{smoothing_factor}'")
        logger.debug(f"dpi: '{dpi}'")
        logger.debug(f"forc_plot_png: '{forc_plot_png}'")
        logger.debug(f"forc_plot_pdf: '{forc_plot_pdf}'")
        logger.debug(f"forc_plot_jpg: '{forc_plot_jpg}'")
        logger.debug(f"forc_loops_plot_png: '{forc_loops_plot_png}'")
        logger.debug(f"forc_loops_plot_pdf: '{forc_loops_plot_pdf}'")
        logger.debug(f"forc_loops_plot_jpg: '{forc_loops_plot_jpg}'")

        log_normal_cmd = f"synth-forc-cli log-normal " \
                         f"{db_file} " \
                         f"{ar_shape} " \
                         f"{ar_location} " \
                         f"{ar_scale} " \
                         f"{size_shape} " \
                         f"{size_location} " \
                         f"{size_scale} " \
                         f"--forc-plot-png {forc_plot_png} " \
                         f"--forc-plot-pdf {forc_plot_pdf} " \
                         f"--forc-plot-jpg {forc_plot_jpg} " \
                         f"--forc-loops-plot-png {forc_loops_plot_png} " \
                         f"--forc-loops-plot-pdf {forc_loops_plot_pdf} " \
                         f"--forc-loops-plot-jpg {forc_loops_plot_jpg} " \
                         f"--smoothing-factor {smoothing_factor} " \
                         f"--dpi {dpi} " \
                         f"--json-output"
        logger.debug(log_normal_cmd)

        proc = Popen(log_normal_cmd, stdout=PIPE, stderr=PIPE, shell=True, universal_newlines=True)

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
