

from PyQt5 import QtCore, QtGui, QtWidgets
import pyqtgraph as pg


class Ui_MainWindow(object):



    def setupUi(self, MainWindow,amplitude_before,amplitude_after,time,repsonse_fequency,response_gain):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(771, 600)

        self.make_plots(amplitude_before,amplitude_after,time,repsonse_fequency,response_gain)
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
        self.chara_amplitudowa = self.plot3
        self.chara_amplitudowa.setObjectName("chara_amplitudowa ")
        self.verticalLayout.addWidget(self.chara_amplitudowa )
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 771, 22))
        self.menubar.setObjectName("menubar")
        self.menuEdycja = QtWidgets.QMenu(self.menubar)
        self.menuEdycja.setObjectName("menuEdycja")

        self.menu_sygnal = QtWidgets.QMenu(self.menubar)
        self.menu_sygnal.setObjectName("sygnal")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionzmie_order = QtWidgets.QAction(MainWindow)
        self.actionzmie_order.setObjectName("actionzmie_order")
        self.default_signal = QtWidgets.QAction(MainWindow)
        self.default_signal.setObjectName("default_signal")

        self.filter_type = QtWidgets.QAction(MainWindow)
        self.filter_type.setObjectName("filter_type")

        self.new_signal = QtWidgets.QAction(MainWindow)
        self.new_signal.setObjectName("new_signal")

        self.add_signal_part = QtWidgets.QAction(MainWindow)
        self.add_signal_part.setObjectName("signal_part")
        self.menuEdycja.addSeparator()



        self.menuEdycja.addAction(self.actionzmie_order)
        self.menuEdycja.addAction(self.filter_type)
        self.menu_sygnal.addAction(self.add_signal_part)
        self.menu_sygnal.addAction(self.default_signal)
        self.menu_sygnal.addAction(self.new_signal )
        self.menubar.addAction(self.menuEdycja.menuAction())
        self.menubar.addAction(self.menu_sygnal.menuAction())




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Program Edukacyjny"))
        self.menuEdycja.setTitle(_translate("MainWindow", "Edycja filtru"))
        self.menu_sygnal.setTitle(_translate("MainWindow", "Sygnał"))
        self.actionzmie_order.setText(_translate("MainWindow", "Rząd filtru"))
        self.add_signal_part.setText(_translate("MainWindow", "Dodaj składową sygnału"))
        self.default_signal.setText(_translate("MainWindow", "Sygnał domyślny"))
        self.filter_type.setText(_translate("MainWindow", "Przepustowość"))
        self.new_signal.setText(_translate("MainWindow", "Nowy sygnał"))




    def make_plots(self,amplitude_before,amplitude_after,time,repsonse_fequency,response_gain):
        self.plot = pg.PlotWidget(y=amplitude_before, x=time,title="sygnał wejsciowy")
        self.plot2 = pg.PlotWidget(y=amplitude_after, x=time,title="sygnał po filtracji")
        self.plot3=pg.PlotWidget(y=response_gain, x=repsonse_fequency,title="Reakcja na częstotliwość")
        self.plot.setLabel('bottom', "Czas", units='s')
        self.plot.setLabel('left', "Amplituda")
        self.plot2.setLabel('bottom', "Czas", units='s')
        self.plot2.setLabel('left', "Amplituda")
        self.plot3.setLabel('bottom', "Częstotliwość", units='Hz')
        self.plot3.setLabel('left', "Waga")

    def repaint(self,amplitude_before, amplitude_after, time, repsonse_fequency, response_gain):
        self.plot.close()
        self.plot2.close()
        self.plot3.close()
        self.make_plots(amplitude_before, amplitude_after, time, repsonse_fequency, response_gain)
        self.widok_przed = self.plot
        self.widok_przed.setObjectName("widok_przed")
        self.verticalLayout.addWidget(self.widok_przed)
        self.widok_po = self.plot2
        self.widok_po.setObjectName("widok_po")
        self.verticalLayout.addWidget(self.widok_po)
        self.chara_amplitudowa = self.plot3
        self.chara_amplitudowa.setObjectName("chara_amplitudowa ")
        self.verticalLayout.addWidget(self.chara_amplitudowa)
