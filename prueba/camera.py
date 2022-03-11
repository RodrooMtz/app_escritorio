from os import remove, getcwd

from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtCore import Qt, QByteArray, QFile, QByteArray, QIODevice, QBuffer
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QCameraImageCapture
from PyQt5.QtMultimediaWidgets import QCameraViewfinder, QVideoWidget
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QWidget, QFileDialog,
                             QAction, QStyle, QActionGroup, QFrame, QLabel, QStackedWidget,
                             QMessageBox)


class Widgets(QWidget):
    def __init__(self, dispositivoCamara, parent=None):
        super(Widgets, self).__init__(parent)

        self.parent = parent

        self.estadoFoto = False
        self.byteArrayFoto = QByteArray()

        frame = QFrame(self)
        frame.setFrameShape(QFrame.Box)
        frame.setFrameShadow(QFrame.Sunken)
        frame.setFixedWidth(505)
        frame.setFixedHeight(380)
        frame.move(10, 10)

        self.paginaVisor = QVideoWidget()
        self.paginaVisor.resize(500, 375)
        
        self.visor = QCameraViewfinder(self.paginaVisor)
        self.visor.resize(500, 375)

        self.labelFoto = QLabel()
        self.labelFoto.setAlignment(Qt.AlignCenter)
        self.labelFoto.resize(500, 375)

        # QStackedWidget
        self.stackedWidget = QStackedWidget(frame)
        self.stackedWidget.addWidget(self.paginaVisor)
        self.stackedWidget.addWidget(self.labelFoto)
        self.stackedWidget.resize(500, 375)
        self.stackedWidget.move(2, 2)

    def setCamara(self, dispositivoCamara):

        if dispositivoCamara.isEmpty():
            self.camara = QCamera()
        else:
            self.camara = QCamera(dispositivoCamara)

        self.camara.stateChanged.connect(self.actualizarEstadoCamara)

        self.capturaImagen = QCameraImageCapture(self.camara)

        self.camara.setViewfinder(self.visor)

        self.actualizarEstadoCamara(self.camara.state())
        
        self.capturaImagen.imageCaptured.connect(self.procesarImagenCapturada)

        self.capturaImagen.imageSaved.connect(self.imagenGuardada)

        self.camara.isCaptureModeSupported(QCamera.CaptureStillImage)

        self.camara.start()

        self.paginaVisor.update()
        
    def actualizarDispositivoCamara(self, action):
        self.setCamara(action.data())

        

class tomarFoto(QMainWindow):
    def __init__(self, parent = None):
        super(tomarFoto, self).__init__(parent)

        self.setWindowTitle("Tomar foto con PyQt5 por: ANDRES NIÑO")
        self.setWindowIcon(QIcon("Qt.png"))
        self.setWindowFlags(Qt.WindowMinimizeButtonHint | Qt.WindowCloseButtonHint |
                            Qt.MSWindowsFixedSizeDialogHint)
        self.setFixedSize(645, 420)

        camera = QCamera()
        camera.start()
        camera.isCaptureModeSupported(QCamera.CaptureStillImage)
        


if __name__ == '__main__':

    import sys
    
    aplicacion = QApplication(sys.argv)

    ventana = tomarFoto()
    ventana.show()

    sys.exit(aplicacion.exec_())