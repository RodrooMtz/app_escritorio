# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////
# from _typeshed import NoneType
# from _typeshed import IdentityFunction

from ctypes import string_at
import json
import sys
import os
from urllib.parse import urldefrag
import re

import requests
import pyrebase
import random
import time
import urllib.request
import listas.FCMManager as fcm
import string

from PySide6.QtCore import QDate
from requests.models import HTTPError
from httplib2 import socks
from PyQt5.QtGui import QPixmap, QIcon
from datetime import datetime
from listas.datosLista import datosProducto
from listas.listaClases import datosClase
from PIL.ImageQt import ImageQt
from PIL import Image
from dateutil.relativedelta import relativedelta
from modules import *
from modules import Ui_MainWindow, Settings
from widgets import *
from widgets.custom_grips.custom_grips import Widgets

firebaseConfig = {
    "apiKey": "AIzaSyChD7i5tuQgRClNL24yJ1rvo8ot17N2BGo",
    "authDomain": "resilience66-abd3e.firebaseapp.com",
    "databaseURL": "https://resilience66-abd3e-default-rtdb.firebaseio.com",
    "projectId": "resilience66-abd3e",
    "storageBucket": "resilience66-abd3e.appspot.com",
    "messagingSenderId": "975779634876",
    "serviceAccount": "serviceAccountKey.json",
    "appId": "1:975779634876:web:64ade2008a37e17a35bab9",
    "measurementId": "G-1EFQLX0JEX"}

os.environ["QT_FONT_DPI"] = "96"  # FIX Problem for High DPI and Scale above 100%

