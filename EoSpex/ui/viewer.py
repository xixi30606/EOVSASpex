# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'viewer.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1058, 757)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setAcceptDrops(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(600, 200))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.controlWidget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.controlWidget.sizePolicy().hasHeightForWidth())
        self.controlWidget.setSizePolicy(sizePolicy)
        self.controlWidget.setMinimumSize(QtCore.QSize(280, 0))
        self.controlWidget.setMaximumSize(QtCore.QSize(350, 16777215))
        self.controlWidget.setObjectName("controlWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.controlWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.Control_tab = QtWidgets.QTabWidget(self.controlWidget)
        self.Control_tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.Control_tab.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.Control_tab.setObjectName("Control_tab")
        self.layer = QtWidgets.QWidget()
        self.layer.setObjectName("layer")
        self.scrollArea_2 = QtWidgets.QScrollArea(self.layer)
        self.scrollArea_2.setGeometry(QtCore.QRect(-10, 0, 341, 684))
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollArea_2.setObjectName("scrollArea_2")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 339, 682))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.groupBox_image_control = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_image_control.setObjectName("groupBox_image_control")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_image_control)
        self.verticalLayout.setObjectName("verticalLayout")
        self.control_image_type_2 = QtWidgets.QComboBox(self.groupBox_image_control)
        self.control_image_type_2.setObjectName("control_image_type_2")
        self.control_image_type_2.addItem("")
        self.control_image_type_2.addItem("")
        self.control_image_type_2.addItem("")
        self.control_image_type_2.addItem("")
        self.control_image_type_2.addItem("")
        self.verticalLayout.addWidget(self.control_image_type_2)
        self.gridLayout_8.addWidget(self.groupBox_image_control, 2, 0, 1, 1)
        self.groupBox_image_layers = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_image_layers.sizePolicy().hasHeightForWidth())
        self.groupBox_image_layers.setSizePolicy(sizePolicy)
        self.groupBox_image_layers.setObjectName("groupBox_image_layers")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.groupBox_image_layers)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem = QtWidgets.QSpacerItem(60, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem, 0, 1, 1, 1)
        self.NewLayer = QtWidgets.QPushButton(self.groupBox_image_layers)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.NewLayer.sizePolicy().hasHeightForWidth())
        self.NewLayer.setSizePolicy(sizePolicy)
        self.NewLayer.setMinimumSize(QtCore.QSize(120, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icon/plus-symbol-button.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NewLayer.setIcon(icon)
        self.NewLayer.setObjectName("NewLayer")
        self.gridLayout_2.addWidget(self.NewLayer, 0, 0, 1, 1)
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_image_layers)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 300, 459))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.ImageLayer_Table = QtWidgets.QTableWidget(self.scrollAreaWidgetContents)
        self.ImageLayer_Table.setObjectName("ImageLayer_Table")
        self.ImageLayer_Table.setColumnCount(0)
        self.ImageLayer_Table.setRowCount(0)
        self.gridLayout_4.addWidget(self.ImageLayer_Table, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_2.addWidget(self.scrollArea, 1, 0, 1, 2)
        self.gridLayout_7.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_image_layers, 1, 0, 1, 1)
        self.groupBox_movie_controls = QtWidgets.QGroupBox(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_movie_controls.sizePolicy().hasHeightForWidth())
        self.groupBox_movie_controls.setSizePolicy(sizePolicy)
        self.groupBox_movie_controls.setObjectName("groupBox_movie_controls")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.groupBox_movie_controls)
        self.gridLayout_6.setContentsMargins(2, 2, 2, 2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.Slider_frame = QtWidgets.QSlider(self.groupBox_movie_controls)
        self.Slider_frame.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_frame.setObjectName("Slider_frame")
        self.gridLayout_6.addWidget(self.Slider_frame, 0, 0, 1, 5)
        self.btn_prev = QtWidgets.QPushButton(self.groupBox_movie_controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_prev.sizePolicy().hasHeightForWidth())
        self.btn_prev.setSizePolicy(sizePolicy)
        self.btn_prev.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_prev.setMaximumSize(QtCore.QSize(20, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icon/left-arrow-4.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_prev.setIcon(icon1)
        self.btn_prev.setObjectName("btn_prev")
        self.gridLayout_6.addWidget(self.btn_prev, 1, 0, 1, 1)
        self.btn_play = QtWidgets.QPushButton(self.groupBox_movie_controls)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_play.sizePolicy().hasHeightForWidth())
        self.btn_play.setSizePolicy(sizePolicy)
        self.btn_play.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_play.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_play.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icon/right-arrow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_play.setIcon(icon2)
        self.btn_play.setObjectName("btn_play")
        self.gridLayout_6.addWidget(self.btn_play, 1, 1, 1, 1)
        self.btn_next = QtWidgets.QPushButton(self.groupBox_movie_controls)
        self.btn_next.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_next.sizePolicy().hasHeightForWidth())
        self.btn_next.setSizePolicy(sizePolicy)
        self.btn_next.setMinimumSize(QtCore.QSize(30, 30))
        self.btn_next.setMaximumSize(QtCore.QSize(30, 30))
        self.btn_next.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("icon/right-arrow-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next.setIcon(icon3)
        self.btn_next.setObjectName("btn_next")
        self.gridLayout_6.addWidget(self.btn_next, 1, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(91, 12, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_6.addItem(spacerItem1, 1, 3, 1, 1)
        self.label_frame = QtWidgets.QLabel(self.groupBox_movie_controls)
        self.label_frame.setText("")
        self.label_frame.setObjectName("label_frame")
        self.gridLayout_6.addWidget(self.label_frame, 1, 4, 1, 1)
        self.gridLayout_8.addWidget(self.groupBox_movie_controls, 0, 0, 1, 1)
        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
        self.Control_tab.addTab(self.layer, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.Control_tab.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.Control_tab, 0, 0, 1, 1)
        self.plotWidget = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(240, 0))
        self.plotWidget.setAutoFillBackground(False)
        self.plotWidget.setObjectName("plotWidget")
        self.horizontalLayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1058, 22))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuModules = QtWidgets.QMenu(self.menubar)
        self.menuModules.setObjectName("menuModules")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBar.sizePolicy().hasHeightForWidth())
        self.toolBar.setSizePolicy(sizePolicy)
        self.toolBar.setIconSize(QtCore.QSize(18, 18))
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setEnabled(True)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("icon/open-folder-with-document.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionOpen.setIcon(icon4)
        self.actionOpen.setObjectName("actionOpen")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("icon/power-symbol-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionExit.setIcon(icon5)
        self.actionExit.setObjectName("actionExit")
        self.actionsolarpy = QtWidgets.QAction(MainWindow)
        self.actionsolarpy.setObjectName("actionsolarpy")
        self.actionUndo = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("icon/undo-arrow2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionUndo.setIcon(icon6)
        self.actionUndo.setObjectName("actionUndo")
        self.actionRedo = QtWidgets.QAction(MainWindow)
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("icon/redo-arrow-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionRedo.setIcon(icon7)
        self.actionRedo.setObjectName("actionRedo")
        self.actionslit = QtWidgets.QAction(MainWindow)
        self.actionslit.setCheckable(True)
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("icon/map-route.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionslit.setIcon(icon8)
        self.actionslit.setObjectName("actionslit")
        self.actionTrack = QtWidgets.QAction(MainWindow)
        self.actionTrack.setCheckable(True)
        self.actionTrack.setChecked(True)
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("icon/aim.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionTrack.setIcon(icon9)
        self.actionTrack.setObjectName("actionTrack")
        self.actionLoadChunk = QtWidgets.QAction(MainWindow)
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("icon/download.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionLoadChunk.setIcon(icon10)
        self.actionLoadChunk.setObjectName("actionLoadChunk")
        self.actionDisplay_Header = QtWidgets.QAction(MainWindow)
        self.actionDisplay_Header.setEnabled(False)
        self.actionDisplay_Header.setObjectName("actionDisplay_Header")
        self.actiontestaction = QtWidgets.QAction(MainWindow)
        self.actiontestaction.setObjectName("actiontestaction")
        self.actiontools = QtWidgets.QAction(MainWindow)
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("icon/edit.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actiontools.setIcon(icon11)
        self.actiontools.setObjectName("actiontools")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionExit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionDisplay_Header)
        self.menuEdit.addAction(self.actionUndo)
        self.menuEdit.addAction(self.actionRedo)
        self.menuAbout.addAction(self.actionsolarpy)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuModules.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionUndo)
        self.toolBar.addAction(self.actionRedo)
        self.toolBar.addAction(self.actiontools)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionLoadChunk)
        self.toolBar.addAction(self.actionslit)
        self.toolBar.addAction(self.actionTrack)
        self.toolBar.addAction(self.actiontestaction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox_image_control.setTitle(_translate("MainWindow", "Image Control"))
        self.control_image_type_2.setItemText(0, _translate("MainWindow", "No difference images"))
        self.control_image_type_2.setItemText(1, _translate("MainWindow", "Running difference"))
        self.control_image_type_2.setItemText(2, _translate("MainWindow", "Running difference Ratio"))
        self.control_image_type_2.setItemText(3, _translate("MainWindow", "Base difference"))
        self.control_image_type_2.setItemText(4, _translate("MainWindow", "Base difference Ratio"))
        self.groupBox_image_layers.setTitle(_translate("MainWindow", "Image Layer"))
        self.NewLayer.setText(_translate("MainWindow", "New Layer"))
        self.groupBox_movie_controls.setTitle(_translate("MainWindow", "Movie controls"))
        self.btn_prev.setStatusTip(_translate("MainWindow", "Step to previous frame"))
        self.btn_prev.setShortcut(_translate("MainWindow", "Left"))
        self.btn_play.setStatusTip(_translate("MainWindow", "Play movie"))
        self.btn_next.setStatusTip(_translate("MainWindow", "Step to next frame"))
        self.btn_next.setShortcut(_translate("MainWindow", "Right"))
        self.Control_tab.setTabText(self.Control_tab.indexOf(self.layer), _translate("MainWindow", "Layer"))
        self.Control_tab.setTabText(self.Control_tab.indexOf(self.tab_4), _translate("MainWindow", "Tab 2"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuAbout.setTitle(_translate("MainWindow", "solarpy"))
        self.menuModules.setTitle(_translate("MainWindow", "Modules"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setStatusTip(_translate("MainWindow", "Open new File"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit application"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionsolarpy.setText(_translate("MainWindow", "About solarpy"))
        self.actionUndo.setText(_translate("MainWindow", "Undo"))
        self.actionUndo.setStatusTip(_translate("MainWindow", "Undo"))
        self.actionUndo.setShortcut(_translate("MainWindow", "Ctrl+Z"))
        self.actionRedo.setText(_translate("MainWindow", "Redo"))
        self.actionRedo.setStatusTip(_translate("MainWindow", "Redo"))
        self.actionRedo.setShortcut(_translate("MainWindow", "Ctrl+Shift+Z"))
        self.actionslit.setText(_translate("MainWindow", "Add slit"))
        self.actionslit.setToolTip(_translate("MainWindow", "Add slit"))
        self.actionslit.setStatusTip(_translate("MainWindow", "Add a slit"))
        self.actionTrack.setText(_translate("MainWindow", "Track"))
        self.actionTrack.setToolTip(_translate("MainWindow", "Track"))
        self.actionTrack.setStatusTip(_translate("MainWindow", "De-rotation"))
        self.actionLoadChunk.setText(_translate("MainWindow", "LoadChunk"))
        self.actionLoadChunk.setStatusTip(_translate("MainWindow", "LoadChunk"))
        self.actionDisplay_Header.setText(_translate("MainWindow", "Display Header"))
        self.actiontestaction.setText(_translate("MainWindow", "testaction"))
        self.actiontools.setText(_translate("MainWindow", "tools"))
