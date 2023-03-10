# Form implementation generated from reading ui file 'gui/main_window.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.lbl_forc_diagram_loops = QtWidgets.QLabel(self.centralwidget)
        self.lbl_forc_diagram_loops.setObjectName("lbl_forc_diagram_loops")
        self.gridLayout.addWidget(self.lbl_forc_diagram_loops, 0, 1, 1, 1)
        self.graphics_size_distribution = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphics_size_distribution.sizePolicy().hasHeightForWidth())
        self.graphics_size_distribution.setSizePolicy(sizePolicy)
        self.graphics_size_distribution.setMinimumSize(QtCore.QSize(320, 240))
        self.graphics_size_distribution.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphics_size_distribution.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphics_size_distribution.setSceneRect(QtCore.QRectF(0.0, 0.0, 220.0, 220.0))
        self.graphics_size_distribution.setRenderHints(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        self.graphics_size_distribution.setObjectName("graphics_size_distribution")
        self.gridLayout.addWidget(self.graphics_size_distribution, 4, 0, 1, 1)
        self.lbl_aratio_distribution = QtWidgets.QLabel(self.centralwidget)
        self.lbl_aratio_distribution.setObjectName("lbl_aratio_distribution")
        self.gridLayout.addWidget(self.lbl_aratio_distribution, 3, 1, 1, 1)
        self.frm_input = QtWidgets.QFrame(self.centralwidget)
        self.frm_input.setMaximumSize(QtCore.QSize(250, 16777215))
        self.frm_input.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frm_input.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frm_input.setObjectName("frm_input")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frm_input)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grp_size_distribution_parameters = QtWidgets.QGroupBox(self.frm_input)
        self.grp_size_distribution_parameters.setObjectName("grp_size_distribution_parameters")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.grp_size_distribution_parameters)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.txt_size_distr_shape = QtWidgets.QLineEdit(self.grp_size_distribution_parameters)
        self.txt_size_distr_shape.setObjectName("txt_size_distr_shape")
        self.gridLayout_3.addWidget(self.txt_size_distr_shape, 0, 1, 1, 1)
        self.lbl_size_distr_location = QtWidgets.QLabel(self.grp_size_distribution_parameters)
        self.lbl_size_distr_location.setObjectName("lbl_size_distr_location")
        self.gridLayout_3.addWidget(self.lbl_size_distr_location, 1, 0, 1, 1)
        self.lbl_size_distr_shape = QtWidgets.QLabel(self.grp_size_distribution_parameters)
        self.lbl_size_distr_shape.setObjectName("lbl_size_distr_shape")
        self.gridLayout_3.addWidget(self.lbl_size_distr_shape, 0, 0, 1, 1)
        self.lbl_size_distr_scale = QtWidgets.QLabel(self.grp_size_distribution_parameters)
        self.lbl_size_distr_scale.setObjectName("lbl_size_distr_scale")
        self.gridLayout_3.addWidget(self.lbl_size_distr_scale, 2, 0, 1, 1)
        self.txt_size_distr_location = QtWidgets.QLineEdit(self.grp_size_distribution_parameters)
        self.txt_size_distr_location.setObjectName("txt_size_distr_location")
        self.gridLayout_3.addWidget(self.txt_size_distr_location, 1, 1, 1, 1)
        self.txt_size_distr_scale = QtWidgets.QLineEdit(self.grp_size_distribution_parameters)
        self.txt_size_distr_scale.setObjectName("txt_size_distr_scale")
        self.gridLayout_3.addWidget(self.txt_size_distr_scale, 2, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.grp_size_distribution_parameters)
        self.grp_aratio_distribution_parameters = QtWidgets.QGroupBox(self.frm_input)
        self.grp_aratio_distribution_parameters.setObjectName("grp_aratio_distribution_parameters")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.grp_aratio_distribution_parameters)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.txt_aratio_distr_scale = QtWidgets.QLineEdit(self.grp_aratio_distribution_parameters)
        self.txt_aratio_distr_scale.setObjectName("txt_aratio_distr_scale")
        self.gridLayout_4.addWidget(self.txt_aratio_distr_scale, 2, 1, 1, 1)
        self.lbl_aratio_distr_scale = QtWidgets.QLabel(self.grp_aratio_distribution_parameters)
        self.lbl_aratio_distr_scale.setObjectName("lbl_aratio_distr_scale")
        self.gridLayout_4.addWidget(self.lbl_aratio_distr_scale, 2, 0, 1, 1)
        self.txt_aratio_distr_location = QtWidgets.QLineEdit(self.grp_aratio_distribution_parameters)
        self.txt_aratio_distr_location.setObjectName("txt_aratio_distr_location")
        self.gridLayout_4.addWidget(self.txt_aratio_distr_location, 1, 1, 1, 1)
        self.txt_aratio_distr_shape = QtWidgets.QLineEdit(self.grp_aratio_distribution_parameters)
        self.txt_aratio_distr_shape.setObjectName("txt_aratio_distr_shape")
        self.gridLayout_4.addWidget(self.txt_aratio_distr_shape, 0, 1, 1, 1)
        self.lbl_aratio_distr_location = QtWidgets.QLabel(self.grp_aratio_distribution_parameters)
        self.lbl_aratio_distr_location.setObjectName("lbl_aratio_distr_location")
        self.gridLayout_4.addWidget(self.lbl_aratio_distr_location, 1, 0, 1, 1)
        self.lbl_aratio_distr_shape = QtWidgets.QLabel(self.grp_aratio_distribution_parameters)
        self.lbl_aratio_distr_shape.setObjectName("lbl_aratio_distr_shape")
        self.gridLayout_4.addWidget(self.lbl_aratio_distr_shape, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.grp_aratio_distribution_parameters)
        self.grp_parameters = QtWidgets.QGroupBox(self.frm_input)
        self.grp_parameters.setObjectName("grp_parameters")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.grp_parameters)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frm_parameters = QtWidgets.QFrame(self.grp_parameters)
        self.frm_parameters.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.frm_parameters.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frm_parameters.setObjectName("frm_parameters")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frm_parameters)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_smoothing_factor = QtWidgets.QLabel(self.frm_parameters)
        self.lbl_smoothing_factor.setObjectName("lbl_smoothing_factor")
        self.horizontalLayout.addWidget(self.lbl_smoothing_factor)
        self.txt_smoothing_factor = QtWidgets.QLineEdit(self.frm_parameters)
        self.txt_smoothing_factor.setObjectName("txt_smoothing_factor")
        self.horizontalLayout.addWidget(self.txt_smoothing_factor)
        self.verticalLayout.addWidget(self.frm_parameters)
        self.verticalLayout_2.addWidget(self.grp_parameters)
        self.grp_commands = QtWidgets.QGroupBox(self.frm_input)
        self.grp_commands.setMinimumSize(QtCore.QSize(0, 70))
        self.grp_commands.setObjectName("grp_commands")
        self.btn_generate = QtWidgets.QPushButton(self.grp_commands)
        self.btn_generate.setGeometry(QtCore.QRect(20, 30, 100, 32))
        self.btn_generate.setObjectName("btn_generate")
        self.verticalLayout_2.addWidget(self.grp_commands)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout.addWidget(self.frm_input, 2, 2, 3, 1)
        self.lbl_forc_diagram = QtWidgets.QLabel(self.centralwidget)
        self.lbl_forc_diagram.setObjectName("lbl_forc_diagram")
        self.gridLayout.addWidget(self.lbl_forc_diagram, 0, 0, 1, 1)
        self.graphics_loops = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphics_loops.sizePolicy().hasHeightForWidth())
        self.graphics_loops.setSizePolicy(sizePolicy)
        self.graphics_loops.setMinimumSize(QtCore.QSize(320, 240))
        self.graphics_loops.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphics_loops.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphics_loops.setSceneRect(QtCore.QRectF(0.0, 0.0, 220.0, 220.0))
        self.graphics_loops.setRenderHints(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        self.graphics_loops.setObjectName("graphics_loops")
        self.gridLayout.addWidget(self.graphics_loops, 2, 1, 1, 1)
        self.lbl_size_distribution = QtWidgets.QLabel(self.centralwidget)
        self.lbl_size_distribution.setObjectName("lbl_size_distribution")
        self.gridLayout.addWidget(self.lbl_size_distribution, 3, 0, 1, 1)
        self.graphics_forcs = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphics_forcs.sizePolicy().hasHeightForWidth())
        self.graphics_forcs.setSizePolicy(sizePolicy)
        self.graphics_forcs.setMinimumSize(QtCore.QSize(320, 240))
        self.graphics_forcs.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.graphics_forcs.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphics_forcs.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphics_forcs.setSceneRect(QtCore.QRectF(0.0, 0.0, 220.0, 220.0))
        self.graphics_forcs.setRenderHints(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        self.graphics_forcs.setObjectName("graphics_forcs")
        self.gridLayout.addWidget(self.graphics_forcs, 2, 0, 1, 1)
        self.graphics_aratio_distribution = QtWidgets.QGraphicsView(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.graphics_aratio_distribution.sizePolicy().hasHeightForWidth())
        self.graphics_aratio_distribution.setSizePolicy(sizePolicy)
        self.graphics_aratio_distribution.setMinimumSize(QtCore.QSize(320, 240))
        self.graphics_aratio_distribution.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphics_aratio_distribution.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.graphics_aratio_distribution.setSceneRect(QtCore.QRectF(0.0, 0.0, 220.0, 220.0))
        self.graphics_aratio_distribution.setRenderHints(QtGui.QPainter.RenderHint.SmoothPixmapTransform)
        self.graphics_aratio_distribution.setObjectName("graphics_aratio_distribution")
        self.gridLayout.addWidget(self.graphics_aratio_distribution, 4, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 24))
        self.menubar.setObjectName("menubar")
        self.menu_file = QtWidgets.QMenu(self.menubar)
        self.menu_file.setObjectName("menu_file")
        self.menu_settings = QtWidgets.QMenu(self.menubar)
        self.menu_settings.setObjectName("menu_settings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menu_save = QtGui.QAction(MainWindow)
        self.menu_save.setObjectName("menu_save")
        self.actionsave_loops_diagram = QtGui.QAction(MainWindow)
        self.actionsave_loops_diagram.setObjectName("actionsave_loops_diagram")
        self.menu_close = QtGui.QAction(MainWindow)
        self.menu_close.setObjectName("menu_close")
        self.menu_configure = QtGui.QAction(MainWindow)
        self.menu_configure.setObjectName("menu_configure")
        self.menu_load = QtGui.QAction(MainWindow)
        self.menu_load.setObjectName("menu_load")
        self.menu_file.addAction(self.menu_save)
        self.menu_file.addAction(self.menu_load)
        self.menu_file.addSeparator()
        self.menu_file.addAction(self.menu_close)
        self.menu_settings.addAction(self.menu_configure)
        self.menubar.addAction(self.menu_file.menuAction())
        self.menubar.addAction(self.menu_settings.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.graphics_size_distribution, self.graphics_aratio_distribution)
        MainWindow.setTabOrder(self.graphics_aratio_distribution, self.txt_size_distr_shape)
        MainWindow.setTabOrder(self.txt_size_distr_shape, self.txt_size_distr_location)
        MainWindow.setTabOrder(self.txt_size_distr_location, self.txt_size_distr_scale)
        MainWindow.setTabOrder(self.txt_size_distr_scale, self.txt_aratio_distr_shape)
        MainWindow.setTabOrder(self.txt_aratio_distr_shape, self.txt_aratio_distr_location)
        MainWindow.setTabOrder(self.txt_aratio_distr_location, self.txt_aratio_distr_scale)
        MainWindow.setTabOrder(self.txt_aratio_distr_scale, self.btn_generate)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "synth-FORC"))
        self.lbl_forc_diagram_loops.setText(_translate("MainWindow", "FORC diagram loops"))
        self.lbl_aratio_distribution.setText(_translate("MainWindow", "aspect ratio distribution"))
        self.grp_size_distribution_parameters.setTitle(_translate("MainWindow", "size distribution parameters"))
        self.txt_size_distr_shape.setToolTip(_translate("MainWindow", "<html><head/><body><p>The shape parameter of the size distribution.</p></body></html>"))
        self.txt_size_distr_shape.setText(_translate("MainWindow", "0.3"))
        self.lbl_size_distr_location.setText(_translate("MainWindow", "location:"))
        self.lbl_size_distr_shape.setText(_translate("MainWindow", "shape:"))
        self.lbl_size_distr_scale.setText(_translate("MainWindow", "scale:"))
        self.txt_size_distr_location.setToolTip(_translate("MainWindow", "<html><head/><body><p>The location parameter of the size distribution.</p></body></html>"))
        self.txt_size_distr_location.setText(_translate("MainWindow", "1.0"))
        self.txt_size_distr_scale.setToolTip(_translate("MainWindow", "<html><head/><body><p>The scale parameter of the size distribution.</p></body></html>"))
        self.txt_size_distr_scale.setText(_translate("MainWindow", "90.0"))
        self.grp_aratio_distribution_parameters.setTitle(_translate("MainWindow", "aspect ratio distribution parameters"))
        self.txt_aratio_distr_scale.setToolTip(_translate("MainWindow", "<html><head/><body><p>The scale parameter of the aspect ratio distribution.</p></body></html>"))
        self.txt_aratio_distr_scale.setText(_translate("MainWindow", "0.8"))
        self.lbl_aratio_distr_scale.setText(_translate("MainWindow", "scale:"))
        self.txt_aratio_distr_location.setToolTip(_translate("MainWindow", "<html><head/><body><p>The location parameter of the aspect ratio distribution.</p></body></html>"))
        self.txt_aratio_distr_location.setText(_translate("MainWindow", "1.0"))
        self.txt_aratio_distr_shape.setToolTip(_translate("MainWindow", "<html><head/><body><p>The shape parameter of the aspect ratio distribution.</p></body></html>"))
        self.txt_aratio_distr_shape.setText(_translate("MainWindow", "0.9"))
        self.lbl_aratio_distr_location.setText(_translate("MainWindow", "location:"))
        self.lbl_aratio_distr_shape.setText(_translate("MainWindow", "shape:"))
        self.grp_parameters.setTitle(_translate("MainWindow", "parameters"))
        self.lbl_smoothing_factor.setText(_translate("MainWindow", "smoothing factor:"))
        self.txt_smoothing_factor.setText(_translate("MainWindow", "3"))
        self.grp_commands.setTitle(_translate("MainWindow", "commands"))
        self.btn_generate.setToolTip(_translate("MainWindow", "<html><head/><body><p>Generate FORC diagram and FORC diagram loops based on size and aspect ratio distribution.</p></body></html>"))
        self.btn_generate.setText(_translate("MainWindow", "generate"))
        self.lbl_forc_diagram.setText(_translate("MainWindow", "FORC diagram"))
        self.lbl_size_distribution.setText(_translate("MainWindow", "size distribution"))
        self.menu_file.setTitle(_translate("MainWindow", "File"))
        self.menu_settings.setTitle(_translate("MainWindow", "Settings"))
        self.menu_save.setText(_translate("MainWindow", "save"))
        self.actionsave_loops_diagram.setText(_translate("MainWindow", "save loops diagram"))
        self.menu_close.setText(_translate("MainWindow", "Close"))
        self.menu_configure.setText(_translate("MainWindow", "Configure"))
        self.menu_load.setText(_translate("MainWindow", "load"))
