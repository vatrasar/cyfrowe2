# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'templatka.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg
import numpy as np

class Ui_MainWindow(object):



    def setupUi(self, MainWindow,amplitude_before,amplitude_after,time):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 600)
        self.make_plots(amplitude_before,amplitude_after,time)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widok_przed = self.plot
        self.widok_przed.setObjectName("widok_przed")
        self.verticalLayout.addWidget(self.widok_przed)
        self.widok_po = self.plot2
        self.widok_po.setObjectName("widok_po")
        self.verticalLayout.addWidget(self.widok_po)
        self.chara_amplitudowa = QtWidgets.QWidget(self.centralwidget)
        self.chara_amplitudowa.setObjectName("chara_amplitudowa ")
        self.verticalLayout.addWidget(self.chara_amplitudowa )
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 22))
        self.menubar.setObjectName("menubar")
        self.menuEdycja = QtWidgets.QMenu(self.menubar)
        self.menuEdycja.setObjectName("menuEdycja")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionzmie_order = QtWidgets.QAction(MainWindow)
        self.actionzmie_order.setObjectName("actionzmie_order")
        self.menuEdycja.addSeparator()
        self.menuEdycja.addAction(self.actionzmie_order)
        self.menubar.addAction(self.menuEdycja.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menuEdycja.setTitle(_translate("MainWindow", "Edycja"))
        self.actionzmie_order.setText(_translate("MainWindow", "zmień order"))
    def make_plots(self,amplitude_before,amplitude_after,time):
        self.plot = pg.PlotWidget(y=amplitude_before, x=time)
        self.plot2 = pg.PlotWidget(y=amplitude_after, x=time)
