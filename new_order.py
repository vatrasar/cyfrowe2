# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_order.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 97)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label_order = QtWidgets.QLabel(self.centralwidget)
        self.label_order.setObjectName("label_order")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_order)
        self.new_order_num = QtWidgets.QSpinBox(self.centralwidget)
        self.new_order_num.setMaximum(20000)
        self.new_order_num.setObjectName("new_order_num")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.new_order_num)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.SpanningRole, self.buttonBox)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Rząd"))
        self.label_order.setText(_translate("MainWindow", "nowa wartośc rzędu"))

