from templatka import Ui_MainWindow
from PyQt5 import  QtWidgets,QtCore
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QLabel
from scipy.signal import freqz
from scipy.signal import butter, lfilter
import numpy as np
import addSignalPart
import new_order
import filter_type

def butter_bandpass(lowcut, highcut, fs, order=5):
    w = 0.5 * fs  # Normalize the frequency
    low = lowcut / w
    high = highcut / w
    b, a = butter(order, [low, high], btype='bandpass')
    return b, a


def butter_lowpass(highcut, fs, order):
    w = 0.5 * fs  # Normalize the frequency

    high = highcut / w
    b, a = butter(order, high, btype='lowpass')
    return b, a


def butter_highpass(lowcut, fs, order):
    w = 0.5 * fs  # Normalize the frequency
    low = lowcut / w
    b, a = butter(order, low, btype='highpass')
    return b, a


def butter_bandstop(lowcut, highcut, fs, order):
    w = 0.5 * fs  # Normalize the frequency
    low = lowcut / w
    high = highcut / w
    b, a = butter(order, [low, high], btype='bandstop')
    return b, a


def butter_filter(data, lowcut, highcut, fs, order=5,filter_type='band'):
    b, a = get_filter(filter_type, fs, highcut, lowcut, order)

    y = lfilter(b, a, data)
    return y


def get_filter(filter_type, fs, highcut, lowcut, order):
    # 'lowpass', 'highpass', 'bandpass', 'bandstop'
    if filter_type == 'lowpass':
        b, a = butter_lowpass(highcut, fs, order=order)
    elif filter_type == 'highpass':
        b, a = butter_highpass(lowcut, fs, order=order)
    elif filter_type == 'bandpass':
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    else:
        b, a = butter_bandstop(lowcut, highcut, fs, order=order)
    return b, a


