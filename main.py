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
    b, a = butter(order, [low, high], btype='band')
    return b, a


def butter_bandpass_filter(data, lowcut, highcut, fs, order=5):
    b, a = butter_bandpass(lowcut, highcut, fs, order=order)
    y = lfilter(b, a, data)
    return y

class Gui:
    def __init__(self,window):
        self.order = 6
        self.lowcut=500.0
        self.highcut=1800.0
        self.filter_type = 'band'  # lowpass', 'highpass', 'bandpass', 'bandstop'
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
        if len(self.signal_parts)==0:#default signal
            amplitude_before = 0.1 * np.sin(2 * np.pi * 1.2 * np.sqrt(time))
            amplitude_before += 0.01 * np.cos(2 * np.pi * 312 * time + 0.1)
            amplitude_before += 0.02 * np.cos(2 * np.pi * 600.0 * time + .11)
            amplitude_before += 0.03 * np.cos(2 * np.pi * 2000 * time)
        else:

            for index,signal_part in enumerate(self.signal_parts):
                a = signal_part[0]
                f = signal_part[1]
                if index==0:

                    amplitude_before = a * np.sin(2 * np.pi * f* np.sqrt(time))
                else:
                    amplitude_before += a* np.sin(2 * np.pi * f * np.sqrt(time))

        amplitude_after = butter_bandpass_filter(amplitude_before, lowcut, highcut, fs, order=6)
        b, a = butter_bandpass(lowcut, highcut, fs, order=order)
        w, h = freqz(b, a, worN=2000)
        repsonse_fequency=(fs * 0.5 / np.pi) * w
        response_gain=abs(h)

        return amplitude_before,amplitude_after,time,repsonse_fequency,response_gain
    def accepted_new_signal_part(self):
        f=self.add_signal_ui.signal_a.text()
        a=self.add_signal_ui.signal_f.text()
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

    def open_filter_type_window(self):
        self.filter_type_window = QtWidgets.QMainWindow()
        self.filter_type_ui = filter_type.Ui_MainWindow()
        self.filter_type_ui.setupUi(self.filter_type_window)
        self.filter_type_ui.button_dialog.accepted.connect(self.accepted_new_filter_type)
        self.filter_type_ui.button_dialog.rejected.connect(self.rejected_new_filter_type)

        self.filter_type_window.show()
    def accepted_new_filter_type(self):

        highcut=self.filter_type_ui.filter_highcut.text()
        lowcut=self.filter_type_ui.filter_low_cut.text()
        highcut=highcut.replace(",",".")
        lowcut=lowcut.replace(",",".")
        self.highcut=float(highcut)
        self.lowcut=float(lowcut)
        self.filter_type_window.close()
        amplitude_before, amplitude_after, time, repsonse_fequency, response_gain = self.compute_plots()
        self.ui.repaint(amplitude_before, amplitude_after, time, repsonse_fequency, response_gain)

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
        amplitude_before, amplitude_after, time, repsonse_fequency, response_gain = self.compute_plots()
        self.ui.repaint(amplitude_before, amplitude_after, time, repsonse_fequency, response_gain)



if __name__ == "__main__":

    app = QApplication(sys.argv)
    window=QtWidgets.QMainWindow()
    gui=Gui(window)
    b=gui.ui.menubar.actions()
    window.show()
    sys.exit(app.exec_())
