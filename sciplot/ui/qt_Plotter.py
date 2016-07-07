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
        MainWindow.resize(1104, 892)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolBox.sizePolicy().hasHeightForWidth())
        self.toolBox.setSizePolicy(sizePolicy)
        self.toolBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.toolBox.setObjectName("toolBox")
        self.GlobalLabels = QtWidgets.QWidget()
        self.GlobalLabels.setGeometry(QtCore.QRect(0, 0, 200, 788))
        self.GlobalLabels.setObjectName("GlobalLabels")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.GlobalLabels)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.GlobalLabels)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.lineEditTitle = QtWidgets.QLineEdit(self.GlobalLabels)
        self.lineEditTitle.setObjectName("lineEditTitle")
        self.verticalLayout_2.addWidget(self.lineEditTitle)
        self.label_2 = QtWidgets.QLabel(self.GlobalLabels)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.lineEditXLabel = QtWidgets.QLineEdit(self.GlobalLabels)
        self.lineEditXLabel.setObjectName("lineEditXLabel")
        self.verticalLayout_2.addWidget(self.lineEditXLabel)
        self.label_3 = QtWidgets.QLabel(self.GlobalLabels)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.lineEditYLabel = QtWidgets.QLineEdit(self.GlobalLabels)
        self.lineEditYLabel.setObjectName("lineEditYLabel")
        self.verticalLayout_2.addWidget(self.lineEditYLabel)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.toolBox.addItem(self.GlobalLabels, "")
        self.gridLayout.addWidget(self.toolBox, 0, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1104, 26))
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
        self.toolBox.setItemText(self.toolBox.indexOf(self.GlobalLabels), _translate("MainWindow", "Global Labels"))
        self.menuFormat.setTitle(_translate("MainWindow", "Format"))
        self.menuFigure_Width_Format.setTitle(_translate("MainWindow", "Figure Width Format"))
        self.actionStyle.setText(_translate("MainWindow", "Color Scheme"))
        self.actionSingle_Column.setText(_translate("MainWindow", "Single-Column"))
        self.actionDouble_Column.setText(_translate("MainWindow", "Double-Column"))
        self.actionJournal_Styles.setText(_translate("MainWindow", "Journal Styles"))
        self.actionMacro_Schema.setText(_translate("MainWindow", "Macro Schema"))

