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
# File: main_window.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import pathlib
import re
import json

from synth_forc.cli.response import Response
from synth_forc.cli.response import ResponseStatusEnum
from synth_forc.qt.main_window import Ui_MainWindow

from PyQt6 import QtGui, QtCore

from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QRegularExpressionValidator

from PyQt6.QtCore import QCoreApplication, QRunnable, QThreadPool, pyqtSlot, QRectF
from PyQt6.QtCore import QRegularExpression
from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog
from PyQt6.QtWidgets import QGraphicsPixmapItem

from PIL import Image, ImageQt

from synth_forc.settings import Settings
from synth_forc.gui.settings_dialog import SettingsDialog
from synth_forc.gui.save_dialog import SaveDialog
from synth_forc.synthforc_db import SynthForcDB
from synth_forc.temporary_directory_space import TemporaryDirectorySpaceManager
from synth_forc.plotting.log_normal import BinsEmptyException
from synth_forc.gui.spinner import QtWaitingSpinner

from synth_forc.plotter_threads import GenerateForcImages

from synth_forc.logger import get_logger


class MainWindow(QMainWindow, Ui_MainWindow):

    re_float = QRegularExpression(r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")
    re_integer = QRegularExpression(r"[0-9]+")

    def __init__(self, temp_dir):

        self.logger = get_logger()

        QMainWindow.__init__(self)
        self.logger.debug("'QMainWindow' is initialized.")

        Ui_MainWindow.__init__(self)
        self.logger.debug("'Ui_MainWindow' is initialized.")

        self.setupUi(self)
        self.logger.debug("User interface has been set up.")

        self.temp_dir = temp_dir
        self.db_file = None
        self.synthforc_db = None
        self.forc_save_file = None
        self.forc_loops_save_file = None
        self.size_distr_save_file = None
        self.aratio_distr_save_file = None
        self.logger.debug("Local variables have been initialized.")

        self.temp_dir_space_manager = TemporaryDirectorySpaceManager(self.temp_dir)
        self.logger.debug(f"'self.temp_dir_space_manager' has been created with self.temp_dir: {self.temp_dir}.")

        self.settings = Settings.get_settings()
        self.logger.debug("'self.settings' has been created.")

        self.btn_generate.clicked.connect(self.btn_generate_action)
        self.logger.debug("'self.btn_generate.clicked' event has been connected to action 'self.btn_generate_action'")

        self.txt_size_distr_shape.textChanged.connect(self.txt_size_distr_shape_change_action)
        self.logger.debug("'self.txt_size_distr_shape.textChanged' event has been connected to action 'self.txt_size_distr_shape_change_action'")

        self.txt_size_distr_location.textChanged.connect(self.txt_size_distr_location_change_action)
        self.logger.debug("'self.txt_size_distr_location.textChanged' event has been connected to action 'self.txt_size_distr_location_change_action'")

        self.txt_size_distr_scale.textChanged.connect(self.txt_size_distr_scale_change_action)
        self.logger.debug("'self.txt_size_distr_scale.textChanged' event has been connected to action 'self.txt_size_distr_scale_change_action'")

        self.txt_aratio_distr_shape.textChanged.connect(self.txt_aratio_distr_shape_change_action)
        self.logger.debug("'self.txt_aratio_distr_shape.textChanged' event has been connected to action 'self.txt_aratio_distr_shape_change_action'")

        self.txt_aratio_distr_location.textChanged.connect(self.txt_aratio_distr_location_change_action)
        self.logger.debug("'self.txt_aratio_distr_location.textChanged' event has been connected to action 'self.txt_aratio_distr_location_change_action'")

        self.txt_aratio_distr_scale.textChanged.connect(self.txt_aratio_scale_change_action)
        self.logger.debug("'self.txt_aratio_distr_scale.textChanged' event has been connected to action 'self.txt_aratio_scale_change_action'")

        self.menu_configure.triggered.connect(self.menu_configure_action)
        self.logger.debug("'self.menu_configure.triggered' event has been connected to action 'self.menu_configure_action'")

        self.menu_close.triggered.connect(self.menu_close_action)
        self.logger.debug("'self.menu_close.triggered' event has been connected to action 'self.menu_close_action'")

        self.menu_save.triggered.connect(self.menu_save_action)
        self.logger.debug("'self.menu_save.triggered' event has been connected to action 'self.menu_save_action'")

        self.menu_load.triggered.connect(self.menu_load_action)
        self.logger.debug("'self.menu_load.triggered' event has been connected to action 'self.menu_load_action'")

        self.logger.debug(f"self.graphics_size_distribution size: {self.graphics_size_distribution.sceneRect().width()}, {self.graphics_size_distribution.sceneRect().height()}")

        self.size_distr_scene = QGraphicsScene(self)
        self.logger.debug(f"Created self.size_distr_scene: {self.size_distr_scene}")

        self.graphics_size_distribution.setScene(self.size_distr_scene)
        self.logger.debug(f"Set graphics_size_distribution scene")

        self.size_distr_pixmap = self.size_distr_scene.addPixmap(QPixmap())
        self.logger.debug(f"Created self.size_distr_pixmap: {self.size_distr_pixmap}")

        self.logger.debug(f"self.graphics_aratio_distribution size: {self.graphics_aratio_distribution.sceneRect().width()}, {self.graphics_aratio_distribution.sceneRect().height()}")

        self.aratio_distr_scene = QGraphicsScene(self)
        self.logger.debug(f"Created self.aratio_distr_scene: {self.aratio_distr_scene}")

        self.graphics_aratio_distribution.setScene(self.aratio_distr_scene)
        self.logger.debug(f"Set graphics_aratio_distribution scene")

        self.aratio_distr_pixmap = self.aratio_distr_scene.addPixmap(QPixmap())
        self.logger.debug(f"Created self.aratio_distr_pixmap: {self.aratio_distr_pixmap}")

        self.graphics_aratio_distribution.pixmap = self.aratio_distr_pixmap

        self.forc_scene = QGraphicsScene(self)
        self.graphics_forcs.setScene(self.forc_scene)
        self.forc_pixmap = self.forc_scene.addPixmap(QPixmap())

        self.forc_loops_scene = QGraphicsScene(self)
        self.graphics_loops.setScene(self.forc_loops_scene)
        self.forc_loops_pixmap = self.forc_loops_scene.addPixmap(QPixmap())

        self.txt_size_distr_shape.setValidator(QRegularExpressionValidator(MainWindow.re_float))
        self.txt_size_distr_location.setValidator(QRegularExpressionValidator(MainWindow.re_float))
        self.txt_size_distr_scale.setValidator(QRegularExpressionValidator(MainWindow.re_float))

        self.txt_aratio_distr_shape.setValidator(QRegularExpressionValidator(MainWindow.re_float))
        self.txt_aratio_distr_location.setValidator(QRegularExpressionValidator(MainWindow.re_float))
        self.txt_aratio_distr_scale.setValidator(QRegularExpressionValidator(MainWindow.re_float))

        self.txt_smoothing_factor.setValidator(QRegularExpressionValidator(MainWindow.re_integer))

        self.spinner = QtWaitingSpinner(self)

        self.initialise_distribution_plots()

    def set_forc_image(self, image, no_adjust=False):
        logger = self.logger

        # FORC plot
        forc_image = Image.open(image)
        forc_image_width, forc_image_height = forc_image.size
        if not no_adjust:
            forc_image = forc_image.crop((1200, 0, forc_image_width - 150, forc_image_height))
        forc_qimage = ImageQt.ImageQt(forc_image)

        width, height = (self.graphics_forcs.geometry().width(), self.graphics_forcs.geometry().height())

        logger.debug(f"width: {width}, height: {height}")

        self.forc_pixmap.setPixmap(QtGui.QPixmap.fromImage(forc_qimage))
        self.graphics_forcs.resetTransform()
        self.graphics_forcs.scale(0.15, 0.15)

    def set_forc_loops_image(self, image):

        # FORC loops plot
        forc_loops_image = Image.open(image)
        # forc_loops_width, forc_loops_height = forc_loops_image.size
        forc_loops_qimage = ImageQt.ImageQt(forc_loops_image)
        self.forc_loops_pixmap.setPixmap(QtGui.QPixmap.fromImage(forc_loops_qimage))
        self.graphics_loops.resetTransform()
        self.graphics_loops.scale(0.15, 0.15)

    def btn_generate_action(self):

        if self.db_file is None and self.synthforc_db is None:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("No database file set.")
            dlg.setText("A file containing FORC data has not been loaded. " 
                        "Please load a synth-FORC file using the 'File' menu")
            dlg.exec()
        else:
            pool = QThreadPool.globalInstance()

            self.spinner.start()

            pool.start(
                GenerateForcImages(
                    1, self, self.logger
                )
            )

    @pyqtSlot(str, str)
    def forc_generation_complete(self, stdout: str, stderr: str):
        logger = self.logger

        self.spinner.stop()

        logger.debug(f"stdout: {stdout}")
        logger.debug(f"stderr: {stderr}")

        response = Response(json.loads(stdout))

        if response.status == ResponseStatusEnum.EMPTY_LOOPS.value:
            print("Empty loops")
        elif response.status == ResponseStatusEnum.SUCCESS.value:

            # Display the images.
            self.set_forc_image(response.forc_png)
            self.set_forc_loops_image(response.forc_loop_png)

        elif response.status == ResponseStatusEnum.EMPTY_BINS.value:

            # Display empty images
            self.set_forc_image(self.temp_dir_space_manager.empty_image_png, no_adjust=True)
            self.set_forc_loops_image(self.temp_dir_space_manager.empty_image_png)

        elif response.status == ResponseStatusEnum.EXCEPTION.value:
            print(response.exception)
        else:
            print("Unknown error occurred")
            QCoreApplication.quit()

    def menu_configure_action(self):
        dlg = SettingsDialog(self.settings)
        dlg.exec()

    def menu_close_action(self):
        QCoreApplication.quit()

    def menu_load_action(self):
        if self.db_file is None:
            start_dir = str(pathlib.Path.home())
        else:
            start_dir = str(pathlib.Path(self.db_file).parents[0])

        db_file = QFileDialog.getOpenFileNames(self, 'Open file', start_dir)

        if db_file[0] and len(db_file[0]) == 1:
            self.synthforc_db = SynthForcDB(db_file[0][0])
            self.db_file = db_file[0][0]

            self.update_size_distribution_plot()
            self.update_aratio_distribution_plot()

            print(self.synthforc_db.aratios)

    def txt_size_distr_shape_change_action(self, text):
        self.update_size_distribution_plot()

    def txt_size_distr_location_change_action(self, text):
        self.update_size_distribution_plot()

    def txt_size_distr_scale_change_action(self, text):
        self.update_size_distribution_plot()

    def txt_aratio_distr_shape_change_action(self, text):
        self.update_aratio_distribution_plot()

    def txt_aratio_distr_location_change_action(self, text):
        self.update_aratio_distribution_plot()

    def txt_aratio_scale_change_action(self, text):
        self.update_aratio_distribution_plot()

    def get_size_distr_shape(self):
        try:
            return float(self.txt_size_distr_shape.text())
        except ValueError:
            return None

    def get_size_distr_location(self):
        try:
            return float(self.txt_size_distr_location.text())
        except ValueError:
            return None

    def get_size_distr_scale(self):
        try:
            return float(self.txt_size_distr_scale.text())
        except ValueError:
            return None

    def get_aratio_distr_shape(self):
        try:
            return float(self.txt_aratio_distr_shape.text())
        except ValueError:
            return None

    def get_aratio_distr_location(self):
        try:
            return float(self.txt_aratio_distr_location.text())
        except ValueError:
            return None

    def get_aratio_distr_scale(self):
        try:
            return float(self.txt_aratio_distr_scale.text())
        except ValueError:
            return None

    def initialise_distribution_plots(self):
        self.update_size_distribution_plot()
        self.update_aratio_distribution_plot()

    def set_size_image(self, image):
        image = Image.open(image)
        width, height = image.size
        qimage = ImageQt.ImageQt(image)
        self.size_distr_pixmap.setPixmap(QtGui.QPixmap.fromImage(qimage))
        self.graphics_size_distribution.resetTransform()
        self.graphics_size_distribution.scale(0.15, 0.15)

    def update_size_distribution_plot(self):

        if self.db_file is None and self.synthforc_db is None:
            size_bins = None
        else:
            size_bins = self.synthforc_db.sizes

        # If any of the text boxes associated with the image are empty, then don't display.
        if self.txt_size_distr_scale.text() == "" or \
                self.txt_size_distr_shape.text() == "" or \
                self.txt_size_distr_location.text() == "":
            self.set_size_image(self.temp_dir_space_manager.empty_image_png)
            return

        # If there is a BinsEmptyException then don't display.
        try:
            self.temp_dir_space_manager.create_size_distribution_plot(
                self.get_size_distr_shape(), self.get_size_distr_location(), self.get_size_distr_scale(), size_bins
            )
        except BinsEmptyException as e:
            self.set_size_image(self.temp_dir_space_manager.empty_image_png)
            return

        if self.temp_dir_space_manager.size_distribution_plot_png is not None:
            self.set_size_image(self.temp_dir_space_manager.size_distribution_plot_png)

    def set_aratio_image(self, image):
        logger = self.logger

        scene_rect = self.graphics_aratio_distribution.sceneRect()
        logger.debug(
            f"'self.graphics_aratio_distribution' graphics coordinates {scene_rect.width()}, {scene_rect.height()}.")

        pil_image = Image.open(image)
        logger.debug(f"Loaded image in to PIL Image object {pil_image.size}.")

        pil_image = pil_image.crop((0, 0, 3840, 3840))
        logger.debug(f"Cropped image to {pil_image.size}.")

        qimage = ImageQt.ImageQt(pil_image)
        logger.debug("Created ImageQT object from PIL Image.")

        #
        # qpixmap = QPixmap.fromImage(qimage)
        # logger.debug("Created QPixmap from ImageQT object.")
        #
        # qpixmap = qpixmap.scaledToWidth(int(scene_rect.width()))
        # logger.debug(f"Scaled qpixmap to scene_rect.width() ({scene_rect.width()})")
        #
        # qgraphics_pixmap_itm = self.aratio_distr_scene.addPixmap(QPixmap.fromImage(qpixmap.toImage()))
        #
        # self.graphics_aratio_distribution.fitInView(qgraphics_pixmap_itm)
        #

        self.aratio_distr_pixmap.setPixmap(QtGui.QPixmap.fromImage(qimage))
        self.graphics_aratio_distribution.resetTransform()
        self.graphics_aratio_distribution.scale(scene_rect.width()/pil_image.size[0],
                                                scene_rect.height()/pil_image.size[1])

    def update_aratio_distribution_plot(self):

        if self.db_file is None and self.synthforc_db is None:
            aratio_bins = None
        else:
            aratio_bins = self.synthforc_db.aratios

        # If any of the text boxes associated with the image are empty, then don't display.
        if self.txt_aratio_distr_scale.text() == "" or \
                self.txt_aratio_distr_shape.text() == "" or \
                self.txt_aratio_distr_location.text() == "":
            self.set_aratio_image(self.temp_dir_space_manager.empty_image_png)
            return

        # If there is a BinsEmptyException then don't display.
        try:
            self.temp_dir_space_manager.create_aratio_distribution_plot(
                self.get_aratio_distr_shape(), self.get_aratio_distr_location(), self.get_aratio_distr_scale(), aratio_bins
            )
        except BinsEmptyException as e:
            self.set_aratio_image(self.temp_dir_space_manager.empty_image_png)
            return

        if self.temp_dir_space_manager.aratio_distribution_plot_png is not None:
            self.set_aratio_image(self.temp_dir_space_manager.aratio_distribution_plot_png)

    def menu_save_action(self):
        dlg = SaveDialog(self,
                         self.temp_dir_space_manager,
                         self.forc_save_file,
                         self.forc_loops_save_file,
                         self.size_distr_save_file,
                         self.aratio_distr_save_file)

        dlg.exec()

        # Retrieve the FORC save file name.
        if not re.sub(r"\s+", "", dlg.txt_forc.text(), flags=re.UNICODE) == "":
            self.forc_save_file = dlg.txt_forc.text()
        else:
            self.forc_save_file = None

        # Retrieve the FORC loops save file name.
        if not re.sub(r"\s+", "", dlg.txt_forc_loops.text(), flags=re.UNICODE) == "":
            self.forc_loops_save_file = dlg.txt_forc_loops.text()
        else:
            self.forc_loops_save_file = None

        # Retrieve the size distribution file name.
        if not re.sub(r"\s+", "", dlg.txt_size_distribution.text(), flags=re.UNICODE) == "":
            self.size_distr_save_file = dlg.txt_size_distribution.text()
        else:
            self.size_distr_save_file = None

        # Retrieve the aspect ratio distribution file name.
        if not re.sub(r"\s+", "", dlg.txt_aspect_ratio_distribution.text(), flags=re.UNICODE) == "":
            self.aratio_distr_save_file = dlg.txt_aspect_ratio_distribution.text()
        else:
            self.aratio_distr_save_file = None

    def showEvent(self, a0: QtGui.QShowEvent) -> None:
        logger = self.logger

        logger.debug(f"self.graphics_aratio_distribution size: {self.graphics_aratio_distribution.sceneRect().width()}, {self.graphics_aratio_distribution.sceneRect().height()}")

    def resizeEvent(self, a0: QtGui.QResizeEvent) -> None:
        logger = self.logger

        logger.debug(f"Resizing window.")
        self.set_aratio_image(self.temp_dir_space_manager.aratio_distribution_plot_png)