class Gui:
    def __init__(self,window):
        self.order = 6
        self.new_signal=False
        self.lowcut=500.0
        self.highcut=1800.0
        self.filter_type = 'bandpass'  # lowpass', 'highpass', 'bandpass', 'bandstop'
        self.signal_parts = list()
        amplitude_before,amplitude_after,time,repsonse_fequency,response_gain=self.compute_plots()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window,amplitude_before,amplitude_after,time,repsonse_fequency,response_gain)
        self.add_actions()


    def compute_plots(self):
        # Sample rate and desired cutoff frequencies (in Hz).
        fs = 5000.0
        T = 0.05
        lowcut = self.lowcut
        highcut = self.highcut
        nsamples = T * fs
        order=self.order
        time = np.linspace(0, T, nsamples, endpoint=False)

        amplitude_before=None
        if self.new_signal==False:#default signal
            amplitude_before = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(time))
            amplitude_before += 0.01 * np.cos(2 * np.pi * 312 * time + 0.1)
            amplitude_before += 0.02 * np.cos(2 * np.pi * 600.0 * time + .11)
            amplitude_before += 0.03 * np.cos(2 * np.pi * 2000 * time)

        if len(self.signal_parts)==0 and self.new_signal==True:
            b, a = get_filter(self.filter_type, fs, highcut, lowcut, order=order)
            w, h = freqz(b, a, worN=2000)
            repsonse_fequency = (fs * 0.5 / np.pi) * w
            response_gain = abs(h)
            amplitude_after=time*0
            amplitude_before=time*0
            return amplitude_before, amplitude_after, time, repsonse_fequency, response_gain
        for index,signal_part in enumerate(self.signal_parts):
            a = signal_part[0]
            f = signal_part[1]
            if index==0 and self.new_signal==True:

                amplitude_before = a * np.sin(2 * np.pi * f* np.sqrt(time))
            else:
                amplitude_before += a* np.sin(2 * np.pi * f * np.sqrt(time))

        amplitude_after = butter_filter(amplitude_before, lowcut, highcut, fs, order=6,filter_type=self.filter_type)
        b, a = get_filter(self.filter_type,fs,highcut,lowcut, order=order)
        w, h = freqz(b, a, worN=2000)
        repsonse_fequency=(fs * 0.5 / np.pi) * w
        response_gain=abs(h)

        return amplitude_before,amplitude_after,time,repsonse_fequency,response_gain
    def accepted_new_signal_part(self):
        a=self.add_signal_ui.signal_a.text()
        f=self.add_signal_ui.signal_f.text()
        a=a.replace(",",".")
        b=f.replace(",",".")

        self.signal_parts.append([float(a),float(b)])

        self.add_signal_window.close()
        amplitude_before, amplitude_after, time, repsonse_fequency, response_gain=self.compute_plots()
        self.ui.repaint(amplitude_before, amplitude_after, time, repsonse_fequency, response_gain)

    def rejected_new_signal_part(self):
        self.add_signal_window.close()
    def add_actions(self):
        self.ui.add_signal_part.triggered.connect(self.open_add_signal_window)
        self.ui.default_signal.triggered.connect(self.restore_default_signal)
        self.ui.actionzmie_order.triggered.connect(self.change_order)
        self.ui.filter_type.triggered.connect(self.open_filter_type_window)
        self.ui.new_signal.triggered.connect(self.set_new_signal)


    def set_new_signal(self):
        self.new_signal=True
        amplitude_before, amplitude_after, time, repsonse_fequency, response_gain = self.compute_plots()
        self.ui.repaint(amplitude_before, amplitude_after, time, repsonse_fequency, response_gain)
    def open_filter_type_window(self):
        self.filter_type_window = QtWidgets.QMainWindow()
        self.filter_type_ui = filter_type.Ui_MainWindow()
        self.filter_type_ui.setupUi(self.filter_type_window)
        self.filter_type_ui.button_dialog.accepted.connect(self.accepted_new_filter_type)
        self.filter_type_ui.button_dialog.rejected.connect(self.rejected_new_filter_type)

        self.filter_type_ui.filter_type.currentIndexChanged.connect(self.index_changed)
        self.filter_type_window.show()


    def index_changed(self):
        if self.filter_type_ui.filter_type.currentText()=="dolnoprzepustowy":
            self.filter_type_ui.filter_low_cut.setDisabled(True)
            self.filter_type_ui.filter_highcut.setDisabled(False)
        elif self.filter_type_ui.filter_type.currentText()=="górnoprzepustowy":
            self.filter_type_ui.filter_highcut.setDisabled(True)
            self.filter_type_ui.filter_low_cut.setDisabled(False)
        else:
            self.filter_type_ui.filter_low_cut.setDisabled(False)
            self.filter_type_ui.filter_highcut.setDisabled(False)

    def accepted_new_filter_type(self):
        # lowpass', 'highpass', 'bandpass', 'bandstop'
        types={"dolnoprzepustowy":'lowpass',"górnoprzepustowy":'highpass',"środkowozaporowy":'bandstop',"środkowoprzepustowy":'bandpass'}
        highcut=self.filter_type_ui.filter_highcut.text()
        lowcut=self.filter_type_ui.filter_low_cut.text()
        highcut=highcut.replace(",",".")
        lowcut=lowcut.replace(",",".")
        highcut=float(highcut)
        lowcut=float(lowcut)
        new_type=types[self.filter_type_ui.filter_type.currentText()]
        if (highcut <= lowcut and new_type!='lowpass' and new_type!='highpass'):
            self.alter()
            return
        self.highcut=float(highcut)
        self.lowcut=float(lowcut)


        self.filter_type=types[self.filter_type_ui.filter_type.currentText()]

        self.filter_type_window.close()
        amplitude_before, amplitude_after, time, repsonse_fequency, response_gain = self.compute_plots()
        self.ui.repaint(amplitude_before, amplitude_after, time, repsonse_fequency, response_gain)

    def alter(self):
        dialog=QDialog()
        ok_button=QLabel("Błędne dane.",dialog)
        # ok_button.move(80,50)
        dialog.resize(200,80)
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.setWindowTitle("Błąd")
        dialog.exec_()

    def rejected_new_filter_type(self):
        self.filter_type_window.close()
    def change_order(self):
        self.change_order_window = QtWidgets.QMainWindow()
        self.change_order_ui = new_order.Ui_MainWindow()
        self.change_order_ui.setupUi(self.change_order_window)
        self.change_order_ui.buttonBox.accepted.connect(self.accepted_new_order)
        self.change_order_ui.buttonBox.rejected.connect(self.rejected_new_order)

        self.change_order_window.show()
    def accepted_new_order(self):
        self.change_order_window.close()
        new_order=int(self.change_order_ui.new_order_num.text())
        self.order=new_order
        amplitude_before, amplitude_after, time, repsonse_fequency, response_gain = self.compute_plots()
        self.ui.repaint(amplitude_before, amplitude_after, time, repsonse_fequency, response_gain)
    def rejected_new_order(self):
        self.add_signal_window.close()
    def open_add_signal_window(self):
        self.add_signal_window=QtWidgets.QMainWindow()
        self.add_signal_ui=addSignalPart.Ui_MainWindow()
        self.add_signal_ui.setupUi(self.add_signal_window)
        self.add_signal_ui.button_dialog.accepted.connect(self.accepted_new_signal_part)
        self.add_signal_ui.button_dialog.rejected.connect(self.rejected_new_signal_part)

        self.add_signal_window.show()
    def restore_default_signal(self):
        self.signal_parts.clear()
        self.new_signal=False
        amplitude_before, amplitude_after, time, repsonse_fequency, response_gain = self.compute_plots()
        self.ui.repaint(amplitude_before, amplitude_after, time, repsonse_fequency, response_gain)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window=QtWidgets.QMainWindow()
    gui=Gui(window)
    b=gui.ui.menubar.actions()
    window.show()
    sys.exit(app.exec_())
