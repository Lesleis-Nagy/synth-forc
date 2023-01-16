# Form implementation generated from reading ui file 'gui/settings_dialog.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_SettingsDialog(object):
    def setupUi(self, SettingsDialog):
        SettingsDialog.setObjectName("SettingsDialog")
        SettingsDialog.setWindowModality(QtCore.Qt.WindowModality.ApplicationModal)
        SettingsDialog.resize(470, 387)
        self.verticalLayout = QtWidgets.QVBoxLayout(SettingsDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_2.setObjectName("groupBox_2")
        self.txt_smoothing_factor = QtWidgets.QLineEdit(self.groupBox_2)
        self.txt_smoothing_factor.setGeometry(QtCore.QRect(20, 30, 121, 21))
        self.txt_smoothing_factor.setObjectName("txt_smoothing_factor")
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_3.setObjectName("groupBox_3")
        self.txt_dpi = QtWidgets.QLineEdit(self.groupBox_3)
        self.txt_dpi.setGeometry(QtCore.QRect(20, 30, 121, 21))
        self.txt_dpi.setObjectName("txt_dpi")
        self.verticalLayout.addWidget(self.groupBox_3)
        self.groupBox = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox.setObjectName("groupBox")
        self.txt_x_limits_to = QtWidgets.QLineEdit(self.groupBox)
        self.txt_x_limits_to.setGeometry(QtCore.QRect(200, 30, 90, 21))
        self.txt_x_limits_to.setObjectName("txt_x_limits_to")
        self.txt_x_limits_from = QtWidgets.QLineEdit(self.groupBox)
        self.txt_x_limits_from.setGeometry(QtCore.QRect(60, 30, 90, 21))
        self.txt_x_limits_from.setObjectName("txt_x_limits_from")
        self.lbl_x_limits_to = QtWidgets.QLabel(self.groupBox)
        self.lbl_x_limits_to.setGeometry(QtCore.QRect(160, 30, 16, 21))
        self.lbl_x_limits_to.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_x_limits_to.setObjectName("lbl_x_limits_to")
        self.lbl_x_limits_from = QtWidgets.QLabel(self.groupBox)
        self.lbl_x_limits_from.setGeometry(QtCore.QRect(20, 30, 41, 21))
        self.lbl_x_limits_from.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_x_limits_from.setObjectName("lbl_x_limits_from")
        self.verticalLayout.addWidget(self.groupBox)
        self.grp_parameters = QtWidgets.QGroupBox(SettingsDialog)
        self.grp_parameters.setMinimumSize(QtCore.QSize(0, 0))
        self.grp_parameters.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.grp_parameters.setObjectName("grp_parameters")
        self.lbl_y_limits_from = QtWidgets.QLabel(self.grp_parameters)
        self.lbl_y_limits_from.setGeometry(QtCore.QRect(20, 30, 41, 21))
        self.lbl_y_limits_from.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_y_limits_from.setObjectName("lbl_y_limits_from")
        self.txt_y_limits_from = QtWidgets.QLineEdit(self.grp_parameters)
        self.txt_y_limits_from.setGeometry(QtCore.QRect(60, 30, 90, 21))
        self.txt_y_limits_from.setObjectName("txt_y_limits_from")
        self.lbl_y_limits_to = QtWidgets.QLabel(self.grp_parameters)
        self.lbl_y_limits_to.setGeometry(QtCore.QRect(160, 30, 16, 21))
        self.lbl_y_limits_to.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_y_limits_to.setObjectName("lbl_y_limits_to")
        self.txt_y_limits_to = QtWidgets.QLineEdit(self.grp_parameters)
        self.txt_y_limits_to.setGeometry(QtCore.QRect(200, 30, 90, 21))
        self.txt_y_limits_to.setObjectName("txt_y_limits_to")
        self.verticalLayout.addWidget(self.grp_parameters)
        self.groupBox_4 = QtWidgets.QGroupBox(SettingsDialog)
        self.groupBox_4.setObjectName("groupBox_4")
        self.txt_contour_end = QtWidgets.QLineEdit(self.groupBox_4)
        self.txt_contour_end.setGeometry(QtCore.QRect(330, 30, 90, 21))
        self.txt_contour_end.setObjectName("txt_contour_end")
        self.lbl_contour_start = QtWidgets.QLabel(self.groupBox_4)
        self.lbl_contour_start.setGeometry(QtCore.QRect(20, 30, 32, 21))
        self.lbl_contour_start.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_contour_start.setObjectName("lbl_contour_start")
        self.txt_contour_step = QtWidgets.QLineEdit(self.groupBox_4)
        self.txt_contour_step.setGeometry(QtCore.QRect(200, 30, 90, 21))
        self.txt_contour_step.setObjectName("txt_contour_step")
        self.lbl_contour_step = QtWidgets.QLabel(self.groupBox_4)
        self.lbl_contour_step.setGeometry(QtCore.QRect(160, 30, 30, 21))
        self.lbl_contour_step.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_contour_step.setObjectName("lbl_contour_step")
        self.txt_contour_start = QtWidgets.QLineEdit(self.groupBox_4)
        self.txt_contour_start.setGeometry(QtCore.QRect(60, 30, 90, 21))
        self.txt_contour_start.setObjectName("txt_contour_start")
        self.lbl_contour_end = QtWidgets.QLabel(self.groupBox_4)
        self.lbl_contour_end.setGeometry(QtCore.QRect(300, 30, 27, 21))
        self.lbl_contour_end.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTrailing|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.lbl_contour_end.setObjectName("lbl_contour_end")
        self.verticalLayout.addWidget(self.groupBox_4)
        self.frame = QtWidgets.QFrame(SettingsDialog)
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Plain)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btn_save = QtWidgets.QPushButton(self.frame)
        self.btn_save.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_save.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout.addWidget(self.btn_save)
        self.btn_exit = QtWidgets.QPushButton(self.frame)
        self.btn_exit.setMinimumSize(QtCore.QSize(60, 0))
        self.btn_exit.setMaximumSize(QtCore.QSize(60, 16777215))
        self.btn_exit.setObjectName("btn_exit")
        self.horizontalLayout.addWidget(self.btn_exit)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(SettingsDialog)
        QtCore.QMetaObject.connectSlotsByName(SettingsDialog)

    def retranslateUi(self, SettingsDialog):
        _translate = QtCore.QCoreApplication.translate
        SettingsDialog.setWindowTitle(_translate("SettingsDialog", "Settings"))
        self.groupBox_2.setTitle(_translate("SettingsDialog", "smoothing factor"))
        self.txt_smoothing_factor.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>The smoothing factor used for FORC diagram generation.</p></body></html>"))
        self.txt_smoothing_factor.setText(_translate("SettingsDialog", "3"))
        self.groupBox_3.setTitle(_translate("SettingsDialog", "dpi"))
        self.txt_dpi.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>The dots per inch (DPI) used when saving FORC and FORC curve bitmap images.</p></body></html>"))
        self.txt_dpi.setText(_translate("SettingsDialog", "600"))
        self.groupBox.setTitle(_translate("SettingsDialog", "x limits"))
        self.txt_x_limits_to.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>The maximum value used for the FORC diagram x-axis.</p></body></html>"))
        self.txt_x_limits_to.setText(_translate("SettingsDialog", "200.0"))
        self.txt_x_limits_from.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>The minimum value used for the FORC diagram x-axis.</p></body></html>"))
        self.txt_x_limits_from.setText(_translate("SettingsDialog", "0"))
        self.lbl_x_limits_to.setText(_translate("SettingsDialog", "to:"))
        self.lbl_x_limits_from.setText(_translate("SettingsDialog", "from:"))
        self.grp_parameters.setTitle(_translate("SettingsDialog", "y limits"))
        self.lbl_y_limits_from.setText(_translate("SettingsDialog", "from:"))
        self.txt_y_limits_from.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>The minimum value used for the FORC diagram y-axis.</p></body></html>"))
        self.txt_y_limits_from.setText(_translate("SettingsDialog", "-200.0"))
        self.lbl_y_limits_to.setText(_translate("SettingsDialog", "to:"))
        self.txt_y_limits_to.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>The maximum value used for the FORC diagram y-axis.</p></body></html>"))
        self.txt_y_limits_to.setText(_translate("SettingsDialog", "200.0"))
        self.groupBox_4.setTitle(_translate("SettingsDialog", "contour"))
        self.txt_contour_end.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>FORC diagram contour end value.</p></body></html>"))
        self.txt_contour_end.setText(_translate("SettingsDialog", "0.1"))
        self.lbl_contour_start.setText(_translate("SettingsDialog", "start:"))
        self.txt_contour_step.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>FORC diagram countour steps.</p></body></html>"))
        self.txt_contour_step.setText(_translate("SettingsDialog", "0.3"))
        self.lbl_contour_step.setText(_translate("SettingsDialog", "step:"))
        self.txt_contour_start.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>FORC diagram contour start value.</p></body></html>"))
        self.txt_contour_start.setText(_translate("SettingsDialog", "0.1"))
        self.lbl_contour_end.setText(_translate("SettingsDialog", "end:"))
        self.btn_save.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>Save settings and exit.</p></body></html>"))
        self.btn_save.setText(_translate("SettingsDialog", "save"))
        self.btn_exit.setToolTip(_translate("SettingsDialog", "<html><head/><body><p>Exit without saving settings.</p></body></html>"))
        self.btn_exit.setText(_translate("SettingsDialog", "exit"))
