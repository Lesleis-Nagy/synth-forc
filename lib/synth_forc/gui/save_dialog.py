import tempfile

import typer

from importlib import resources

from synth_forc.qt.save_dialog import Ui_SaveDialog

from PyQt6 import QtCore

from PyQt6 import QtGui

from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QRegularExpressionValidator

from PyQt6.QtCore import QUrl, QCoreApplication, QRegularExpression

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import QGraphicsScene
from PyQt6.QtWidgets import QGraphicsView
from PyQt6.QtWidgets import QGraphicsPixmapItem
from PyQt6.QtWidgets import QFrame
from PyQt6.QtWidgets import QLabel

from PyQt6 import uic

#from PyQt6.QtCharts import QChart, QChartView, QLineSeries, QDateTimeAxis, QValueAxis

from PIL import Image, ImageQt, ImageEnhance

from synth_forc.settings import Settings

class SaveDialog(QDialog, Ui_SaveDialog):
    r"""
    Settings dialog object.
    """

    re_int = QRegularExpression(r"[0-9]+")
    re_float = QRegularExpression(r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")

    def __init__(self, settings):
        r"""
        Create a settings dialog window.
        """

        QDialog.__init__(self)
        Ui_SaveDialog.__init__(self)

        self.setupUi(self)

        self.settings = settings

        self.btn_exit.clicked.connect(self.btn_exit_action)
        self.btn_save.clicked.connect(self.btn_save_action)
        self.btn_aspect_ratio_distribution_file_dialog.clicked.connect(self.btn_aspect_ratio_distribution_file_dialog_action)
        self.btn_clear_aspect_ratio_distribution.clicked.connect(self.btn_clear_aspect_ratio_distribution_action)
        self.btn_clear_forc.clicked.connect(self.btn_clear_forc_action)
        self.btn_clear_forc_loops.clicked.connect(self.btn_clear_forc_loops_action)
        self.btn_clear_size_distribution.clicked.connect(self.btn_clear_size_distribution_action)
        self.btn_forc_file_dialog.clicked.connect(self.btn_forc_file_dialog_action)
        self.btn_forc_loops_file_dialog.clicked.connect(self.btn_forc_loops_file_dialog_action)
        self.btn_size_distribution_file_dialog.clicked.connect(self.btn_size_distribution_file_dialog_action)

    def btn_exit_action(self):
        self.close()

    def btn_save_action(self):
        print("btn_save_action() stub")

    def btn_aspect_ratio_distribution_file_dialog_action(self):
        print("btn_aspect_ratio_distribution_file_dialog_action() stub")

    def btn_clear_aspect_ratio_distribution_action(self):
        print("btn_clear_aspect_ratio_distribution_action() stub")

    def btn_clear_forc_action(self):
        print("btn_clear_forc_action() stub")

    def btn_clear_forc_loops_action(self):
        print("btn_clear_forc_loops_action() stub")

    def btn_clear_size_distribution_action(self):
        print("btn_clear_size_distribution_action() stub")

    def btn_forc_file_dialog_action(self):
        print("btn_forc_file_dialog_action() stub")

    def btn_forc_loops_file_dialog_action(self):
        print("btn_forc_loops_file_dialog_action() stub")

    def btn_size_distribution_file_dialog_action(self):
        print("btn_size_distribution_file_dialog_action() stub")


