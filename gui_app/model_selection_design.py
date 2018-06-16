# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'model_selection_design.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMaximumSize(QtCore.QSize(800, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(800, 0))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.splitter = QtWidgets.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.label = QtWidgets.QLabel(self.splitter)
        self.label.setObjectName("label")
        self.selectMetric = QtWidgets.QComboBox(self.splitter)
        self.selectMetric.setMinimumSize(QtCore.QSize(100, 10))
        self.selectMetric.setObjectName("selectMetric")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.splitter)
        self.checkShowOnlyBest = QtWidgets.QCheckBox(self.centralwidget)
        self.checkShowOnlyBest.setObjectName("checkShowOnlyBest")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkShowOnlyBest)
        self.btnGo = QtWidgets.QPushButton(self.centralwidget)
        self.btnGo.setObjectName("btnGo")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.btnGo)
        self.verticalLayout.addLayout(self.formLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Select metric"))
        self.checkShowOnlyBest.setText(_translate("MainWindow", "Show only the best model"))
        self.btnGo.setText(_translate("MainWindow", "Go!"))

