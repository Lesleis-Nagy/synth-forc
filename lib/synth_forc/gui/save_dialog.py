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
# File: save_dialog.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import re
import os
import pathlib
import shutil

from synth_forc.qt.save_dialog import Ui_SaveDialog

from PyQt6.QtCore import QRegularExpression

from PyQt6.QtWidgets import QDialog
from PyQt6.QtWidgets import QMessageBox
from PyQt6.QtWidgets import QFileDialog


class SaveDialog(QDialog, Ui_SaveDialog):
    r"""
    Settings dialog object.
    """

    re_int = QRegularExpression(r"[0-9]+")
    re_float = QRegularExpression(r"[-+]?[0-9]*\.?[0-9]+([eE][-+]?[0-9]+)?")

    allowed_file_extensions = ["png", "pdf", "jpg"]

    def __init__(self, settings, temp_dir_space_manager, forc_save_file, forc_loops_save_file,
                 forc_size_distr_save_file, forc_aratio_distr_save_file):
        r"""
        Create a settings dialog window.
        """

        QDialog.__init__(self)
        Ui_SaveDialog.__init__(self)

        self.setupUi(self)

        self.settings = settings
        self.temp_dir_space_manager = temp_dir_space_manager

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

        if forc_save_file is not None:
            self.txt_forc.setText(forc_save_file)

        if forc_loops_save_file is not None:
            self.txt_forc_loops.setText(forc_loops_save_file)

        if forc_size_distr_save_file is not None:
            self.txt_size_distribution.setText(forc_size_distr_save_file)

        if forc_aratio_distr_save_file is not None:
            self.txt_aspect_ratio_distribution.setText(forc_aratio_distr_save_file)

    def btn_exit_action(self):
        self.close()

    def btn_save_action(self):
        response = QMessageBox.question(self, "", "Are you sure you want to continue?",
                                        QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)
        if response == QMessageBox.StandardButton.Yes:
            self._save_forc_file()
            self._save_forc_loops_file()
            self._save_size_distribution_file()
            self._save_aratio_distribution_file()

    def btn_clear_aspect_ratio_distribution_action(self):
        self.txt_aspect_ratio_distribution.setText("")

    def btn_clear_forc_action(self):
        self.txt_forc.setText("")

    def btn_clear_forc_loops_action(self):
        self.txt_forc_loops.setText("")

    def btn_clear_size_distribution_action(self):
        self.txt_size_distribution.setText("")

    def btn_forc_file_dialog_action(self):
        start_dir = str(pathlib.Path.home())
        if self.txt_forc.text() is not None and re.sub(r"\s+", "", self.txt_forc.text(), flags=re.UNICODE) != "":
            start_dir = os.path.dirname(self.txt_forc.text())

        new_file = QFileDialog.getSaveFileName(self, 'Save FORC diagram file', directory=start_dir)
        if new_file[0] and len(new_file[0]) > 0:
            self.txt_forc.setText(new_file[0])
            self._save_forc_file()

    def btn_forc_loops_file_dialog_action(self):
        start_dir = str(pathlib.Path.home())
        if self.txt_forc_loops.text() is not None and re.sub(r"\s+", "", self.txt_forc_loops.text(),
                                                             flags=re.UNICODE) != "":
            start_dir = os.path.dirname(self.txt_forc_loops.text())

        new_file = QFileDialog.getSaveFileName(self, 'Save FORC hysteresis loops file', start_dir)
        if new_file[0] and len(new_file[0]) > 0:
            self.txt_forc_loops.setText(new_file[0])
            self._save_forc_loops_file()

    def btn_size_distribution_file_dialog_action(self):
        start_dir = str(pathlib.Path.home())
        if self.txt_size_distribution.text() is not None and re.sub(r"\s+", "", self.txt_size_distribution.text(),
                                                                    flags=re.UNICODE) != "":
            start_dir = os.path.dirname(self.txt_size_distribution.text())

        new_file = QFileDialog.getSaveFileName(self, 'Save size distribution graph', start_dir)
        if new_file[0] and len(new_file[0]) > 0:
            self.txt_size_distribution.setText(new_file[0])
            self._save_size_distribution_file()

    def btn_aspect_ratio_distribution_file_dialog_action(self):
        start_dir = str(pathlib.Path.home())
        if self.txt_aspect_ratio_distribution.text() is not None and re.sub(r"\s+", "",
                                                                            self.txt_aspect_ratio_distribution.text(),
                                                                            flags=re.UNICODE) != "":
            start_dir = os.path.dirname(self.txt_aspect_ratio_distribution.text())

        new_file = QFileDialog.getSaveFileName(self, 'Save aspect ratio graph', start_dir)
        if new_file[0] and len(new_file[0]) > 0:
            self.txt_aspect_ratio_distribution.setText(new_file[0])
            self._save_aratio_distribution_file()

    def _save_forc_file(self):
        r"""
        Perform a save action by copying the FORC file from the temporary directory to the file of the user's choice.
        """
        extension = os.path.splitext(self.txt_forc.text())
        if len(self.txt_forc.text()) > 0:
            if extension[1] == ".pdf":
                if self.temp_dir_space_manager.forc_plot_pdf:
                    shutil.copyfile(self.temp_dir_space_manager.forc_plot_pdf, self.txt_forc.text())
            elif extension[1] == ".png":
                if self.temp_dir_space_manager.forc_plot_png:
                    shutil.copyfile(self.temp_dir_space_manager.forc_plot_png, self.txt_forc.text())
            elif extension[1] == ".jpg":
                if self.temp_dir_space_manager.forc_plot_jpg:
                    shutil.copyfile(self.temp_dir_space_manager.forc_plot_jpg, self.txt_forc.text())
            else:
                # Since we don't know the extension - default to pdf
                if self.temp_dir_space_manager.forc_plot_pdf:
                    shutil.copyfile(self.temp_dir_space_manager.forc_plot_pdf, self.txt_forc.text())

    def _save_forc_loops_file(self):
        r"""
        Perform a save action by copying the FORC loops file from the temporary directory to the file of the user's
        choice.
        """
        extension = os.path.splitext(self.txt_forc_loops.text())
        if len(self.txt_forc_loops.text()) > 0:
            if extension[1] == ".pdf":
                if self.temp_dir_space_manager.forc_loops_plot_pdf:
                    shutil.copyfile(self.temp_dir_space_manager.forc_loops_plot_pdf, self.txt_forc_loops.text())
            elif extension[1] == ".png":
                if self.temp_dir_space_manager.forc_loops_plot_png:
                    shutil.copyfile(self.temp_dir_space_manager.forc_loops_plot_png, self.txt_forc_loops.text())
            elif extension[1] == ".jpg":
                if self.temp_dir_space_manager.forc_loops_plot_jpg:
                    shutil.copyfile(self.temp_dir_space_manager.forc_loops_plot_jpg, self.txt_forc_loops.text())
            else:
                # Since we don't know the extension - default to pdf
                if self.temp_dir_space_manager.forc_loops_plot_pdf:
                    shutil.copyfile(self.temp_dir_space_manager.forc_loops_plot_pdf, self.txt_forc_loops.text())

    def _save_size_distribution_file(self):
        r"""
        Perform a save action by copying the size distribution plot from the temporary directory to the file of the
        user's choice.
        """
        extension = os.path.splitext(self.txt_size_distribution.text())
        if len(self.txt_size_distribution.text()) > 0:
            if extension[1] == ".pdf":
                if self.temp_dir_space_manager.size_distribution_plot_pdf:
                    shutil.copyfile(self.temp_dir_space_manager.size_distribution_plot_pdf,
                                    self.txt_size_distribution.text())
            elif extension[1] == ".png":
                if self.temp_dir_space_manager.size_distribution_plot_png:
                    shutil.copyfile(self.temp_dir_space_manager.size_distribution_plot_png,
                                    self.txt_size_distribution.text())
            elif extension[1] == ".jpg":
                if self.temp_dir_space_manager.size_distribution_plot_jpg:
                    shutil.copyfile(self.temp_dir_space_manager.size_distribution_plot_jpg,
                                    self.txt_size_distribution.text())
            else:
                # Since we don't know the extension - default to pdf
                if self.temp_dir_space_manager.size_distribution_plot_pdf:
                    shutil.copyfile(self.temp_dir_space_manager.size_distribution_plot_pdf,
                                    self.txt_size_distribution.text())

    def _save_aratio_distribution_file(self):
        r"""
        Perform a save action by copying the aspect ratio distribution plot from the temporary directory to the file of
        the user's choice.
        """
        extension = os.path.splitext(self.txt_aspect_ratio_distribution.text())
        if len(self.txt_aspect_ratio_distribution.text()) > 0:
            if extension[1] == ".pdf":
                if self.temp_dir_space_manager.aratio_distribution_plot_pdf:
                    shutil.copyfile(self.temp_dir_space_manager.aratio_distribution_plot_pdf,
                                    self.txt_aspect_ratio_distribution.text())
            elif extension[1] == ".png":
                if self.temp_dir_space_manager.aratio_distribution_plot_png:
                    shutil.copyfile(self.temp_dir_space_manager.aratio_distribution_plot_png,
                                    self.txt_aspect_ratio_distribution.text())
            elif extension[1] == ".jpg":
                if self.temp_dir_space_manager.aratio_distribution_plot_jpg:
                    shutil.copyfile(self.temp_dir_space_manager.aratio_distribution_plot_jpg,
                                    self.txt_aspect_ratio_distribution.text())
            else:
                # Since we don't know the extension - default to pdf
                if self.temp_dir_space_manager.aratio_distribution_plot_pdf:
                    shutil.copyfile(self.temp_dir_space_manager.aratio_distribution_plot_pdf,
                                    self.txt_aspect_ratio_distribution.text())
