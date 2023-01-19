import tempfile

import typer

from importlib import resources

from synth_forc.qt.main_window import Ui_MainWindow

from PyQt6 import QtCore

from PyQt6 import QtGui

from PyQt6.QtGui import QPixmap

from PyQt6.QtCore import QUrl, QCoreApplication

from PyQt6.QtWidgets import QApplication
from PyQt6.QtWidgets import QMainWindow
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

from synth_forc.gui.main_window import MainWindow

app = typer.Typer()

@app.command()
def begin():
    import sys

    with tempfile.TemporaryDirectory() as temp_dir:
        app = QApplication(sys.argv)
        win = MainWindow(temp_dir)
        win.show()
        sys.exit(app.exec())


def main():
    app()


if __name__ == "__main__":
    app()
