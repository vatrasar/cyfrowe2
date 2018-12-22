from templatka import Ui_MainWindow
from PyQt5 import  QtWidgets,QtCore
import sys
from PyQt5.QtWidgets import QApplication,QDialog,QLabel



class Gui:
    def __init__(self,window):
        self.ui = Ui_MainWindow()
        self.ui.setupUi(window)






if __name__ == "__main__":
    try:


        app = QApplication(sys.argv)
        window=QtWidgets.QMainWindow()
        gui=Gui(window)
        b=gui.ui.menubar.actions()
        window.show()
        sys.exit(app.exec_())
    except ValueError:
        dialog = QDialog()
        ok_button = QLabel("Nie można wczytać tego pliku.\n Proszę wybrać inny.", dialog)
        # ok_button.move(80,50)
        dialog.resize(200, 80)
        dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        dialog.setWindowTitle("Błąd")
        dialog.exec_()