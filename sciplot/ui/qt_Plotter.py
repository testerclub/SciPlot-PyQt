# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_Plotter.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1208, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.toolBox = QtWidgets.QToolBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.toolBox.setObjectName("toolBox")
        self.GeneralParameters = QtWidgets.QWidget()
        self.GeneralParameters.setGeometry(QtCore.QRect(0, 0, 176, 332))
        self.GeneralParameters.setObjectName("GeneralParameters")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.GeneralParameters)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.GeneralParameters)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEditTitle = QtWidgets.QLineEdit(self.GeneralParameters)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.verticalLayout_2.addWidget(self.lineEditTitle)
        self.label_2 = QtWidgets.QLabel(self.GeneralParameters)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEditXLabel = QtWidgets.QLineEdit(self.GeneralParameters)
        self.lineEditXLabel.setObjectName("lineEditXLabel")
        self.verticalLayout_2.addWidget(self.lineEditXLabel)
        self.label_3 = QtWidgets.QLabel(self.GeneralParameters)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEditYLabel = QtWidgets.QLineEdit(self.GeneralParameters)
        self.lineEditYLabel.setObjectName("lineEditYLabel")
        self.verticalLayout_2.addWidget(self.lineEditYLabel)
        self.label_4 = QtWidgets.QLabel(self.GeneralParameters)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.comboBoxAspect = QtWidgets.QComboBox(self.GeneralParameters)
        self.comboBoxAspect.setObjectName("comboBoxAspect")
        self.comboBoxAspect.addItem("")
        self.comboBoxAspect.addItem("")
        self.verticalLayout_2.addWidget(self.comboBoxAspect)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem1, 1, 0, 1, 1)
        self.toolBox.addItem(self.GeneralParameters, "")
        self.AxisParameters = QtWidgets.QWidget()
        self.AxisParameters.setObjectName("AxisParameters")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.AxisParameters)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.AxisParameters)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5)
        self.checkBoxAxisVisible = QtWidgets.QCheckBox(self.AxisParameters)
        self.checkBoxAxisVisible.setText("")
        self.checkBoxAxisVisible.setObjectName("checkBoxAxisVisible")
        self.verticalLayout_3.addWidget(self.checkBoxAxisVisible)
        self.label_6 = QtWidgets.QLabel(self.AxisParameters)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEditXLimMin = QtWidgets.QLineEdit(self.AxisParameters)
        self.lineEditXLimMin.setObjectName("lineEditXLimMin")
        self.horizontalLayout.addWidget(self.lineEditXLimMin)
        self.lineEditXLimMax = QtWidgets.QLineEdit(self.AxisParameters)
        self.lineEditXLimMax.setObjectName("lineEditXLimMax")
        self.horizontalLayout.addWidget(self.lineEditXLimMax)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.label_7 = QtWidgets.QLabel(self.AxisParameters)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_3.addWidget(self.label_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEditYLimMin = QtWidgets.QLineEdit(self.AxisParameters)
        self.lineEditYLimMin.setObjectName("lineEditYLimMin")
        self.horizontalLayout_2.addWidget(self.lineEditYLimMin)
        self.lineEditYLimMax = QtWidgets.QLineEdit(self.AxisParameters)
        self.lineEditYLimMax.setObjectName("lineEditYLimMax")
        self.horizontalLayout_2.addWidget(self.lineEditYLimMax)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.label_8 = QtWidgets.QLabel(self.AxisParameters)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_3.addWidget(self.label_8)
        self.comboBoxAxisScaling = QtWidgets.QComboBox(self.AxisParameters)
        self.comboBoxAxisScaling.setObjectName("comboBoxAxisScaling")
        self.comboBoxAxisScaling.addItem("")
        self.comboBoxAxisScaling.addItem("")
        self.comboBoxAxisScaling.addItem("")
        self.comboBoxAxisScaling.addItem("")
        self.comboBoxAxisScaling.addItem("")
        self.verticalLayout_3.addWidget(self.comboBoxAxisScaling)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.gridLayout_3.addLayout(self.verticalLayout_3, 0, 0, 1, 1)
        self.toolBox.addItem(self.AxisParameters, "")
        self.verticalLayout_5.addWidget(self.toolBox)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem3)
        self.gridLayout.addWidget(self.groupBox, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1208, 26))
        self.menubar.setObjectName("menubar")
        self.menuFormat = QtWidgets.QMenu(self.menubar)
        self.menuFormat.setObjectName("menuFormat")
        self.menuFigure_Width_Format = QtWidgets.QMenu(self.menuFormat)
        self.menuFigure_Width_Format.setObjectName("menuFigure_Width_Format")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionStyle = QtWidgets.QAction(MainWindow)
        self.actionStyle.setObjectName("actionStyle")
        self.actionSingle_Column = QtWidgets.QAction(MainWindow)
        self.actionSingle_Column.setObjectName("actionSingle_Column")
        self.actionDouble_Column = QtWidgets.QAction(MainWindow)
        self.actionDouble_Column.setObjectName("actionDouble_Column")
        self.actionJournal_Styles = QtWidgets.QAction(MainWindow)
        self.actionJournal_Styles.setObjectName("actionJournal_Styles")
        self.actionMacro_Schema = QtWidgets.QAction(MainWindow)
        self.actionMacro_Schema.setObjectName("actionMacro_Schema")
        self.menuFigure_Width_Format.addAction(self.actionSingle_Column)
        self.menuFigure_Width_Format.addAction(self.actionDouble_Column)
        self.menuFormat.addAction(self.actionStyle)
        self.menuFormat.addAction(self.menuFigure_Width_Format.menuAction())
        self.menuFormat.addSeparator()
        self.menuFormat.addAction(self.actionJournal_Styles)
        self.menuFormat.addAction(self.actionMacro_Schema)
        self.menubar.addAction(self.menuFormat.menuAction())

        self.retranslateUi(MainWindow)
        self.toolBox.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Title"))
        self.label_2.setText(_translate("MainWindow", "X Label"))
        self.label_3.setText(_translate("MainWindow", "Y Label"))
        self.label_4.setText(_translate("MainWindow", "Aspect Ratio"))
        self.comboBoxAspect.setItemText(0, _translate("MainWindow", "auto"))
        self.comboBoxAspect.setItemText(1, _translate("MainWindow", "equal"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.GeneralParameters), _translate("MainWindow", "General Parameters"))
        self.label_5.setText(_translate("MainWindow", "Axis Visibility"))
        self.label_6.setText(_translate("MainWindow", "X Limits"))
        self.label_7.setText(_translate("MainWindow", "Y Label"))
        self.label_8.setText(_translate("MainWindow", "Scaling"))
        self.comboBoxAxisScaling.setItemText(0, _translate("MainWindow", "auto"))
        self.comboBoxAxisScaling.setItemText(1, _translate("MainWindow", "equal"))
        self.comboBoxAxisScaling.setItemText(2, _translate("MainWindow", "tight"))
        self.comboBoxAxisScaling.setItemText(3, _translate("MainWindow", "image"))
        self.comboBoxAxisScaling.setItemText(4, _translate("MainWindow", "square"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.AxisParameters), _translate("MainWindow", "Axis Parameters"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuFigure_Width_Format.setTitle(_translate("MainWindow", "Figure Width Format"))
        self.actionStyle.setText(_translate("MainWindow", "Color Scheme"))
        self.actionSingle_Column.setText(_translate("MainWindow", "Single-Column"))
        self.actionDouble_Column.setText(_translate("MainWindow", "Double-Column"))
        self.actionJournal_Styles.setText(_translate("MainWindow", "Journal Styles"))
        self.actionMacro_Schema.setText(_translate("MainWindow", "Macro Schema"))

