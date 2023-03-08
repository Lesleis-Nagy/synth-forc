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
# File: main.py
# Authors: L. Nagy, Miguel A. Valdez-Grijalva, W. Williams, A. Muxworthy,  G. Paterson and L. Tauxe
# Date: Jan 25 2023
#

import sys
import tempfile

import typer
from typer import Option

from PyQt6.QtWidgets import QApplication

from synth_forc.gui.main_window import MainWindow

from synth_forc.logger import setup_logger

app = typer.Typer()

@app.command()
def begin(log_file: str = Option(None, help="if supplied, logging data is saved to this file."),
          log_level: str = Option(None, help="if supplied, the level at which logging data is produced."),
          log_to_stdout: bool = Option(False, help="if set, write logging data to standard output.")):

    setup_logger(log_file, log_level, log_to_stdout)

    with tempfile.TemporaryDirectory() as temp_dir:
        app = QApplication(sys.argv)
        win = MainWindow(temp_dir)
        win.show()
        sys.exit(app.exec())


def main():
    app()


if __name__ == "__main__":
    app()
