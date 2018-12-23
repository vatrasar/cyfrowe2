

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(269, 188)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayout_3 = QtWidgets.QFormLayout(self.centralwidget)
        self.formLayout_3.setObjectName("formLayout_3")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.formLayout_2 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.label)
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.widget)
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setObjectName("widget_2")
        self.formLayout = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.signal_a = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.signal_a.setObjectName("signal_a")
        self.signal_a.setMaximum(200000)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.signal_a)
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_3)


        self.signal_f = QtWidgets.QDoubleSpinBox(self.widget_2)
        self.signal_f.setObjectName("signal_f")
        self.signal_f.setMaximum(200000)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.signal_f)
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.widget_2)
        self.button_dialog = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.button_dialog.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_dialog.setObjectName("button_dialog")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.button_dialog)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_4.setText(_translate("MainWindow", "wzór:"))
        self.label.setText(_translate("MainWindow", " a * cos(2 * pi * f * time)"))
        self.label_2.setText(_translate("MainWindow", "a"))
        self.label_3.setText(_translate("MainWindow", "f"))

