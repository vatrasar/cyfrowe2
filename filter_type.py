# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filter_type.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(399, 160)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.filter_type = QtWidgets.QComboBox(self.centralwidget)
        self.filter_type.setObjectName("filter_type")
        self.filter_type.addItem("")
        self.filter_type.addItem("")
        self.filter_type.addItem("")
        self.filter_type.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.filter_type)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.filter_low_cut = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.filter_low_cut.setMaximum(2000000.99)
        self.filter_low_cut.setObjectName("filter_low_cut")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.filter_low_cut)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.filter_highcut = QtWidgets.QDoubleSpinBox(self.centralwidget)
        self.filter_highcut.setMaximum(2000000.99)
        self.filter_highcut.setObjectName("filter_highcut")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.filter_highcut)
        self.button_dialog = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.button_dialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_dialog.setObjectName("button_dialog")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.SpanningRole, self.button_dialog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "przepustowość"))
        self.filter_type.setItemText(0, _translate("MainWindow", "dolnoprzepustowy"))
        self.filter_type.setItemText(1, _translate("MainWindow", "górnoprzepustowy"))
        self.filter_type.setItemText(2, _translate("MainWindow", "środkowozaporowy"))
        self.filter_type.setItemText(3, _translate("MainWindow", "środkowoprzepustowy"))
        self.label_2.setText(_translate("MainWindow", "lewy kraniec przedziału"))
        self.label_3.setText(_translate("MainWindow", "prawy kraniec przedziału"))

