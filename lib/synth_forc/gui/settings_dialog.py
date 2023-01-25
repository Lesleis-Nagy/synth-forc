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
# File: settings_dialog.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

from synth_forc.qt.settings_dialog import Ui_SettingsDialog

from PyQt6.QtGui import QRegularExpressionValidator

from PyQt6.QtCore import QRegularExpression

from PyQt6.QtWidgets import QDialog


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

        # Assign validators for text boxes.
        self.txt_dpi.setValidator(QRegularExpressionValidator(SettingsDialog.re_int))
        self.txt_x_limits_from.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_x_limits_to.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_y_limits_from.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_y_limits_to.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_contour_start.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_contour_end.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))
        self.txt_contour_step.setValidator(QRegularExpressionValidator(SettingsDialog.re_float))

        # Set text box parameters.
        self.txt_dpi.setText(str(settings.dpi))
        self.txt_x_limits_from.setText(str(settings.x_limits_from))
        self.txt_x_limits_to.setText(str(settings.x_limits_to))
        self.txt_y_limits_from.setText(str(settings.y_limits_from))
        self.txt_y_limits_to.setText(str(settings.y_limits_to))
        self.txt_contour_start.setText(str(settings.contour_start))
        self.txt_contour_end.setText(str(settings.contour_end))
        self.txt_contour_step.setText(str(settings.contour_step))

    def btn_exit_action(self):
        r"""
        The exit action, this will exit the settings dialog and do nothing.
        """
        self.close()

    def btn_save_action(self):
        r"""
        The save action will update the settings file with the user's input.
        """
        self.settings.dpi = int(self.txt_dpi.text())
        self.settings.x_limits_from = float(self.txt_x_limits_from.text())
        self.settings.x_limits_to = float(self.txt_x_limits_to.text())
        self.settings.y_limits_from = float(self.txt_y_limits_from.text())
        self.settings.y_limits_to = float(self.txt_y_limits_to.text())
        self.settings.contour_start = float(self.txt_contour_start.text())
        self.settings.contour_end = float(self.txt_contour_end.text())
        self.settings.contour_step = float(self.txt_contour_step.text())

        self.settings.save()

        self.close()
