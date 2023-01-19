import tempfile

import typer

from importlib import resources

from synth_forc.qt.settings_dialog import Ui_SettingsDialog

from PyQt6 import QtCore

from PyQt6 import QtGui

from PyQt6.QtGui import QPixmap
from PyQt6.QtGui import QRegularExpressionValidator

from PyQt6.QtCore import QUrl
from PyQt6.QtCore import QCoreApplication
from PyQt6.QtCore import QRegularExpression

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

class SettingsDialog(QDialog, Ui_SettingsDialog):
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
        Ui_SettingsDialog.__init__(self)

        self.setupUi(self)

        self.settings = settings

        self.btn_exit.clicked.connect(self.btn_exit_action)
        self.btn_save.clicked.connect(self.btn_save_action)

        self.txt_smoothing_factor.setValidator(QRegularExpressionValidator(SettingsDialog.re_int))
        self.txt_dpi.setValidator(QRegularExpressionValidator(SettingsDialog.re_int))
        self.txt_x_limits_from.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_x_limits_to.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_y_limits_from.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_y_limits_to.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_contour_start.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_contour_end.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_contour_step.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))

    def btn_exit_action(self):
        self.close()

    def btn_save_action(self):
        print("btn_save_action() stub")
