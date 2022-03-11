import sys
from PyQt5 import QtWidgets
from modules.ui_main import Ui_MainWindow
from modules.login_ui import Ui_principal

class MyApp(QtWidgets.QMainWindow, Ui_principal):

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.abrir)

    def abrir(self):
        self.ventana = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.ventana)
        self.ventana.show()
 
if __name__ == "__main__":
    app =  QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    app.exec_()