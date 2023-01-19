import pathlib
import tempfile

import typer

from importlib import resources

from synth_forc.qt.main_window import Ui_MainWindow

from PyQt6 import QtCore

from PyQt6 import QtGui

from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QRegularExpressionValidator

from PyQt6.QtCore import QUrl
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtCore import QRegularExpression

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog

from PyQt6 import uic

#from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis

from PIL import Image, ImageQt, ImageEnhance

from synth_forc.settings import Settings
from synth_forc.gui.settings_dialog import SettingsDialog
from synth_forc.gui.save_dialog import SaveDialog
from synth_forc.synthforc_db import SynthForcDB
from synth_forc.temporary_directory_space import TemporaryDirectorySpaceManager

class MainWindow(QMainWindow, Ui_MainWindow):

    re_float = QRegularExpression(r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")

    def __init__(self, temp_dir):

        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        self.setupUi(self)

        self.temp_dir = temp_dir
        self.temp_dir_space_manager = TemporaryDirectorySpaceManager(self.temp_dir)
        self.settings = Settings.get_settings()
        self.db_file = None
        self.synthforc_db = None

        self.btn_generate.clicked.connect(self.btn_generate_action)

        self.txt_size_distr_shape.textChanged.connect(self.txt_size_distr_shape_change_action)
        self.txt_size_distr_location.textChanged.connect(self.txt_size_distr_location_change_action)
        self.txt_size_distr_scale.textChanged.connect(self.txt_size_distr_scale_change_action)

        self.txt_aratio_distr_shape.textChanged.connect(self.txt_aratio_distr_shape_change_action)
        self.txt_aratio_distr_location.textChanged.connect(self.txt_aratio_distr_location_change_action)
        self.txt_aratio_distr_scale.textChanged.connect(self.txt_aratio_scale_change_action)

        self.menu_configure.triggered.connect(self.menu_configure_action)
        self.menu_close.triggered.connect(self.menu_close_action)
        self.menu_save.triggered.connect(self.menu_save_action)
        self.menu_load.triggered.connect(self.menu_load_action)

        self.size_distr_scene = QGraphicsScene(self)
        self.graphics_size_distribution.setScene(self.size_distr_scene)
        self.size_distr_pixmap = self.size_distr_scene.addPixmap(QPixmap())

        self.aratio_distr_scene = QGraphicsScene(self)
        self.graphics_aratio_distribution.setScene(self.aratio_distr_scene)
        self.aratio_distr_pixmap = self.aratio_distr_scene.addPixmap(QPixmap())

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

        self.initialise_distribution_plots()

    def btn_generate_action(self):
        if self.db_file is None and self.synthforc_db is None:
            dlg = QMessageBox(self)
            dlg.setWindowTitle("No database file set.")
            dlg.setText("A file containing FORC data has not been loaded. " 
                        "Please load a synth-FORC file using the 'File' menu")
            dlg.exec()
        else:
            ar_shape = float(self.txt_aratio_distr_shape.text())
            ar_location = float(self.txt_aratio_distr_location.text())
            ar_scale = float(self.txt_aratio_distr_scale.text())
            size_shape = float(self.txt_size_distr_shape.text())
            size_location = float(self.txt_size_distr_location.text())
            size_scale = float(self.txt_size_distr_scale.text())

            self.temp_dir_space_manager.create_forc_and_forc_loops_plot(self.synthforc_db, ar_shape, ar_location, ar_scale, size_shape, size_location, size_scale)

            if self.temp_dir_space_manager.forc_plot is not None:
                # FORC plot
                forc_image = Image.open(self.temp_dir_space_manager.forc_plot)
                forc_image_width, forc_image_height = forc_image.size
                forc_image = forc_image.crop((1200, 0, forc_image_width - 150, forc_image_height))
                forc_qimage = ImageQt.ImageQt(forc_image)
                self.forc_pixmap.setPixmap(QtGui.QPixmap.fromImage(forc_qimage))
                self.graphics_forcs.resetTransform()
                self.graphics_forcs.scale(0.15, 0.15)

                # FORC loops plot
                forc_loops_image = Image.open(self.temp_dir_space_manager.forc_loops_plot)
                # forc_loops_width, forc_loops_height = forc_loops_image.size
                forc_loops_qimage = ImageQt.ImageQt(forc_loops_image)
                self.forc_loops_pixmap.setPixmap(QtGui.QPixmap.fromImage(forc_loops_qimage))
                self.graphics_loops.resetTransform()
                self.graphics_loops.scale(0.15, 0.15)

    def menu_configure_action(self):
        dlg = SettingsDialog(self)
        dlg.exec()

    def menu_close_action(self):
        QCoreApplication.quit()

    def menu_save_action(self):
        dlg = SaveDialog(self)
        dlg.exec()

    def menu_load_action(self):
        if self.db_file is None:
            start_dir = str(pathlib.Path.home())
        else:
            start_dir = str(pathlib.Path(self.db_file).parents[0])

        db_file = QFileDialog.getOpenFileNames(self, 'Open file', start_dir)

        if db_file[0]:
            if len(db_file[0]) == 1:
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

    def update_size_distribution_plot(self):
        if self.db_file is None and self.synthforc_db is None:
            size_bins = None
        else:
            size_bins = self.synthforc_db.sizes

        self.temp_dir_space_manager.create_size_distribution_plot(
            self.get_size_distr_shape(), self.get_size_distr_location(), self.get_size_distr_scale(), size_bins
        )

        if self.temp_dir_space_manager.size_distribution_plot is not None:
            image = Image.open(self.temp_dir_space_manager.size_distribution_plot)
            width, height = image.size
            qimage = ImageQt.ImageQt(image)
            self.size_distr_pixmap.setPixmap(QtGui.QPixmap.fromImage(qimage))
            self.graphics_size_distribution.resetTransform()
            self.graphics_size_distribution.scale(0.2, 0.2)

    def update_aratio_distribution_plot(self):
        if self.db_file is None and self.synthforc_db is None:
            aratio_bins = None
        else:
            aratio_bins = self.synthforc_db.aratios

        self.temp_dir_space_manager.create_aratio_distribution_plot(
            self.get_aratio_distr_shape(), self.get_aratio_distr_location(), self.get_aratio_distr_scale(), aratio_bins
        )

        if self.temp_dir_space_manager.aratio_distribution_plot is not None:
            image = Image.open(self.temp_dir_space_manager.aratio_distribution_plot)
            width, height = image.size
            qimage = ImageQt.ImageQt(image)
            self.aratio_distr_pixmap.setPixmap(QtGui.QPixmap.fromImage(qimage))
            self.graphics_aratio_distribution.resetTransform()
            self.graphics_aratio_distribution.scale(0.2, 0.2)
