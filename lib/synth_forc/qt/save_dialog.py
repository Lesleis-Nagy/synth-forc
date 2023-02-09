# Form implementation generated from reading ui file 'gui/save_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SaveDialog(object):
    def setupUi(self, SaveDialog):
        SaveDialog.setObjectName("SaveDialog")
        SaveDialog.resize(773, 332)
        self.gridLayout = QtWidgets.QGridLayout(SaveDialog)
        self.gridLayout.setObjectName("gridLayout")
        self.txt_aspect_ratio_distribution = QtWidgets.QLineEdit(SaveDialog)
        self.txt_aspect_ratio_distribution.setObjectName("txt_aspect_ratio_distribution")
        self.gridLayout.addWidget(self.txt_aspect_ratio_distribution, 4, 1, 1, 1)
        self.lbl_aspect_ratio_distribution = QtWidgets.QLabel(SaveDialog)
        self.lbl_aspect_ratio_distribution.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_aspect_ratio_distribution.setObjectName("lbl_aspect_ratio_distribution")
        self.gridLayout.addWidget(self.lbl_aspect_ratio_distribution, 4, 0, 1, 1)
        self.frm_save_exit = QtWidgets.QFrame(SaveDialog)
        self.frm_save_exit.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frm_save_exit.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frm_save_exit.setObjectName("frm_save_exit")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_save_exit)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(self.frm_save_exit)
        self.btn_save.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_save.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_exit = QtWidgets.QPushButton(self.frm_save_exit)
        self.btn_exit.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_exit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.frm_save_exit, 5, 0, 1, 2)
        self.btn_forc_file_dialog = QtWidgets.QPushButton(SaveDialog)
        self.btn_forc_file_dialog.setObjectName("btn_forc_file_dialog")
        self.gridLayout.addWidget(self.btn_forc_file_dialog, 1, 2, 1, 1)
        self.txt_size_distribution = QtWidgets.QLineEdit(SaveDialog)
        self.txt_size_distribution.setObjectName("txt_size_distribution")
        self.gridLayout.addWidget(self.txt_size_distribution, 3, 1, 1, 1)
        self.txt_forc = QtWidgets.QLineEdit(SaveDialog)
        self.txt_forc.setObjectName("txt_forc")
        self.gridLayout.addWidget(self.txt_forc, 1, 1, 1, 1)
        self.lbl_forc = QtWidgets.QLabel(SaveDialog)
        self.lbl_forc.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_forc.setObjectName("lbl_forc")
        self.gridLayout.addWidget(self.lbl_forc, 1, 0, 1, 1)
        self.lbl_forc_loops = QtWidgets.QLabel(SaveDialog)
        self.lbl_forc_loops.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_forc_loops.setObjectName("lbl_forc_loops")
        self.gridLayout.addWidget(self.lbl_forc_loops, 2, 0, 1, 1)
        self.lbl_size_distribution = QtWidgets.QLabel(SaveDialog)
        self.lbl_size_distribution.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_size_distribution.setObjectName("lbl_size_distribution")
        self.gridLayout.addWidget(self.lbl_size_distribution, 3, 0, 1, 1)
        self.txt_forc_loops = QtWidgets.QLineEdit(SaveDialog)
        self.txt_forc_loops.setObjectName("txt_forc_loops")
        self.gridLayout.addWidget(self.txt_forc_loops, 2, 1, 1, 1)
        self.btn_clear_forc = QtWidgets.QPushButton(SaveDialog)
        self.btn_clear_forc.setObjectName("btn_clear_forc")
        self.gridLayout.addWidget(self.btn_clear_forc, 1, 3, 1, 1)
        self.btn_forc_loops_file_dialog = QtWidgets.QPushButton(SaveDialog)
        self.btn_forc_loops_file_dialog.setObjectName("btn_forc_loops_file_dialog")
        self.gridLayout.addWidget(self.btn_forc_loops_file_dialog, 2, 2, 1, 1)
        self.btn_size_distribution_file_dialog = QtWidgets.QPushButton(SaveDialog)
        self.btn_size_distribution_file_dialog.setObjectName("btn_size_distribution_file_dialog")
        self.gridLayout.addWidget(self.btn_size_distribution_file_dialog, 3, 2, 1, 1)
        self.btn_aspect_ratio_distribution_file_dialog = QtWidgets.QPushButton(SaveDialog)
        self.btn_aspect_ratio_distribution_file_dialog.setObjectName("btn_aspect_ratio_distribution_file_dialog")
        self.gridLayout.addWidget(self.btn_aspect_ratio_distribution_file_dialog, 4, 2, 1, 1)
        self.btn_clear_forc_loops = QtWidgets.QPushButton(SaveDialog)
        self.btn_clear_forc_loops.setObjectName("btn_clear_forc_loops")
        self.gridLayout.addWidget(self.btn_clear_forc_loops, 2, 3, 1, 1)
        self.btn_clear_size_distribution = QtWidgets.QPushButton(SaveDialog)
        self.btn_clear_size_distribution.setObjectName("btn_clear_size_distribution")
        self.gridLayout.addWidget(self.btn_clear_size_distribution, 3, 3, 1, 1)
        self.btn_clear_aspect_ratio_distribution = QtWidgets.QPushButton(SaveDialog)
        self.btn_clear_aspect_ratio_distribution.setObjectName("btn_clear_aspect_ratio_distribution")
        self.gridLayout.addWidget(self.btn_clear_aspect_ratio_distribution, 4, 3, 1, 1)
        self.lbl_message = QtWidgets.QLabel(SaveDialog)
        self.lbl_message.setWordWrap(True)
        self.lbl_message.setObjectName("lbl_message")
        self.gridLayout.addWidget(self.lbl_message, 0, 0, 1, 4)

        self.retranslateUi(SaveDialog)
        QtCore.QMetaObject.connectSlotsByName(SaveDialog)
        SaveDialog.setTabOrder(self.txt_forc, self.txt_forc_loops)
        SaveDialog.setTabOrder(self.txt_forc_loops, self.txt_size_distribution)
        SaveDialog.setTabOrder(self.txt_size_distribution, self.txt_aspect_ratio_distribution)
        SaveDialog.setTabOrder(self.txt_aspect_ratio_distribution, self.btn_save)
        SaveDialog.setTabOrder(self.btn_save, self.btn_exit)
        SaveDialog.setTabOrder(self.btn_exit, self.btn_forc_file_dialog)
        SaveDialog.setTabOrder(self.btn_forc_file_dialog, self.btn_clear_forc)
        SaveDialog.setTabOrder(self.btn_clear_forc, self.btn_forc_loops_file_dialog)
        SaveDialog.setTabOrder(self.btn_forc_loops_file_dialog, self.btn_clear_forc_loops)
        SaveDialog.setTabOrder(self.btn_clear_forc_loops, self.btn_size_distribution_file_dialog)
        SaveDialog.setTabOrder(self.btn_size_distribution_file_dialog, self.btn_clear_size_distribution)
        SaveDialog.setTabOrder(self.btn_clear_size_distribution, self.btn_aspect_ratio_distribution_file_dialog)
        SaveDialog.setTabOrder(self.btn_aspect_ratio_distribution_file_dialog, self.btn_clear_aspect_ratio_distribution)

    def retranslateUi(self, SaveDialog):
        _translate = QtCore.QCoreApplication.translate
        SaveDialog.setWindowTitle(_translate("SaveDialog", "Save"))
        self.txt_aspect_ratio_distribution.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Aspect ratio graph output file name.</p></body></html>"))
        self.lbl_aspect_ratio_distribution.setText(_translate("SaveDialog", "Aspect ratio distribution:"))
        self.btn_save.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Save files.</p></body></html>"))
        self.btn_save.setText(_translate("SaveDialog", "save"))
        self.btn_exit.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Exit without saving.</p></body></html>"))
        self.btn_exit.setText(_translate("SaveDialog", "exit"))
        self.btn_forc_file_dialog.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Open FORC diagram file output dialog.</p></body></html>"))
        self.btn_forc_file_dialog.setText(_translate("SaveDialog", "..."))
        self.txt_size_distribution.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Size distribution graph output file name.</p></body></html>"))
        self.txt_forc.setToolTip(_translate("SaveDialog", "<html><head/><body><p>FORC diagram figure output file name.</p></body></html>"))
        self.lbl_forc.setText(_translate("SaveDialog", "FORC:"))
        self.lbl_forc_loops.setText(_translate("SaveDialog", "FORC loops:"))
        self.lbl_size_distribution.setText(_translate("SaveDialog", "Size distribution:"))
        self.txt_forc_loops.setToolTip(_translate("SaveDialog", "<html><head/><body><p>FORC loops figure output file name.</p></body></html>"))
        self.btn_clear_forc.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Clear FORC diagram file output.</p></body></html>"))
        self.btn_clear_forc.setText(_translate("SaveDialog", "clear"))
        self.btn_forc_loops_file_dialog.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Open FORC loops diagram file output dialog.</p></body></html>"))
        self.btn_forc_loops_file_dialog.setText(_translate("SaveDialog", "..."))
        self.btn_size_distribution_file_dialog.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Open size distribution graph file output dialog.</p></body></html>"))
        self.btn_size_distribution_file_dialog.setText(_translate("SaveDialog", "..."))
        self.btn_aspect_ratio_distribution_file_dialog.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Open aspect ratio distribution graph file output dialog.</p></body></html>"))
        self.btn_aspect_ratio_distribution_file_dialog.setText(_translate("SaveDialog", "..."))
        self.btn_clear_forc_loops.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Clear FORC loops diagram file output.</p></body></html>"))
        self.btn_clear_forc_loops.setText(_translate("SaveDialog", "clear"))
        self.btn_clear_size_distribution.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Clear size distribution graph file output.</p></body></html>"))
        self.btn_clear_size_distribution.setText(_translate("SaveDialog", "clear"))
        self.btn_clear_aspect_ratio_distribution.setToolTip(_translate("SaveDialog", "<html><head/><body><p>Clear aspect ratio distribution graph file output.</p></body></html>"))
        self.btn_clear_aspect_ratio_distribution.setText(_translate("SaveDialog", "clear"))
        self.lbl_message.setText(_translate("SaveDialog", "Input file names for the images you\'d like to save. Please note that any existing file names will be overwritten."))