# widgets = None
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()
storage = firebase.storage()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        global widgets
        widgets = self.ui

        Settings.ENABLE_CUSTOM_TITLE_BAR = True
        widgets.toggleButton.clicked.connect(lambda: UIFunctions.toggleMenu(self, True))

        UIFunctions.uiDefinitions(self)
        # widgets.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        widgets.titleRightInfo.setText("Iniciar Sesión")
        widgets.leftMenuBg.setVisible(False)

        widgets.txtUsuario.setText("Roy")
        widgets.txtContrasea.setText("12345")

        widgets.txtHoraAgregar.setCurrentText("hora(hh:mm)")

        self.cmbLista()
        d = datetime.now().strftime("%d")
        m = datetime.now().strftime("%m")
        a = datetime.now().strftime("%Y")
        widgets.calendarWidget.setMinimumDate(QDate(int(a), int(m), int(d)))
        widgets.tableWidget.horizontalHeader().setVisible(True)
        widgets.tableWidget_2.horizontalHeader().setVisible(True)
        widgets.tableWidget_3.horizontalHeader().setVisible(True)
        widgets.tableWidget_4.horizontalHeader().setVisible(True)
        widgets.tableWidget_5.horizontalHeader().setVisible(True)
        widgets.tableWidget_6.horizontalHeader().setVisible(True)

        self.listaIdGeneral = []
        self.listaHoras = []
        self.n = 0

        widgets.txtTelefono.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+")))
        widgets.txtEdad.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+")))
        widgets.txtNumCliente.setValidator(QRegularExpressionValidator(QRegularExpression("[0-9]+")))

        # Botones de acción que nos dirigen a las funciones

        widgets.btnRegistrarUsuario.clicked.connect(self.buttonClick)
        widgets.btnReservaClase.clicked.connect(self.buttonClick)
        widgets.btnBuscarUsuario.clicked.connect(self.buttonClick)
        widgets.btnIniciarSesion.clicked.connect(self.buttonClick)
        widgets.btnCerrarSesion.clicked.connect(self.buttonClick)
        widgets.btnRegistrar.clicked.connect(self.buttonClick)
        widgets.btnNuevaSesion.clicked.connect(self.buttonClick)
        widgets.btnBuscar.clicked.connect(self.buscarUsuarios)
        widgets.btnRegistrarEmpleado.clicked.connect(self.buttonClick)
        widgets.btnReservarClase.clicked.connect(self.buttonClick)
        widgets.btnAtras.clicked.connect(self.buttonClick)
        widgets.btnRenovar.clicked.connect(self.renovar)
        widgets.pushButton.clicked.connect(self.eliminarFila)
        widgets.btnRegistroEmpleado.clicked.connect(self.registrarEmpleado)
        widgets.btnCSEnt.clicked.connect(self.cerrarSesion)
        widgets.btnCSPsi.clicked.connect(self.cerrarSesion)
        widgets.btnBEnt.clicked.connect(self.buttonClick)
        widgets.btnBNut.clicked.connect(self.buttonClick)
        widgets.btnBPsi.clicked.connect(self.buttonClick)
        widgets.btnNotificacion.clicked.connect(self.buttonClick)
        widgets.btnAgregar.clicked.connect(self.nuevaSesion)
        widgets.ntBtnEnviar.clicked.connect(self.enviarNot)
        widgets.btnAgregar_2.clicked.connect(self.nuevaHora)
        widgets.btnNuevaClase.clicked.connect(self.NuevaClase)
        widgets.btnImgNut1.clicked.connect(self.buttonClick)
        widgets.btnImgNut4.clicked.connect(self.buttonClick)
        widgets.lblAbrirImg.clicked.connect(self.get_image_file)
        widgets.btnSubirDieta.clicked.connect(self.imgDietaPerso)
        widgets.eliminarClase.clicked.connect(self.eliminarClase)
        widgets.eliminarHora.clicked.connect(self.eliminarHora)

        widgets.chkOpcionRenovar.clicked.connect(self.habilitarCampos)
        widgets.chkOpcionRenovar.clicked.connect(self.nombreProductos)

        widgets.calendarWidget.selectionChanged.connect(self.fechaCalendario)

        widgets.cmbHorario.currentIndexChanged.connect(self.claseCalendario)
        widgets.ntCmbRemitente.currentIndexChanged.connect(self.habilitar2)
        widgets.cmbFechaImg.currentIndexChanged.connect(self.mostrarImgNut)
        widgets.cmbSubirDieta.currentIndexChanged.connect(self.habilitarBoton)

        self.show()

        # SET CUSTOM THEME
        useCustomTheme = False
        themeFile = "themes\py_dracula_light.qss"

        # SET THEME AND HACKS
        if useCustomTheme:
            # LOAD AND APPLY STYLE
            UIFunctions.theme(self, themeFile, True)

            # SET HACKS
            AppFunctions.setThemeHack(self)

        # SET HOME PAGE AND SELECT MENU
        widgets.stackedWidget.setCurrentWidget(widgets.lytLogin)

    # widgets.btn_home.setStyleSheet(UIFunctions.selectMenu(widgets.btn_home.styleSheet()))

    # BUTTONS CLICK
    def buttonClick(self):
        # GET BUTTON CLICKED
        btn = self.sender()
        btnName = btn.objectName()

        # SHOW HOME PAGE
        if btnName == "btnRegistrarUsuario":
            widgets.titleRightInfo.setText("Registrar Usuario")
            widgets.stackedWidget.setCurrentWidget(widgets.lytRegistroUsuario)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.cmbAnadir("Niveles", widgets.cmbNivel)

        # Sección Reservar Sesión
        if btnName == "btnReservaClase":
            widgets.titleRightInfo.setText("Reservar Sesión")
            widgets.stackedWidget.setCurrentWidget(widgets.lytReservar)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.cmbAnadir("Niveles", widgets.cmbHorario)
            widgets.cmbClase.clear()
            widgets.lblNumCliente.setText("")
            widgets.calendarWidget.setStyleSheet("background-color: rgb(220, 220, 220);\n"
                                                 "color: rgb(100, 100, 100);\n"
                                                 "font: 12pt Montserrat;\n"
                                                 "alternate-background-color: rgb(174, 174, 174);\n"
                                                 "selection-background-color: rgb(237, 28, 40);")
            widgets.cmbClase.setStyleSheet("background-color: rgb(220, 220, 220);\n"
                                           "color: rgb(100, 100, 100 );\n"
                                           "font: 10pt Montserrat;")
            widgets.calendarWidget.setEnabled(False)
            widgets.cmbClase.setEnabled(False)

        # Sección Buscar Usuario
        if btnName == "btnBuscarUsuario":
            widgets.titleRightInfo.setText("Buscar Usuario")
            widgets.stackedWidget.setCurrentWidget(widgets.lytBuscarUsuario)  # SET PAGE
            UIFunctions.resetStyle(self, btnName)  # RESET ANOTHERS BUTTONS SELECTED
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))  # SELECT MENU

        # Ejecuta la función iniciarSesion
        if btnName == "btnIniciarSesion":
            self.iniciarSesion()

        # Sección Iniciar Sesión
        if btnName == "btnCerrarSesion":
            widgets.stackedWidget.setCurrentWidget(widgets.lytLogin)
            widgets.leftMenuBg.setVisible(False)
            widgets.titleRightInfo.setText("Iniciar Sesión")
            widgets.txtUsuario.setText("")
            widgets.txtContrasea.setText("")
            widgets.label_6.setText("")
            widgets.label_14.setText("")
            widgets.label_18.setText("")

        # Sección 'Registro de Empleados'
        if btnName == "btnRegistrarEmpleado":
            widgets.titleRightInfo.setText("Registro de Empleados")
            widgets.stackedWidget.setCurrentWidget(widgets.lytEmpleado)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))

        # Sección 'Nueva Sesión'
        if btnName == "btnNuevaSesion":
            widgets.titleRightInfo.setText("Nueva Sesión")
            widgets.stackedWidget.setCurrentWidget(widgets.lytNuevaClase)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.nombreClase()
            self.cmbAnadir("Intensidades", widgets.cmbIntensidad)
            self.cmbAnadir("Niveles", widgets.cmbselecNivel)

        # Sección 'Enviar Notificaciones'
        if btnName == "btnNotificacion":
            widgets.titleRightInfo.setText("Enviar Notificaciones")
            widgets.stackedWidget.setCurrentWidget(widgets.lytNotificacion)
            UIFunctions.resetStyle(self, btnName)
            btn.setStyleSheet(UIFunctions.selectMenu(btn.styleSheet()))
            self.cmbTopics()

        # Ejecuta la función registrar
        if btnName == "btnRegistrar":
            self.registrar()

        # Ejecuta la función reservar
        if btnName == "btnReservarClase":
            self.reservar()

        # Ejecuta la función buscar
        if btnName == "btnBPsi":
            self.buscar(widgets.txtNClientePsi, widgets.lblNClientePsi)

        # Ejecuta la función buscar
        if btnName == "btnBEnt":
            self.buscar(widgets.txtNClienteEnt, widgets.lblNClienteEnt)

        # Ejecuta la función buscar
        if btnName == "btnBNut":
            self.buscar(widgets.txtNClienteNut, widgets.lblNClienteNut)

        # Sección 'Nutrición'
        if btnName == "btnAtras":
            widgets.titleRightInfo.setText("Nutrición")
            widgets.btnAtras.setVisible(False)
            widgets.stackedWidget.setCurrentWidget(widgets.lytNutriologo)

        # Sección Nutrición - 3 fotografías
        if btnName == "btnImgNut1":
            widgets.stackedWidget.setCurrentWidget(widgets.lytWeb)
            widgets.leftMenuBg.setVisible(True)
            widgets.titleRightInfo.setText("Fotografías")
            widgets.btnAtras.setVisible(True)
            widgets.lblfoto1.setPixmap(self.image1)
            widgets.lblfoto2.setPixmap(self.image2)
            widgets.lblfoto3.setPixmap(self.image3)

        # Sección Nutrición - Dieta Anterior
        if btnName == "btnImgNut4":
            widgets.stackedWidget.setCurrentWidget(widgets.lytImgDieta)
            widgets.leftMenuBg.setVisible(True)
            widgets.btnAtras.setVisible(True)
            widgets.titleRightInfo.setText("Dieta Anterior")
            widgets.lblImgDieta.setPixmap(self.image4)

    def validarCampos(self, objeto, etiqueta):
        """Valida si el campo esta vacío, en este caso el borde del campo se cambia a color rojo.
            Parámetros:
                 self : MainWindow
                    indica que se esta trabajando con los objetos de esta ventana
                 objeto : QLineEdit
                    se usa para la entrada de texto
                 etiqueta : QLabel
                    se usa para mostrar texto
            Retorna:
                tipo : booleano
            Excepciones:
                Si (objeto == "") -- return False
        """
        campo = objeto.text()
        if campo == "":
            objeto.setStyleSheet("border: 1px solid red;\n")
            etiqueta.setText("Requerido")
            return False
        else:
            etiqueta.setText("")
            return True

    def buscarUsuarios(self):
        """Busca un usuario en la base de datos de firebase por el numero de usuario.
            Parámetros:
                self : tipo MainWindow
                    Indica que se esta trabajando con los objetos de esta ventana
            Returns
                tipo : string
                    devuelve un mensaje dependiendo que caso es el que cumpla
            Excepciones:
                Si el número de cliente no es encontrado en la base de datos
        """
        numCliente = widgets.txtBuscar.text()
        usuarios = db.child("Usuarios").get(self.tokenWR).val()
        band = True

        for usuario, datos in usuarios.items():
            if numCliente == datos["Número de Cliente"]:
                band = False
                baseNut = datos["Nutriólogo"]
                acceso = baseNut["Acceso"]
                if acceso == "Pe":
                    nutri = "Dieta Personalizada"
                elif acceso == "Ge":
                    nutri = "Dieta General"
                else:
                    nutri = acceso

                NombreM = datos["Stripe"]["Suscripción"]["NombreM"]
                vigencia = int(datos["Stripe"]["Suscripción"]["Vigencia"])
                vigenciaStr = time.strftime("%d-%m-%Y", time.localtime(vigencia))
                widgets.tableWidget.setItem(0, 1, QtWidgets.QTableWidgetItem(datos["Número de Cliente"]))
                widgets.tableWidget.setItem(1, 1, QtWidgets.QTableWidgetItem(datos["Nombre"]))
                widgets.tableWidget.setItem(2, 1, QtWidgets.QTableWidgetItem(datos["Correo"]))
                widgets.tableWidget.setItem(3, 1, QtWidgets.QTableWidgetItem(datos["Teléfono"]))
                widgets.tableWidget.setItem(4, 1, QtWidgets.QTableWidgetItem(datos["Edad"]))
                widgets.tableWidget.setItem(5, 1, QtWidgets.QTableWidgetItem(NombreM))
                widgets.tableWidget.setItem(6, 1, QtWidgets.QTableWidgetItem(datos["Peso"]))
                widgets.tableWidget.setItem(7, 1, QtWidgets.QTableWidgetItem(datos["Estatura"]))
                widgets.tableWidget.setItem(8, 1, QtWidgets.QTableWidgetItem(datos["Sexo"]))
                widgets.tableWidget.setItem(9, 1, QtWidgets.QTableWidgetItem(datos["Clases"]))
                widgets.tableWidget.setItem(10, 1, QtWidgets.QTableWidgetItem("N/A"))
                widgets.tableWidget.setItem(11, 1, QtWidgets.QTableWidgetItem(nutri))
                widgets.tableWidget.setItem(12, 1, QtWidgets.QTableWidgetItem(datos["Nivel"]))
                widgets.tableWidget.setItem(13, 1, QtWidgets.QTableWidgetItem(str(vigenciaStr)))

                automatico = db.child("Usuarios").child(usuario).child("Automático").get(self.tokenWR).val()
                nivel = db.child("Usuarios").child(usuario).child("Nivel").get(self.tokenWR).val()
                widgets.tableWidget_2.clearContents()
                if automatico == "Si":
                    fechaBase = db.child("Fechas").child(nivel).get(self.tokenWR).val()
                    if fechaBase is not None:
                        listaId = []
                        listaHoras = []
                        b = 0
                        v = 0
                        for TFechas, TId in fechaBase.items():
                            v = v + len(TId)
                            widgets.tableWidget_2.setRowCount(v)
                            for id, datosT in TId.items():
                                listaId.append(id)
                                d = datosT["Horas"]
                                listaHoras.append(d)
                                horas = ", ".join(listaHoras[b])
                                widgets.tableWidget_2.setItem(b, 0, QtWidgets.QTableWidgetItem(datosT["Nombre"]))
                                widgets.tableWidget_2.setItem(b, 1, QtWidgets.QTableWidgetItem(TFechas))
                                widgets.tableWidget_2.setItem(b, 2, QtWidgets.QTableWidgetItem(horas))
                                b = b + 1
                        widgets.lblBuscar.setText("")
                    else:
                        widgets.lblBuscar.setText("No tiene clases registradas")
                else:
                    nClases = db.child("Usuarios").child(usuario).child("Mis Clases").get(self.tokenWR).val()
                    if nClases is not None:
                        widgets.tableWidget_2.clearContents()
                        n = 0
                        widgets.tableWidget_2.setRowCount(len(nClases))

                        if nClases is not None:
                            for nomClase, claseHorario in nClases.items():
                                widgets.tableWidget_2.setItem(n, 0, QtWidgets.QTableWidgetItem(claseHorario["Nombre"]))
                                widgets.tableWidget_2.setItem(n, 1, QtWidgets.QTableWidgetItem(claseHorario["Fecha"]))
                                widgets.tableWidget_2.setItem(n, 2, QtWidgets.QTableWidgetItem(claseHorario["Hora"]))
                                n = n + 1
                        widgets.lblBuscar.setText("")
                    else:
                        widgets.lblBuscar.setText("No tiene clases registradas")

                __qtablewidgetitem39 = QTableWidgetItem("SESIÓN")
                __qtablewidgetitem39.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                widgets.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem39)

                __qtablewidgetitem39 = QTableWidgetItem("FECHA")
                __qtablewidgetitem39.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                widgets.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem39)

                __qtablewidgetitem39 = QTableWidgetItem("HORA")
                __qtablewidgetitem39.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                widgets.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem39)

                self.mostrarImagen(usuario)
        if band:
            widgets.lblBuscar.setText("Usuario no encontrado")

    def habilitarCampos(self):
        """ Habilita el combo para seleccionar el plan al que se va a renovar el cliente.
                Excepciones:
                    Si el objeto ChekBox no esta checado
        """
        if widgets.chkOpcionRenovar.isChecked():
            widgets.cmbOpcionRenovar.setDisabled(False)
            widgets.btnRenovar.setDisabled(False)
            widgets.cmbOpcionRenovar.setStyleSheet("color: rgb(0, 0, 0 );\n")
        else:
            widgets.cmbOpcionRenovar.clear()
            widgets.cmbOpcionRenovar.setDisabled(True)
            widgets.btnRenovar.setDisabled(True)
            widgets.cmbOpcionRenovar.setStyleSheet("background-color: rgb(220, 220, 220);\n"
                                                   "color: rgb(100, 100, 100 );\n")

    def fechaCalendario(self):
        """ Visualiza las clases que existen en un determinado dia.
                Excepciones:
                    Si no existen clases registradas:
                        mensaje de error
                Retorna:
                    tipo : lista
                    lista de clases en el formato: nombre de clase - hora

        """
        nivelOpcion = widgets.cmbHorario.currentText()

        dia = widgets.calendarWidget.selectedDate().day()
        mes = widgets.calendarWidget.selectedDate().month()
        anio = widgets.calendarWidget.selectedDate().year()

        fechaSeleccionada = "{}-{}-{}".format(dia, mes, anio)
        fecha = fechaSeleccionada
        fechaC = datetime.strptime(fecha, '%d-%m-%Y')
        self.fechaS = datetime.strftime(fechaC, '%d-%m-%Y')
        fechaBase = db.child("Fechas").child(nivelOpcion).child(self.fechaS).get(self.tokenWR).val()
        if fechaBase is None:
            widgets.lblNumCliente.setText("No hay sesiones para este nivel en esta fecha")
            widgets.cmbClase.clear()
            widgets.cmbClase.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                           "color: rgb(0, 0, 0 );\n"
                                           "font: 10pt Montserrat;")
        else:
            widgets.lblNumCliente.setText("")
            lista = []
            self.listaClases = []
            widgets.cmbClase.clear()
            widgets.cmbClase.setEnabled(True)
            for id, datos in fechaBase.items():
                h = datos["Horas"]
                for horas in h:
                    lista.append(datos["Nombre"] + " - " + horas)
                    self.listaClases.append(
                        datosClase(datos["Nombre"], horas, datos["URL"], id, self.fechaS, datos["Intensidad"]))
            widgets.cmbClase.addItems(lista)
            widgets.cmbClase.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                           "color: rgb(0, 0, 0 );\n"
                                           "font: 10pt Montserrat;")

    def claseCalendario(self):
        """ habilita el objeto calendario QCalendarWidget
            Retorna:
                Habilitar el calendario y cambiar colores
        """
        widgets.calendarWidget.setEnabled(True)
        widgets.calendarWidget.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                             "color: rgb(0, 0, 0 );\n"
                                             "font: 12pt Montserrat;\n"
                                             "alternate-background-color: rgb(174, 174, 174);\n"
                                             "selection-background-color: rgb(237, 28, 40);")

    def registrar(self):
        """registra un usuario a una clase registrada previamente, por numero de usuario.

            Se genera numero de usuario y contraseña5
            Retorna:
                texto - mensaje de registro exitoso
                correo de verificación para el cliente
                texto - número del cliente
            excepciones
                si los campos están vacíos no se registra
                    if validarCampos = False
                si el correo es incorrecto no se registra
                    if es_correo_valido = False

        """
        numeroRandom = db.child("NumeroCliente").get(self.tokenWR).val() + 1
        fechaToday = datetime.now().strftime("%d-%m-%Y")
        character = list(string.ascii_letters + string.digits + "!@#$%&/()")
        random.shuffle(character)
        password = []
        for i in range(8):
            password.append(random.choice(character))
        random.shuffle(password)
        contra = "".join(password)
        nombre = widgets.txtNombre
        apellido = widgets.txtApellido
        correo = widgets.txtCorreo
        telefono = widgets.txtTelefono
        edad = widgets.txtEdad
        sexo = widgets.cmbTipoSexo
        nivel = widgets.cmbNivel
        contrasena = contra
        peso = widgets.txtPeso
        altura = widgets.txtAltura
        etiquetaNombre = widgets.lblNombre
        etiquetaApellido = widgets.lblApellido
        etiquetaCorreo = widgets.lblCorreo
        etiquetaTelefono = widgets.lblTelefono
        etiquetaEdad = widgets.lblEdad
        etiquetaPeso = widgets.lblPeso
        etiquetaAltura = widgets.lblEstatura

        b1 = self.validarCampos(nombre, etiquetaNombre)
        b2 = self.validarCampos(apellido, etiquetaApellido)
        b3 = self.validarCampos(correo, etiquetaCorreo)
        b4 = self.validarCampos(telefono, etiquetaTelefono)
        b5 = self.validarCampos(edad, etiquetaEdad)
        b6 = self.validarCombo(sexo)
        b7 = self.validarCombo(nivel)
        b8 = self.validarCampos(peso, etiquetaPeso)
        b9 = self.validarCampos(altura, etiquetaAltura)

        if b1 and b2 and b3 and b4 and b5 and b6 and b7 and b8 and b9:
            if self.es_correo_valido(correo.text()):
                try:
                    auth.create_user_with_email_and_password(correo.text(), contrasena)
                    auth.sign_in_with_email_and_password(correo.text(), contrasena)
                    usuario = auth.current_user
                    dictUser = dict(usuario)
                    idToken = dictUser['idToken']
                    self.uid = dictUser['localId']
                    auth.send_email_verification(idToken)
                    modalidad = db.child("Listas/Modalidades").child(nivel.currentText()).get(self.tokenWR).val()
                    data = {
                        "Número de Cliente": str(numeroRandom),
                        "Nombre": nombre.text() + " " + apellido.text(),
                        "Correo": correo.text(),
                        "Teléfono": telefono.text(),
                        "Edad": edad.text(),
                        "Peso": peso.text(),
                        "Estatura": altura.text(),
                        "Sexo": sexo.currentText(),
                        "Clases": "0",
                        "Modalidad": modalidad,
                        "Nutriólogo": {
                            "Acceso": "No",
                            "Cuestionario": "No"
                        },
                        "Nivel": nivel.currentText(),
                        "Fecha de Registro": str(fechaToday),
                        "Automático": "No",
                        "Exclusivo": "No",
                        "Stripe": {
                            "Suscripción": {
                                "StatusSus": "none",
                                "Vigencia": 0,
                                "NombreM": "none"
                            }
                        }
                    }
                    db.child("Usuarios").child(self.uid).set(data, self.tokenWR)
                    db.child("NumeroCliente").set(numeroRandom, self.tokenWR)
                    datosS = {'uid': self.uid, 'contra': contra}
                    response = requests.get('https://us-central1-resilience66-abd3e.cloudfunctions.net/enviarCorreo',
                                            params=datosS)
                    if response.status_code != 200:
                        widgets.lblRegistrar.setText("Error enviando el correo de Bienvenida")
                    widgets.lblRegistrar.setText("Se le envío un correo de verificación\r\n"
                                                 "El número de cliente es: " + str(numeroRandom))
                except requests.HTTPError as e:
                    error_json = e.args[1]
                    error = json.loads(error_json)['error']['message']
                    widgets.lblRegistrar.setText("Error al crear la nueva cuenta: " + error)
            else:
                widgets.lblRegistrar.setText("Correo no valido")
        else:
            widgets.lblRegistrar.setText("Por favor escribe los campos obligatorios")

    def reservar(self):
        """ Registra al usuario a una clase seleccionada en el calendario

            excepciones:
                si no se escribe el numero del cliente no se registra
                si no se encuentra el número de cliente
                si la membresía del cliente esta activa
                si el cliente no tiene sesiones registradas
                si el cliente no tiene nivel
                si el nivel de la sesión coincide con el nivel del cliente
                si las sesiones no se le inscriben al usuario en automático
                si el usuario no selecciono una fecha en el calendario
                si el usuario no selecciono el nombre y hora de la sesión
                si la sesión esta vencida
                si la sesión se registro antes
            Retorna:
                texto - mensaje de clase registrada con éxito

        """
        textoNumCliente = widgets.txtNumCliente.text()
        usuarios = db.child("Usuarios").get(self.tokenWR).val()
        nivelClase = widgets.cmbHorario.currentText()
        nombreClase = widgets.cmbClase.currentText()
        index = widgets.cmbClase.currentIndex()
        fechaSeleccionada = widgets.calendarWidget.selectedDate()
        b = False
        if textoNumCliente != "":
            for usuario, datos in usuarios.items():
                if textoNumCliente == datos["Número de Cliente"]:
                    membresia = db.child("Usuarios").child(usuario).child("Stripe").child("Suscripción").child(
                        "StatusSus").get(self.tokenWR).val()
                    if membresia == "active":
                        if datos["Clases"] != "0":
                            if nivelClase != "":
                                nivelBase = db.child("Usuarios").child(usuario).child("Nivel").get(self.tokenWR).val()
                                automatico = db.child("Usuarios").child(usuario).child("Automático").get(
                                    self.tokenWR).val()
                                if nivelClase == nivelBase:
                                    if automatico == "No":
                                        if fechaSeleccionada != QDate(2021, 8, 2):
                                            id = self.listaClases[index].id
                                            nombre = self.listaClases[index].nombreClase
                                            hora = self.listaClases[index].hora
                                            url = self.listaClases[index].url
                                            fecha = self.listaClases[index].fecha
                                            intensidad = self.listaClases[index].intensidad
                                            if nombreClase != "":
                                                da = datos["Stripe"]
                                                dat = da["Suscripción"]
                                                vigencia = dat["Vigencia"]
                                                diaHoy = time.time() - 610

                                                horaFecha = fecha + " " + hora
                                                fechaf = datetime.strptime(horaFecha, "%d-%m-%Y %H:%M")
                                                fechaEpoch = fechaf.timestamp()

                                                if diaHoy < fechaEpoch < vigencia:
                                                    b = True
                                                    ids = db.child("Usuarios").child(usuario).child("Mis Clases").get(
                                                        self.tokenWR).val()
                                                    if ids is not None:
                                                        for id2 in ids.keys():
                                                            if id2 == id:
                                                                b = False
                                                                break
                                                    if b:
                                                        NumClase = datos["Clases"]
                                                        RestarClase = int(NumClase) - 1
                                                        db.child("Usuarios").child(usuario).child("Clases").set(
                                                            str(RestarClase), self.tokenWR)
                                                        dataClase = {
                                                            "Fecha": fecha,
                                                            "Hora": hora,
                                                            "Intensidad": intensidad,
                                                            "Nombre": nombre,
                                                            "URL": url
                                                        }
                                                        db.child("Usuarios").child(usuario).child("Mis Clases").child(
                                                            id).set(dataClase, self.tokenWR)
                                                        data = {usuario: hora}
                                                        db.child("Fechas").child(nivelClase).child(fecha).child(
                                                            id).child("Inscritos").set(data, self.tokenWR)

                                                        widgets.lblNumCliente.setText("Sesión reservada con éxito")
                                                        break
                                                    else:
                                                        widgets.lblNumCliente.setText("Ya se reservó antes la sesión")
                                                        break
                                                else:
                                                    widgets.lblNumCliente.setText("La sesión esta vencida")
                                                    break
                                            else:
                                                widgets.cmbClase.setStyleSheet("border: 1px solid red;\n"
                                                                               "background-color: rgb(221, 221, 221);\n"
                                                                               "color: rgb(0, 0, 0 );\n"
                                                                               "font: 10pt Montserrat;")
                                                break
                                        else:
                                            widgets.lblNumCliente.setText("Seleccione una fecha")
                                            break
                                    else:
                                        widgets.lblNumCliente.setText("Sesiones ya reservadas")
                                        break
                                else:
                                    widgets.lblNumCliente.setText("No puede reservar sesiones de otro nivel")
                                    break
                            else:
                                widgets.cmbHorario.setStyleSheet("border: 1px solid red;\n"
                                                                 "background-color: rgb(221, 221, 221);\n"
                                                                 "color: rgb(0, 0, 0 );\n"
                                                                 "font: 10pt Montserrat;")
                                break
                        else:
                            widgets.lblNumCliente.setText("No tienes sesiones disponibles")
                            break
                    else:
                        widgets.lblNumCliente.setText("La membresía esta inactiva")
                        break
                else:
                    widgets.lblNumCliente.setText("Número de cliente no encontrado")
        elif not b:
            widgets.lblNumCliente.setText("Escribe el numero de cliente")

    # RESIZE EVENTS
    def resizeEvent(self, event):
        # Update Size Grips
        UIFunctions.resize_grips(self)

    # MOUSE CLICK EVENTS
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()

    def nombreProductos(self):
        """ Agrega la lista de productos de la base de datos al combo cmbOpcionRenovar

            Excepciones:
                si no se escribió el numero de cliente
                si el objeto checkBox no esta checado
            Retorna:
               lista - lista de los nombres de los productos
        """
        self.lista = []
        if widgets.txtBuscar.text() != "":
            productos = db.child("Productos").get(self.tokenWR).val()
            if widgets.chkOpcionRenovar.isChecked():
                for idProducto, nombre in productos.items():
                    self.lista.append(
                        datosProducto(
                            nombre["Nombre"],
                            nombre["Clases"],
                            nombre["Nutriólogo"],
                            nombre["Precio"],
                            nombre["Tipo"],
                            nombre["PrecioID"],
                            nombre["Exclusivo"],
                            idProducto,
                            nombre["Expiración"],
                            nombre["Modalidad"]
                        )
                    )
                    widgets.cmbOpcionRenovar.addItem(nombre["Nombre"])
        else:
            widgets.lblBuscar.setText("Escribe el nombre de usuario")
            widgets.chkOpcionRenovar.setChecked(False)

    def mostrarImagen(self, uid):
        """ Muestra la foto de perfil del cliente previamente subida por el en la aplicación móvil.

                Parámetros:
                    uid : string
                        numero único que identifica al cliente en la base de datos
                Excepciones:
                    Si la respuesta del servidor es un error: texto - mensaje de error
                Retorna:
                    pixmap - imagen de la base de datos

        """
        widgets.lblFotoPerfil.setPixmap(None)
        try:
            url = storage.child("Fotos Perfil").child(uid).get_url(None)
            data = urllib.request.urlopen(url).read()
            pixmap = QPixmap()
            pixmap.loadFromData(data)
            widgets.lblFotoPerfil.setPixmap(pixmap)
        except requests.HTTPError as e:
            error_json = e.args[1]
            error = json.loads(error_json)['error']
            widgets.lblRegistrar.setText("Error al crear la nueva cuenta: " + error)

    def mostrarImgNut(self):
        """ Carga los datos de imagen en una variable que después sera mostrada en label

            Excepciones:
                si no se encuentra el número del cliente
            Retorna:
               3 pixmap - imágenes descargadas de la base de datos

        """
        numCliente = widgets.txtNClienteNut.text()
        usuarios = db.child("Nutrición").get(self.tokenWR).val()
        fechaImgNut = widgets.cmbFechaImg.currentText()

        for usuario, datos in usuarios.items():
            if numCliente == datos["Número de Cliente"]:
                widgets.btnImgNut1.setEnabled(True)
                widgets.btnImgNut1.setStyleSheet("background-color: rgb(237, 28, 40);\n")

                url = storage.child("Nutrición").child(usuario).child(fechaImgNut).child("Foto1").get_url(None)
                data = urllib.request.urlopen(url).read()
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                self.image1 = pixmap

                url = storage.child("Nutrición").child(usuario).child(fechaImgNut).child("Foto2").get_url(None)
                data = urllib.request.urlopen(url).read()
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                self.image2 = pixmap

                url = storage.child("Nutrición").child(usuario).child(fechaImgNut).child("Foto3").get_url(None)
                data = urllib.request.urlopen(url).read()
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                self.image3 = pixmap

    def renovar(self):
        """ Sustituye la suscripción registrada en la base de datos con la que tiene el cliente.

            Excepciones:
                Se renueva la suscripción si cumple con los siguientes requisitos:
                    El campo número de cliente no esta vacío
                    Se selecciono una opción en el combo cmbOpcionRenovar
                    La selección del combo coincide con el nombre del producto de la base de datos
                    Si el número de cliente existe en la base de datos
                    La modalidad del usuario coincide con la del producto

        """
        opcionMembresia = widgets.cmbOpcionRenovar.currentText()
        index = widgets.cmbOpcionRenovar.currentIndex()
        nombre = self.lista[index].nombre
        precioId = self.lista[index].precioId
        tipo = self.lista[index].tipo
        precio = self.lista[index].precio
        exclusivo = self.lista[index].exclusivo
        expiracion = self.lista[index].expiracion
        idProducto = self.lista[index].idProducto
        clases = self.lista[index].clases
        nutriologo = self.lista[index].nutriologo
        modalidadP = self.lista[index].modalidad
        numCliente = widgets.txtBuscar.text()
        usuarios = db.child("Usuarios").get(self.tokenWR).val()
        global nuevoNivel

        if numCliente != "":
            if opcionMembresia != "":
                if opcionMembresia == nombre:
                    bandera = True
                    for usuario, datos in usuarios.items():
                        if numCliente == datos["Número de Cliente"]:
                            bandera = False
                            modalidadU = datos["Modalidad"]
                            nivelU = datos["Nivel"]
                            estatus = datos["Stripe"]["Suscripción"]["StatusSus"]
                            widgets.btnRenovar.setEnabled(False)
                            vigencia = datos["Stripe"]["Suscripción"]["Vigencia"]
                            fechaHoy = time.time()
                            if modalidadU != modalidadP:
                                b = False
                                if modalidadP == "Athlete":
                                    dialogo = QMessageBox.question(
                                        self, "Cambio de nivel", "Actualmente se encuentra en la modalidad "
                                                                 f"{modalidadU}, al realizar esta compra cambiará a la "
                                                                 f"modalidad {modalidadP}, ¿Desea continuar con "
                                                                 "la compra?")
                                    if dialogo == QMessageBox.No:
                                        print("No")
                                    elif dialogo == QMessageBox.Yes:
                                        if tipo == "recurring":
                                            if (vigencia < fechaHoy or estatus != "active") and estatus != "past_due":
                                                customer = datos["Stripe"]["StripeID"]
                                                datosS = {'customer': customer, 'priceId': precioId, 'tipo': tipo}
                                                response = requests.get(
                                                    'https://us-central1-resilience66-abd3e.cloudfunctions.net/pythonS',
                                                    params=datosS
                                                )
                                                if response.status_code == 200:
                                                    nUsuario = widgets.txtUsuario.text()
                                                    textoJson = response.json()
                                                    print(textoJson)
                                                    data = {
                                                        "Responsable": nUsuario,
                                                        "Número de Cliente": datos["Número de Cliente"],
                                                        "PaymentIntent": textoJson["PaymentIntent"],
                                                        "Factura": textoJson["Invoice"],
                                                        "Fecha": str(datetime.now()),
                                                        "Precio": precio
                                                    }
                                                    db.child("Suscripciones Stripe").child(textoJson[
                                                                                               "IDSuscripcion"]).set(
                                                        data,
                                                        self.tokenWR)
                                                    print(textoJson['IDSuscripcion'])
                                                    widgets.lblBuscar.setText("Suscripción actualizada exitosamente")
                                                    widgets.btnRenovar.setEnabled(True)
                                                    # habilitar boton
                                                    break
                                                else:
                                                    # Habilitar boton
                                                    widgets.btnRenovar.setEnabled(True)
                                                    widgets.lblBuscar.setText(response.text, response.status_code)
                                                    break
                                            elif estatus == "" or estatus is None:
                                                widgets.lblBuscar.setText("Error obteniendo los datos de su cuenta")
                                                break
                                            else:
                                                widgets.lblBuscar.setText("Ya cuenta con una suscripción o paquete")
                                                break
                                        else:
                                            ahora = datetime.now()
                                            global epochVigencia, nuevoNivel
                                            if float(expiracion) < 1:
                                                mas2Semanas = ahora + relativedelta(weeks=2)
                                                epochVigencia = mas2Semanas.timestamp()
                                            else:
                                                masNMeses = ahora + relativedelta(months=int(expiracion))
                                                epochVigencia = masNMeses.timestamp()
                                            if (vigencia < fechaHoy or estatus != "active") and estatus != "past_due":
                                                vigenciaE = int(epochVigencia)

                                                db.child("Usuarios").child(usuario).child("Clases").set(clases,
                                                                                                        self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Exclusivo").set(exclusivo,
                                                                                                           self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Nutriólogo").child(
                                                    "Acceso").set(
                                                    nutriologo, self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Nivel").set("ATHLETE 66",
                                                                                                       self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Modalidad").set("Athlete",
                                                                                                           self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Stripe").child(
                                                    "Suscripción").child(
                                                    "Producto").set(idProducto, self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Stripe").child(
                                                    "Suscripción").child(
                                                    "NombreM").set(nombre, self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Stripe").child(
                                                    "Suscripción").child(
                                                    "Tipo").set(tipo, self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Stripe").child(
                                                    "Suscripción").child(
                                                    "StatusSus").set("active", self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Stripe").child(
                                                    "Suscripción").child(
                                                    "Vigencia").set(vigenciaE, self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Stripe").child(
                                                    "Suscripción").child(
                                                    "Precio").set(precioId, self.tokenWR)
                                                db.child("Usuarios").child(usuario).child("Automático").set("No",
                                                                                                            self.tokenWR)

                                                datosConsumible = {
                                                    "Factura": "paid",
                                                    "Fecha": str(datetime.now()),
                                                    "Número de Cliente": datos["Número de Cliente"],
                                                    "PaymentIntent": "Consumible",
                                                    "Responsable": widgets.txtUsuario.text(),
                                                    "Precio": precio
                                                }
                                                db.child("Suscripciones Stripe").push(datosConsumible, self.tokenWR)

                                                widgets.lblBuscar.setText("Suscripción actualizada exitosamente")
                                                widgets.btnRenovar.setEnabled(True)
                                                break
                                            elif estatus == "" or estatus is None:
                                                widgets.lblBuscar.setText("Error obteniendo los datos de su cuenta")
                                                break
                                            else:
                                                widgets.lblBuscar.setText("Ya cuenta con una suscripción o paquete")
                                                break
                                elif modalidadU == "Athlete":
                                    QMessageBox.information(self, "Aviso", f"Lo sentimos el nivel {nivelU} no se "
                                                                           "encuentra disponible en la modalidad "
                                                                           f"{modalidadP}. Contacte a soporte para "
                                                                           "cambiar de nivel o modalidad.",
                                                            QMessageBox.Ok)
                                else:
                                    proporcion = db.child("Listas").child("Proporcionalidades").get(self.tokenWR).val()

                                    for nivel, valor in proporcion.items():
                                        if nivel == nivelU:
                                            b = True
                                            nuevoNivel = valor
                                            break
                                        if valor == nivelU:
                                            b = True
                                            nuevoNivel = nivel
                                            break
                                    if b:
                                        dialogo = QMessageBox.question(
                                            self, "Cambio de nivel", "Actualmente se encuentra en la modalidad "
                                                                     f"{modalidadU}, al realizar esta compra cambiará a la "
                                                                     f"modalidad {modalidadP}, ¿Desea continuar con "
                                                                     "la compra?")
                                        if dialogo == QMessageBox.No:
                                            print("No")
                                        elif dialogo == QMessageBox.Yes:
                                            if tipo == "recurring":
                                                if (vigencia < fechaHoy or estatus != "active") and estatus != "past_due":
                                                    customer = datos["Stripe"]["StripeID"]
                                                    datosS = {'customer': customer, 'priceId': precioId, 'tipo': tipo}
                                                    response = requests.get(
                                                        'https://us-central1-resilience66-abd3e.cloudfunctions.net/pythonS',
                                                        params=datosS
                                                    )
                                                    if response.status_code == 200:
                                                        nUsuario = widgets.txtUsuario.text()
                                                        textoJson = response.json()
                                                        print(textoJson)
                                                        data = {
                                                            "Responsable": nUsuario,
                                                            "Número de Cliente": datos["Número de Cliente"],
                                                            "PaymentIntent": textoJson["PaymentIntent"],
                                                            "Factura": textoJson["Invoice"],
                                                            "Fecha": str(datetime.now()),
                                                            "Precio": precio
                                                        }
                                                        db.child("Suscripciones Stripe").child(textoJson[
                                                                                                   "IDSuscripcion"]).set(
                                                            data,
                                                            self.tokenWR)
                                                        print(textoJson['IDSuscripcion'])
                                                        widgets.lblBuscar.setText(
                                                            "Suscripción actualizada exitosamente")
                                                        widgets.btnRenovar.setEnabled(True)
                                                        # habilitar boton
                                                        break
                                                    else:
                                                        # Habilitar boton
                                                        widgets.btnRenovar.setEnabled(True)
                                                        widgets.lblBuscar.setText(response.text, response.status_code)
                                                        break
                                                elif estatus == "" or estatus is None:
                                                    widgets.lblBuscar.setText("Error obteniendo los datos de su cuenta")
                                                    break
                                                else:
                                                    widgets.lblBuscar.setText("Ya cuenta con una suscripción o paquete")
                                                    break
                                            else:
                                                ahora = datetime.now()
                                                global epochVigencia1
                                                if float(expiracion) < 1:
                                                    mas2Semanas = ahora + relativedelta(weeks=2)
                                                    epochVigencia1 = mas2Semanas.timestamp()
                                                else:
                                                    masNMeses = ahora + relativedelta(months=int(expiracion))
                                                    epochVigencia1 = masNMeses.timestamp()
                                                if (
                                                        vigencia < fechaHoy or estatus != "active") and estatus != "past_due":
                                                    vigenciaE = int(epochVigencia1)
                                                    db.child("Usuarios").child(usuario).child("Clases").set(clases,
                                                                                                            self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Exclusivo").set(
                                                        exclusivo,
                                                        self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Nutriólogo").child(
                                                        "Acceso").set(
                                                        nutriologo, self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Modalidad").set(
                                                        modalidadP, self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Nivel").set(nuevoNivel,
                                                                                                           self.tokenWR)

                                                    db.child("Usuarios").child(usuario).child("Stripe").child(
                                                        "Suscripción").child(
                                                        "Producto").set(idProducto, self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Stripe").child(
                                                        "Suscripción").child(
                                                        "NombreM").set(nombre, self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Stripe").child(
                                                        "Suscripción").child(
                                                        "Tipo").set(tipo, self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Stripe").child(
                                                        "Suscripción").child(
                                                        "StatusSus").set("active", self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Stripe").child(
                                                        "Suscripción").child(
                                                        "Vigencia").set(float(vigenciaE), self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Stripe").child(
                                                        "Suscripción").child(
                                                        "Precio").set(precioId, self.tokenWR)
                                                    db.child("Usuarios").child(usuario).child("Automático").set("No",
                                                                                                                self.tokenWR)

                                                    datosConsumible = {
                                                        "Factura": "paid",
                                                        "Fecha": str(datetime.now()),
                                                        "Número de Cliente": datos["Número de Cliente"],
                                                        "PaymentIntent": "Consumible",
                                                        "Responsable": widgets.txtUsuario.text(),
                                                        "Precio": precio
                                                    }
                                                    db.child("Suscripciones Stripe").push(datosConsumible, self.tokenWR)

                                                    widgets.lblBuscar.setText("Suscripción actualizada exitosamente")
                                                    widgets.btnRenovar.setEnabled(True)
                                                    break
                                                elif estatus == "" or estatus is None:
                                                    widgets.lblBuscar.setText("Error obteniendo los datos de su cuenta")
                                                    break
                                                else:
                                                    widgets.lblBuscar.setText("Ya cuenta con una suscripción o paquete")
                                                    break
                                    else:
                                        QMessageBox.information(self, "Aviso", f"Lo sentimos el nivel {nivelU} no se "
                                                                               "encuentra disponible en la modalidad "
                                                                               f"{modalidadP}. Contacte a soporte "
                                                                               "para cambiar de nivel o modalidad.",
                                                                QMessageBox.Ok)
                            else:
                                if tipo == "recurring":
                                    if (vigencia < fechaHoy or estatus != "active") and estatus != "past_due":
                                        customer = datos["Stripe"]["StripeID"]
                                        datosS = {'customer': customer, 'priceId': precioId, 'tipo': tipo}
                                        response = requests.get(
                                            'https://us-central1-resilience66-abd3e.cloudfunctions.net/pythonS',
                                            params=datosS
                                        )
                                        if response.status_code == 200:
                                            nUsuario = widgets.txtUsuario.text()
                                            textoJson = response.json()
                                            print(textoJson)
                                            data = {
                                                "Responsable": nUsuario,
                                                "Número de Cliente": datos["Número de Cliente"],
                                                "PaymentIntent": textoJson["PaymentIntent"],
                                                "Factura": textoJson["Invoice"],
                                                "Fecha": str(datetime.now()),
                                                "Precio": precio
                                            }
                                            db.child("Suscripciones Stripe").child(textoJson[
                                                                                       "IDSuscripcion"]).set(
                                                data,
                                                self.tokenWR)
                                            print(textoJson['IDSuscripcion'])
                                            widgets.lblBuscar.setText("Suscripción actualizada exitosamente")
                                            widgets.btnRenovar.setEnabled(True)
                                            # habilitar boton
                                            break
                                        else:
                                            # Habilitar boton
                                            widgets.btnRenovar.setEnabled(True)
                                            widgets.lblBuscar.setText(response.text, response.status_code)
                                            break
                                    elif estatus == "" or estatus is None:
                                        widgets.lblBuscar.setText("Error obteniendo los datos de su cuenta")
                                        break
                                    else:
                                        widgets.lblBuscar.setText("Ya cuenta con una suscripción o paquete")
                                        break
                                else:
                                    ahora = datetime.now()
                                    global epochVigencia2
                                    if float(expiracion) < 1:
                                        mas2Semanas = ahora + relativedelta(weeks=2)
                                        epochVigencia2 = mas2Semanas.timestamp()
                                    else:
                                        masNMeses = ahora + relativedelta(months=int(expiracion))
                                        epochVigencia2 = masNMeses.timestamp()
                                    if (vigencia < fechaHoy or estatus != "active") and estatus != "past_due":
                                        vigenciaE = int(epochVigencia2)
                                        db.child("Usuarios").child(usuario).child("Clases").set(clases,
                                                                                                self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Exclusivo").set(exclusivo,
                                                                                                   self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Nutriólogo").child(
                                            "Acceso").set(
                                            nutriologo, self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Stripe").child(
                                            "Suscripción").child(
                                            "Producto").set(idProducto, self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Stripe").child(
                                            "Suscripción").child(
                                            "NombreM").set(nombre, self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Stripe").child(
                                            "Suscripción").child(
                                            "Tipo").set(tipo, self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Stripe").child(
                                            "Suscripción").child(
                                            "StatusSus").set("active", self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Stripe").child(
                                            "Suscripción").child(
                                            "Vigencia").set(vigenciaE, self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Stripe").child(
                                            "Suscripción").child(
                                            "Precio").set(precioId, self.tokenWR)
                                        db.child("Usuarios").child(usuario).child("Automático").set("No",
                                                                                                    self.tokenWR)

                                        datosConsumible = {
                                            "Factura": "paid",
                                            "Fecha": str(datetime.now()),
                                            "Número de Cliente": datos["Número de Cliente"],
                                            "PaymentIntent": "Consumible",
                                            "Responsable": widgets.txtUsuario.text(),
                                            "Precio": precio
                                        }
                                        db.child("Suscripciones Stripe").push(datosConsumible, self.tokenWR)

                                        widgets.lblBuscar.setText("Suscripción actualizada exitosamente")
                                        widgets.btnRenovar.setEnabled(True)
                                        break
                                    elif estatus == "" or estatus is None:
                                        widgets.lblBuscar.setText("Error obteniendo los datos de su cuenta")
                                        break
                                    else:
                                        widgets.lblBuscar.setText("Ya cuenta con una suscripción o paquete")
                                        break
                    if bandera:
                        widgets.lblBuscar.setText("Usuario no encontrado")
                else:
                    widgets.lblBuscar.setText("El producto no esta en existencia")
            else:
                widgets.lblBuscar.setText("Seleccione una opción ")
        else:
            widgets.lblBuscar.setText("Escriba un número de usuario")

    def registrarEmpleado(self):
        """ Se crea un usuario nuevo para que pueda ingresar a esta aplicación de escritorio
                Retorna:
                    mensaje de registro exitoso
                Se crea el registro si:
                    Los campos requeridos no están vacíos
                    El campo contraseña y repetir contraseña son iguales
                    El número de caracteres de la contraseña es mayor a 10
        """
        nombre = widgets.txtNombreEmpleado
        tipo = widgets.cmbTipoEmpleado.currentText()
        contrasena = widgets.txtContrasenaEmpleado
        repContrasena = widgets.txtRepetirContrasena

        etiquetaNombre = widgets.lblNombre_2
        etiquetaContrasena = widgets.lblTelefono_2
        etiquetaRepContrasena = widgets.lblEdad_2

        b1 = self.validarCampos(nombre, etiquetaNombre)
        b4 = self.validarCampos(contrasena, etiquetaContrasena)
        b5 = self.validarCampos(repContrasena, etiquetaRepContrasena)
        if b1 and b4 and b5:
            if contrasena.text() == repContrasena.text():
                if len(contrasena.text()) >= 10:
                    data = {
                        "Nombre": nombre.text(),
                        "Tipo": tipo,
                        "Contrasena": contrasena.text()
                    }
                    db.child("Empleados").push(data, self.tokenWR)
                    widgets.lblTipoMembresia_2.setText("Registro Exitoso")
                else:
                    widgets.lblTipoMembresia_2.setText("Escribir al menos 10 caracteres")
            else:
                widgets.lblTipoMembresia_2.setText("Las contraseñas no son iguales")
        else:
            widgets.lblTipoMembresia_2.setText("Escribe en los campos requeridos")

    def iniciarSesion(self):
        """ El usuario accede a la aplicación
                Excepciones:
                    El usuario no puede acceder a la aplicación si:
                        Los campos Usuario, contraseña y tipo de empleado están vacíos
                        El usuario existe en la base de datos con su tipo de empleado y contraseña
                Retorna:
                    Una interfaz de inicio dependiendo de la opción seleccionada

                El usuario accederá a un menu diferente dependiendo de su tipo de usuario
                Se genera un token único si se tiene usuario
        """
        usuario = widgets.txtUsuario
        contrasena = widgets.txtContrasea
        tipo = widgets.cmbTipoDeUsuario.currentText()

        etiquetaUsuario = widgets.label_6
        etiquetaContrasena = widgets.label_14
        empleados = db.child("Empleados").get().val()

        b1 = self.validarCampos(usuario, etiquetaUsuario)
        b2 = self.validarCampos(contrasena, etiquetaContrasena)

        if b1 and b2:
            for idEmpleado, datos in empleados.items():
                if usuario.text() == datos["Nombre"]:
                    if tipo == datos["Tipo"]:
                        if contrasena.text() == datos["Contrasena"]:
                            if tipo == "Recepcionista":
                                self.ui.leftMenuFrame.setEnabled(True)
                                widgets.stackedWidget.setCurrentWidget(widgets.lytBuscarUsuario)
                                widgets.leftMenuBg.setVisible(True)
                                widgets.titleRightInfo.setText("Buscar Usuario")
                                widgets.label_18.setText("Iniciando...")
                                widgets.btnRegistrarUsuario.setVisible(True)
                                widgets.btnReservaClase.setVisible(True)
                                widgets.btnBuscarUsuario.setVisible(True)
                                widgets.btnRegistrarEmpleado.setVisible(True)
                                widgets.btnNuevaSesion.setVisible(True)
                                widgets.btnNotificacion.setVisible(True)
                                widgets.btnAtras.setVisible(False)
                            elif tipo == "Nutriólogo":
                                widgets.stackedWidget.setCurrentWidget(widgets.lytNutriologo)
                                widgets.titleRightInfo.setText("Nutriólogo")
                                self.ui.leftMenuFrame.setEnabled(True)
                                widgets.leftMenuBg.setVisible(True)
                                widgets.btnAtras.setVisible(False)
                                widgets.btnRegistrarUsuario.setVisible(False)
                                widgets.btnReservaClase.setVisible(False)
                                widgets.btnBuscarUsuario.setVisible(False)
                                widgets.btnRegistrarEmpleado.setVisible(False)
                                widgets.btnNuevaSesion.setVisible(False)
                                widgets.btnNotificacion.setVisible(False)
                            elif tipo == "Psicólogo":
                                widgets.stackedWidget.setCurrentWidget(widgets.lytPsicologo)
                                widgets.titleRightInfo.setText("Psicólogo")
                                widgets.leftMenuBg.setVisible(False)
                            elif tipo == "Entrenador":
                                widgets.stackedWidget.setCurrentWidget(widgets.lytEntrenador)
                                widgets.titleRightInfo.setText("Entrenador")
                                widgets.leftMenuBg.setVisible(False)
                            auth.sign_in_with_email_and_password("resilience66.gym@gmail.com", "admin123")
                            self.tokenWR = auth.current_user['idToken']
                            print(self.tokenWR)
                        else:
                            widgets.label_18.setText("Contraseña incorrecta")
                            break
                    else:
                        widgets.label_18.setText("El tipo de usuario es incorrecto")
                        break
                else:
                    widgets.label_18.setText("Usuario incorrecto")
        else:
            widgets.label_18.setText("Escribe en los campos requeridos")

    def cerrarSesion(self):
        """ Regresa a la pantalla de iniciar Sesión
                Retorna:
                    La vista de la interfaz de inicio de sesión
        """
        widgets.stackedWidget.setCurrentWidget(widgets.lytLogin)
        widgets.leftMenuBg.setVisible(False)
        widgets.titleRightInfo.setText("Iniciar Sesión")
        widgets.txtUsuario.setText("")
        widgets.txtContrasea.setText("")
        widgets.label_6.setText("")
        widgets.label_14.setText("")
        widgets.label_18.setText("")

    def buscar(self, campotexto, label):
        """ Despliega los datos del cuestionario de nutrición previamente contestado en la aplicación móvil
                Parámetros :
                    campotexto: QWidget
                        objeto donde el usuario escribe el número de cliente
                    label: QWidget
                        objeto en donde se muestra un mensaje según sea el caso
                Excepciones:
                    No se encuentra al usuario si:
                        campotexto esta vacío
                        Si efectivamente el cliente existe en la base de datos
                Retorna:
                    Datos para llenar la tabla de información del cliente
                    Imagen pixmap de la dieta del cliente
        """
        opcPlan = widgets.cmbSubirDieta

        numCliente = campotexto.text()
        usuarios = db.child("Nutrición").get(self.tokenWR).val()
        b = False

        if campotexto.text() != "":
            n = 0
            m = 40
            o = 14
            p = 0
            q = 26
            l = 1
            for usuario, datos in usuarios.items():
                if numCliente == datos["Número de Cliente"]:
                    peso = db.child("Usuarios").child(usuario).child("Peso").get(self.tokenWR).val()
                    edad = db.child("Usuarios").child(usuario).child("Edad").get(self.tokenWR).val()
                    altura = db.child("Usuarios").child(usuario).child("Estatura").get(self.tokenWR).val()
                    b = False
                    for resp in range(1, 14):
                        widgets.tableWidget_3.setItem(n, 1, QtWidgets.QTableWidgetItem(datos[str(l)]))
                        n = n + 1
                        l = l + 1
                    for resp2 in range(15, 24):
                        widgets.tableWidget_3.setItem(o, 1, QtWidgets.QTableWidgetItem(datos[str(m)]))
                        m = m + 1
                        o = o + 1
                    for resp3 in range(1, 14):
                        widgets.tableWidget_5.setItem(p, 1, QtWidgets.QTableWidgetItem(datos[str(q)]))
                        p = p + 1
                        q = q + 1
                    listaP16 = datos[str(16)]
                    listaP18 = datos[str(18)]
                    listaP20 = datos[str(20)]
                    listaP24 = datos[str(24)]
                    listaP25 = datos[str(25)]
                    Resp16 = ", ".join(listaP16)
                    Resp18 = ", ".join(listaP18)
                    Resp20 = ", ".join(listaP20)
                    Resp24 = ", ".join(listaP24)
                    Resp25 = ", ".join(listaP25)
                    widgets.tableWidget_4.setItem(0, 1, QtWidgets.QTableWidgetItem(datos[str(14)]))
                    widgets.tableWidget_4.setItem(1, 1, QtWidgets.QTableWidgetItem(datos[str(15)]))
                    widgets.tableWidget_4.setItem(2, 1, QtWidgets.QTableWidgetItem(Resp16))
                    widgets.tableWidget_4.setItem(3, 1, QtWidgets.QTableWidgetItem(datos[str(17)]))
                    widgets.tableWidget_4.setItem(4, 1, QtWidgets.QTableWidgetItem(Resp18))
                    widgets.tableWidget_4.setItem(5, 1, QtWidgets.QTableWidgetItem(datos[str(19)]))
                    widgets.tableWidget_4.setItem(6, 1, QtWidgets.QTableWidgetItem(Resp20))
                    widgets.tableWidget_4.setItem(7, 1, QtWidgets.QTableWidgetItem(datos[str(21)]))
                    widgets.tableWidget_4.setItem(8, 1, QtWidgets.QTableWidgetItem(datos[str(22)]))
                    widgets.tableWidget_4.setItem(9, 1, QtWidgets.QTableWidgetItem(datos[str(23)]))
                    widgets.tableWidget_4.setItem(10, 1, QtWidgets.QTableWidgetItem(Resp24))
                    widgets.tableWidget_4.setItem(11, 1, QtWidgets.QTableWidgetItem(Resp25))
                    widgets.tableWidget_3.setItem(23, 1, QtWidgets.QTableWidgetItem(peso))
                    widgets.tableWidget_3.setItem(24, 1, QtWidgets.QTableWidgetItem(altura))
                    widgets.tableWidget_3.setItem(25, 1, QtWidgets.QTableWidgetItem(edad))
                    widgets.tableWidget_3.resizeRowsToContents()
                    widgets.tableWidget_4.resizeRowsToContents()
                    widgets.tableWidget_5.resizeRowsToContents()
                    label.setText("")
                    self.cmbAnadir("Planes", opcPlan)
                    widgets.cmbFechaImg.setEnabled(True)
                    widgets.cmbSubirDieta.setEnabled(True)
                    self.cmbAnadirFechaImg(usuario)
                    url = storage.child("Nutrición").child(usuario).child("Dieta").get_url(None)
                    try:
                        data = urllib.request.urlopen(url).read()
                        pixmap = QPixmap()
                        pixmap.loadFromData(data)
                        self.image4 = pixmap
                        widgets.btnImgNut4.setEnabled(True)
                        widgets.btnImgNut4.setStyleSheet("background-color: rgb(237, 28, 40);\n")
                    except:
                        widgets.btnImgNut4.setEnabled(False)
                        widgets.btnImgNut4.setStyleSheet("background-color: rgb(223, 40, 41);\n")
                        widgets.lblNClienteNut.setText("No hay dietas anteriores de este usuario")
            if b:
                label.setText("Usuario no encontrado")
        else:
            label.setText("Escribe el número de cliente")

    def nuevaSesion(self):
        """ Registra una o varias sesiones en la base de datos
            Excepciones:
                La sesión no se registra si:
                    Los campos están vacíos
                    El formato de la fecha es dd-mm-aaaa
                    El formato de la hora es hh:mm
                    La fecha y hora deben ser anteriores a la fecha de hoy
            Retorna:
                mensaje de sesión subida a la base de datos
        """
        fecha = widgets.txtFechaAgregar.text()
        hora = widgets.txtHoraAgregar
        nombre = widgets.cmbNombreSesion
        nivel = widgets.cmbselecNivel
        intensidad = widgets.cmbIntensidad
        campoFecha = widgets.txtFechaAgregar
        etiquetaFecha = widgets.lblFechaAgregar
        b1 = self.validarCampos(campoFecha, etiquetaFecha)
        b5 = self.validarCombo(nivel)
        b6 = self.validarCombo(intensidad)
        b3 = self.validarCombo(nombre)
        b2 = self.validarCombo(hora)
        if b1 and b3 and b2 and b5 and b6:
            if len(fecha) != 10 or fecha[2] != "-" or fecha[5] != "-":
                widgets.lblFechaAgregar.setText("Formato de fecha invalido")
            else:
                if len(hora.currentText()) != 5 or hora.currentText()[2] != ":":
                    widgets.lblHoraAgregar.setText("Formato de hora invalido")
                else:
                    fechaCompleta = fecha + " " + hora.currentText()
                    try:
                        fechaHoy = time.time()
                        fechaDate = datetime.strptime(fechaCompleta, '%d-%m-%Y %H:%M')
                        if fechaDate.timestamp() > fechaHoy:
                            data = {
                                "Horas": self.listaHoras,
                                "Intensidad": intensidad.currentText(),
                                "Nombre": nombre.currentText(),
                            }
                            widgets.lblAgregar.setText("Sesión guardada con éxito")

                            baseUrl = db.child("Listas").child("Niveles").child(nivel.currentText()).get(self.tokenWR
                                                                                                         ).val()
                            data.setdefault("URL", baseUrl)
                            db.child("Fechas").child(nivel.currentText()).child(fecha).push(data, self.tokenWR)
                            idBaseO = db.child("Fechas").child(nivel.currentText()).child(fecha).get(self.tokenWR).val()

                            for id34 in idBaseO.keys():
                                print(id34)
                            self.listaIdGeneral.append(id34)
                            db.child("Fechas").child("PRUEBA").child(fecha).child(id34).set(data, self.tokenWR)

                            widgets.tableWidget_6.insertRow(widgets.tableWidget_6.rowCount())
                            rowCount = widgets.tableWidget_6.rowCount()
                            horas = ", ".join(self.listaHoras)
                            item = QTableWidgetItem(nombre.currentText())
                            item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            item1 = QTableWidgetItem(fecha)
                            item1.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            item2 = QTableWidgetItem(intensidad.currentText())
                            item2.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            item3 = QTableWidgetItem(nivel.currentText())
                            item3.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            item5 = QTableWidgetItem(horas)
                            item5.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                            for j in range(rowCount):
                                if widgets.tableWidget_6.item(j, 0) is None:
                                    widgets.tableWidget_6.setItem(j, 0, item)
                                    widgets.tableWidget_6.setItem(j, 1, item1)
                                    widgets.tableWidget_6.setItem(j, 2, item2)
                                    widgets.tableWidget_6.setItem(j, 3, item3)
                                    widgets.tableWidget_6.setItem(j, 4, item5)
                        else:
                            widgets.lblAgregar.setText("La fecha expiro")
                    except ValueError:
                        widgets.lblAgregar.setText("Fecha u hora invalidas")
        else:
            widgets.lblAgregar.setText("Por favor escribe los campos requeridos")

    def habilitar2(self):
        """ Habilita el objeto ComboBox donde se selecciona a quien se le va a enviar la notificación al móvil """
        texto = widgets.ntCmbRemitente.currentText()
        if texto == "Una persona":
            widgets.ntTxtNumCliente.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                                                  "color: rgb(0, 0, 0 );\n")
            widgets.ntTxtNumCliente.setEnabled(True)
        else:
            widgets.ntTxtNumCliente.setStyleSheet("background-color: rgb(210, 210, 210);\n"
                                                  "color: rgb(100, 100, 100 );\n")
            widgets.ntTxtNumCliente.setEnabled(False)
            widgets.ntTxtNumCliente.setText("")

    def habilitarBoton(self):
        """ Habilita el botón donde el usuario al pulsarlo puede elegir que archivo de imagen subir de una dieta """
        OPlan = widgets.cmbSubirDieta.currentText()
        BSubirPlan = widgets.lblAbrirImg
        if OPlan != "":
            BSubirPlan.setEnabled(True)
            BSubirPlan.setStyleSheet("background-color: rgb(237, 28, 40);\n"
                                     "image: url(:/icons/images/icons/cil-folder-open.png);")
        else:
            widgets.label_17.setText("Selecciona un plan")

    def nombreClase(self):
        """ Añade los nombres de las sesiones a un objeto comboBox """
        widgets.cmbNombreSesion.clear()
        Nombres = db.child("Sesiones").child("Nombre").get(self.tokenWR).val()
        for num in Nombres:
            widgets.cmbNombreSesion.addItem(num)

    def cmbAnadir(self, nombreLista, combo):
        """ Añade cualquiera de las listas de la base de datos a un combo
                Parámetros:
                    nombreLista : string
                        nombre de la lista alojada en base de datos
                    combo : QComboBox
                        objeto donde se muestra la lista
        """
        combo.clear()
        combo.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                            "color: rgb(0, 0, 0 );\n"
                            "font: 10pt Montserrat;")
        Nombres = db.child("Listas").child(nombreLista).get(self.tokenWR).val()
        for num in Nombres:
            combo.addItem(num)

    def cmbAnadirFechaImg(self, id):
        """ Añade al combo las fechas de actualización de las fotos para el nutriólogo
                Parámetros : id
                    número único de un usuario que se genera al registrar un cliente
        """
        combo = widgets.cmbFechaImg
        self.id = id
        combo.clear()
        combo.setStyleSheet("background-color: rgb(221, 221, 221);\n"
                            "color: rgb(0, 0, 0 );\n")
        Nombres = db.child("Usuarios").child(self.id).child("Nutriólogo").child("Fechas").get(self.tokenWR).val()
        for NFecha, fecha in Nombres.items():
            combo.addItem(fecha)

    def es_correo_valido(self, correo):
        """ Comprueba que el correo tenga el formato: correo@mail.com
                Parámetros :
                    correo : string
                        texto escrito por el usuario en el campo correo de registro
                Retorna:
                    tipo : booleano
                        devuelve si efectivamente es un correo
         """
        expresion_regular = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"
        # re : librería regular expression
        return re.match(expresion_regular, correo) is not None

    def cmbLista(self):
        """ Agrega una lista con datos estáticos a un objeto combobox """
        widgets.cmbTipoSexo.clear()
        tipoS = ["Hombre", "Mujer", "Prefiero no decir", "Otro"]
        widgets.cmbTipoSexo.addItems(tipoS)

        widgets.cmbTipoEmpleado.clear()
        widgets.cmbTipoDeUsuario.clear()
        tipoE = ["Entrenador", "Nutriólogo", "Recepcionista"]
        widgets.cmbTipoEmpleado.addItems(tipoE)
        widgets.cmbTipoDeUsuario.addItems(tipoE)

    def cmbTopics(self):
        """ Añade la  lista Topics a un objeto combobox 'ntCmbRemitente' """
        opcion = widgets.ntCmbRemitente
        self.cmbAnadir("Topics", opcion)
        widgets.ntCmbRemitente.addItem("Una persona")

    def validarCombo(self, combo):
        """ Comprueba si se selecciona una opción en cualquier objeto comboBox
                Parámetros :
                    combo : QComboBox
                        objeto combo que se va a comprobar
                Retorna : booleano
        """
        textoCombo = combo.currentText()
        if textoCombo == "":
            combo.setStyleSheet("border: 1px solid red;")
            return False
        else:
            return True

    def enviarNot(self):
        """ Enviá una notificación al móvil dependiendo de la opción que se elige
                Excepciones:
                    Si los campos están vacíos
                    Si el usuario no existe en la base de datos
                Retorna:
                    mensaje en formato de notificación móvil
        """
        opcion = widgets.ntCmbRemitente
        titulo = widgets.ntTxtTitulo
        cuerpo = widgets.ntTxtTexto
        usuarios = db.child("Usuarios").get(self.tokenWR).val()
        numCliente = widgets.ntTxtNumCliente.text()

        etiquetaTitulo = widgets.ntLblTitulo
        etiquetaCuerpo = widgets.ntLblTexto

        b1 = self.validarCampos(titulo, etiquetaTitulo)
        b2 = self.validarCampos(cuerpo, etiquetaCuerpo)
        b3 = self.validarCombo(opcion)

        if b1 and b2 and b3:
            if opcion.currentText() == "Una persona":
                band = False
                for usuario, datos in usuarios.items():
                    if numCliente == datos["Número de Cliente"]:
                        token = [datos["Token"]]
                        enviado1 = fcm.sendPush(titulo.text(), cuerpo.text(), token)
                        # fcm.sendPush(titulo.text(), cuerpo.text(), token)
                        widgets.ntLblUrl.setText(str(enviado1))
                        # print(datos["Numero de Cliente"])
                        # print(token)
                        band = True
                        break
                if not band:
                    widgets.ntLblUrl.setText("Usuario no encontrado")
            else:
                nomGrupo = db.child("Listas").child("Topics").child(opcion.currentText()).get().val()
                enviado = fcm.topics(nomGrupo, titulo.text(), cuerpo.text())
                # fcm.topics(nomGrupo, titulo.text(), cuerpo.text())
                widgets.ntLblBtnEnviar.setText(str(enviado))
        else:
            widgets.ntLblCmbRemitente.setText("Campos obligatorios")

    def nuevaHora(self):
        """ Agrega horas a una lista global y a un objeto combo
                Excepciones:
                    El campo de hora esta vacío
                    Si el formato de la hora no coincide con hh:mm
                    La hora escrita no es mayor a la hora actual
                Retorna:
                    lista de las horas que añadió el usuario
        """
        hora = widgets.txtHoraAgregar.currentText()
        fecha = widgets.txtFechaAgregar.text()
        if hora != "":
            try:
                if len(hora) == 5 and hora[2] == ":":
                    fechaCompleta = fecha + " " + hora
                    fechaHoy = time.time()
                    fechaDate = datetime.strptime(fechaCompleta, '%d-%m-%Y %H:%M')
                    if fechaDate.timestamp() > fechaHoy:
                        self.listaHoras.append(hora)
                        widgets.txtHoraAgregar.clear()
                        widgets.txtHoraAgregar.addItems(self.listaHoras)
                        widgets.txtHoraAgregar.setCurrentText("")
                        widgets.txtHoraAgregar.showPopup()
                    else:
                        widgets.lblNuevaAgregar.setText("La hora expiro")
                else:
                    widgets.lblHoraAgregar.setText("Formato de hora invalido")
            except ValueError:
                widgets.lblHoraAgregar.setText("Hora incorrecta")
        else:
            widgets.lblHoraAgregar.setText("Introduzca una hora")

    def eliminarFila(self):
        """ Elimina la fila de la tabla donde se registran las clases subidas a la base de datos,
            también elimina la clase de la base de datos
                Excepciones:
                    Si la columna 'Nivel' del objeto tabla esta vacía
        """
        if widgets.tableWidget_6.rowCount() > 0:
            rows = widgets.tableWidget_6.selectionModel().selectedRows()
            index = []
            for i in rows:
                index.append(i.row())
            index.sort(reverse=True)
            for i in index:
                fechaTabla = widgets.tableWidget_6.item(i, 1).text()
                nivelTabla = widgets.tableWidget_6.item(i, 3).text()
                if nivelTabla != "":
                    db.child("Fechas").child(nivelTabla).child(fechaTabla).child(self.listaIdGeneral[i]).remove(
                        self.tokenWR)
                    db.child("Fechas").child("PRUEBA").child(fechaTabla).child(self.listaIdGeneral[i]).remove(
                        self.tokenWR)
                    widgets.tableWidget_6.removeRow(i)
                    self.listaIdGeneral.pop(i)
                else:
                    widgets.lblAgregar.setText("No has agregado sesiones")

    def eliminarClase(self):
        """ Elimina un nombre de sesión en el combo 'Nombre de sesión' en la sección de 'Nueva Sesión'
                Excepciones:
                    Si el indice del objeto combobox 'cmbNombreSesion' es -1
                    Si el objeto tabla no tiene filas
        """
        nombreClase = widgets.cmbNombreSesion.currentText()
        index = widgets.cmbNombreSesion.currentIndex()
        if index != -1:
            if widgets.cmbNombreSesion.count() > 0:
                index = widgets.cmbNombreSesion.currentIndex()
                widgets.cmbNombreSesion.removeItem(index)
                db.child("Sesiones").child("Nombre").child(nombreClase).remove(self.tokenWR)
        else:
            widgets.label_11.setText("Seleccione una sesión")

    def eliminarHora(self):
        """ Elimina un elemento del combo con la etiqueta 'Hora(hh:mm)' en la sección 'Nueva Sesión'
                Excepciones:
                    El indice del objeto combobox 'txtHoraAgregar' es igual a -1
                    o lo que es lo mismo que no este seleccionado nada
        """
        hora = widgets.txtHoraAgregar.currentText()
        index = widgets.txtHoraAgregar.currentIndex()
        if index != -1:
            index = widgets.txtHoraAgregar.currentIndex()
            widgets.txtHoraAgregar.removeItem(index)
            self.listaHoras.remove(hora)
        else:
            widgets.lblHoraAgregar.setText("Introduzca una hora")

    def NuevaClase(self):
        """ Agrega un elemento (Nombre de sesión) al combo ´Nombre de sesión´ en la sección 'Nueva Sesión'
                Excepciones:
                    El campo ´Nuevo nombre de sesión´ esta vacío
                Retorna:
                    una lista con los nombres de las sesiones
        """
        nombreNuevo = widgets.txtNuevaAgregar.text()
        etiquetaNombreNuevo = widgets.lblNuevaAgregar
        if nombreNuevo != "":
            db.child("Sesiones").child("Nombre").child(nombreNuevo).set("1", self.tokenWR)
            etiquetaNombreNuevo.setText("")
        else:
            etiquetaNombreNuevo.setText("Introduzca un nombre de sesión")
        widgets.cmbNombreSesion.clear()
        Nombres = db.child("Sesiones").child("Nombre").get(self.tokenWR).val()
        for num in Nombres:
            widgets.cmbNombreSesion.addItem(num)

    def get_image_file(self):
        """ Abre la interfaz para seleccionar la imagen a subir en la base de datos
                Excepciones:
                    Si el objeto label esta vacía, esto pasa si no se selecciono un archivo
        """
        ruta = widgets.lblFileName
        BSubirP = widgets.btnSubirDieta
        self.file_name, _ = QFileDialog.getOpenFileName(self, "Seleccione una imagen", r"C:\\Users",
                                                        "Image files (*.jpg *jpeg *.gif *.png)")
        widgets.lblFileName.setText(self.file_name)
        if ruta.text() != "":
            BSubirP.setEnabled(True)
            BSubirP.setStyleSheet("background-color: rgb(237, 28, 40);\n")
        else:
            ruta.setText("Seleccione una imagen primero")

    def imgDietaPerso(self):
        """ Sube la imagen seleccionada anteriormente a la base de datos """
        OpcionPlan = widgets.cmbSubirDieta.currentText()
        desBase = db.child("Listas").child("Planes").child(OpcionPlan).get(self.tokenWR).val()

        storage.child("Nutrición").child(self.id + "/Plan").put(self.file_name)
        db.child("Usuarios").child(self.id).child("Nutriólogo").child("Plan").set(OpcionPlan, self.tokenWR)
        db.child("Usuarios").child(self.id).child("Nutriólogo").child("Descripción").set(desBase, self.tokenWR)
        QMessageBox.information(self, "Listo", "La imagen se guardo exitosamente", QMessageBox.Ok)

    def renovar_checando_tipo(self, tipo, vigencia, fechaHoy, estatus, datos, precioId, precio, expiracion, usuario, nutriologo, clases, exclusivo, idProducto, nombre):
        if tipo == "recurring":
            if (vigencia < fechaHoy or estatus != "active") and estatus != "past_due":
                customer = datos["Stripe"]["StripeID"]
                datosS = {'customer': customer, 'priceId': precioId, 'tipo': tipo}
                response = requests.get(
                    'https://us-central1-resilience66-abd3e.cloudfunctions.net/pythonS',
                    params=datosS
                )
                if response.status_code == 200:
                    nUsuario = widgets.txtUsuario.text()
                    textoJson = response.json()
                    print(textoJson)
                    data = {
                        "Responsable": nUsuario,
                        "Número de Cliente": datos["Número de Cliente"],
                        "PaymentIntent": textoJson["PaymentIntent"],
                        "Factura": textoJson["Invoice"],
                        "Fecha": str(datetime.now()),
                        "Precio": precio
                    }
                    db.child("Suscripciones Stripe").child(textoJson["IDSuscripcion"]).set(data, self.tokenWR)
                    print(textoJson['IDSuscripcion'])
                    widgets.lblBuscar.setText("Suscripción actualizada exitosamente")
                    widgets.btnRenovar.setEnabled(True)
                else:
                    widgets.btnRenovar.setEnabled(True)
                    widgets.lblBuscar.setText(response.text, response.status_code)
            elif estatus == "" or estatus is None:
                widgets.lblBuscar.setText("Error obteniendo los datos de su cuenta")
            else:
                widgets.lblBuscar.setText("Ya cuenta con una suscripción o paquete")
        else:
            ahora = datetime.now()
            global epochVigencia2
            if float(expiracion) < 1:
                mas2Semanas = ahora + relativedelta(weeks=2)
                epochVigencia2 = mas2Semanas.timestamp()
            else:
                masNMeses = ahora + relativedelta(months=int(expiracion))
                epochVigencia2 = masNMeses.timestamp()
            if (vigencia < fechaHoy or estatus != "active") and estatus != "past_due":
                vigenciaE = int(epochVigencia2)
                db.child("Usuarios").child(usuario).child("Clases").set(clases,self.tokenWR)
                db.child("Usuarios").child(usuario).child("Exclusivo").set(exclusivo,self.tokenWR)
                db.child("Usuarios").child(usuario).child("Nutriólogo").child("Acceso").set(nutriologo, self.tokenWR)
                db.child("Usuarios").child(usuario).child("Stripe").child("Suscripción").child("Producto").set(
                                                                                            idProducto, self.tokenWR)
                db.child("Usuarios").child(usuario).child("Stripe").child("Suscripción").child("NombreM").set(
                                                                                            nombre, self.tokenWR)
                db.child("Usuarios").child(usuario).child("Stripe").child("Suscripción").child("Tipo").set(
                                                                                            tipo, self.tokenWR)
                db.child("Usuarios").child(usuario).child("Stripe").child("Suscripción").child("StatusSus").set(
                                                                                            "active", self.tokenWR)
                db.child("Usuarios").child(usuario).child("Stripe").child("Suscripción").child("Vigencia").set(
                                                                                            vigenciaE, self.tokenWR)
                db.child("Usuarios").child(usuario).child("Stripe").child("Suscripción").child("Precio").set(
                                                                                            precioId, self.tokenWR)
                db.child("Usuarios").child(usuario).child("Automático").set("No",self.tokenWR)

                datosConsumible = {
                    "Factura": "paid",
                    "Fecha": str(datetime.now()),
                    "Número de Cliente": datos["Número de Cliente"],
                    "PaymentIntent": "Consumible",
                    "Responsable": widgets.txtUsuario.text(),
                    "Precio": precio
                }
                db.child("Suscripciones Stripe").push(datosConsumible, self.tokenWR)

                widgets.lblBuscar.setText("Suscripción actualizada exitosamente")
                widgets.btnRenovar.setEnabled(True)
            elif estatus == "" or estatus is None:
                widgets.lblBuscar.setText("Error obteniendo los datos de su cuenta")
            else:
                widgets.lblBuscar.setText("Ya cuenta con una suscripción o paquete")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("R66.ico"))
    window = MainWindow()
    sys.exit(app.exec_())
