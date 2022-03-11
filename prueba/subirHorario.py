import pyrebase
import json
import time

from datetime import timedelta
from serial.win32 import LPSECURITY_ATTRIBUTES
from collections import defaultdict
from dateutil.relativedelta import relativedelta
from datetime import datetime

firebaseConfig = {
    "apiKey": "AIzaSyChD7i5tuQgRClNL24yJ1rvo8ot17N2BGo",
    "authDomain": "resilience66-abd3e.firebaseapp.com",
    "databaseURL": "https://resilience66-abd3e-default-rtdb.firebaseio.com",
    "projectId": "resilience66-abd3e",
    "storageBucket": "resilience66-abd3e.appspot.com",
    "messagingSenderId": "975779634876",
    "appId": "1:975779634876:web:64ade2008a37e17a35bab9",
    "measurementId": "G-1EFQLX0JEX"}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


lista_usuarios = {}

"""for idClase, vals in baseProducto1.items():
    precio = (vals["Precio"])[:-2]
    data_usuario = {idClase: {"Nombre": vals["Nombre"],
                              "Precio": precio,
                              "Activo": vals["Activo"],
                              "Clases": vals["Clases"],
                              "Exclusivo": vals["Exclusivo"],
                              "Expiración": vals["Expiración"],
                              "Nutriólogo": vals["Nutriólogo"],
                              "PrecioID": vals["PrecioID"],
                              "Tipo": vals["Tipo"]
                              }}
    lista_usuarios.update(data_usuario)
print(lista_usuarios)

with open("base.json", "w") as crear_archivo:
    json.dump(lista_usuarios, crear_archivo)
    print("Archivo exportado")

with open("base.json", "r") as creado_archivo:
    baseDatos = json.load(creado_archivo)
    print("Archivo obtenido")
"""

precio100 = "10200"

ahora = datetime.now()
dentro_de_2_semanas = ahora + relativedelta(months=2)
f_epoch = dentro_de_2_semanas.timestamp()
print(ahora)

#print(format(int(precio100), ',d'))

#print(str(datetime.now()))

"""info = defaultdict(list)

for key in baseProducto1.keys():
    info['carId'].append(key['metadata']['carId'])
    info['displayName'].append(key['metadata']['displayName'])"""
# with open("producto1.json", "r") as archivo:
#   baseP = json.load(archivo)
#  print(baseP)
"""cadena = "5000"
print(".".join((cadena, "00")))"""

string = "5000"
characters = "0"

nombres = [
    "Full Body",
    "Hiit and Core",
    "Emom",
    "Athlete 66",
    "Cardio",
    "Only Bar5",
    "Animal Move",
    "Core and ABS",
    "High Movility",
    "Power Lowbody",
    "Upper and ABS",
    "Fullbody Hiit",
]

niveles = [
    "66 + BACK TO BASICS",
    "66 IN PROGRESS",
    "ELITE PRO 66"
]

horas = [

]

fulBody = "Full Body"
hiitC = "Hiit and Core"
Emon = "Emom"
ath66 = "Athlete 66"
cardio = "Cardio"
onlyB = "Only Bar5"
animalM = "Animal Move"
candAbs = "Core and ABS"
highM = "High Movility"
powerLow = "Power Lowbody"
uandAbs = "Upper and ABS"
fBodyHiit = "Fullbody Hiit"

nombre = Emon
fecha = "28-09-2021"
cupo = "30"
hora = "21:00"
nivel = "Elite Pro 66"
url = "https://us04web.zoom.us/j/79628772729?pwd=SHZJdkZaY3J2aUhWUUxVK3VEaEgrdz09"

data = {fBodyHiit: "1", uandAbs: "1", powerLow: "1", highM: "1", candAbs: "1", animalM: "1", onlyB: "1", cardio: "1",
        ath66: "1", Emon: "1", hiitC: "1", fulBody: "1"}

# db.child("Fechas").child(fecha).child("Online").push(fBodyHiit)
# db.child("Fechas").child(fecha).child("Online").child(fBodyHiit).child("6:15").set("40")
# db.child("Fechas").child(fecha).child("Online").child(fBodyHiit).child("18:30").set("40")
# db.child("Fechas").child(fecha).child("Online").child(uandAbs).child("18:30").set("40")
# db.child("Fechas").child(fecha).child("Online").child(uandAbs).child("8:30").set("40")

data2 = {
    "Nombre": nombres[2].upper(),
    "Horas": ["7:00", "8:00"],
    "Intensidad": "Media",
    "URL": url
}
# db.child("Fechas").child(niveles[0]).child(fecha).push(data2)

"""texto = "hola como - estas andres"
textoSin = texto.split(" - ")
print(textoSin[0])"""
"""lista = []
db.child("Sesiones").child("Nombre").set(data)"""
"""Nombres = db.child("Sesiones").child("Nombre").get().val()
#print(Nombres)
for num in Nombres:
	lista.append(num)
print(num)"""
# widgets.cmbOpcionRenovar.addItem(nombre["Nombre"])
# db.child("Sesiones").child("Nombre").set(data)

# db.child("Fechas").child(fecha).push(cardio)
# db.child("Fechas").child(fecha).child("Presencial").child(cardio).child("7:30").set("40")
# db.child("Fechas").child(fecha).child("Presencial").child(cardio).child("19:45").set("40")
# db.child("Fechas").child(fecha).push(ath66)
# db.child("Fechas").child(fecha).child("Hibrida").child(ath66).child("8:45").set("30")
# db.child("Fechas").child(fecha).child("Hibrida").child(ath66).child("21:00").set("30")
'''fechaBase = db.child("Fechas").child("66 IN PROGRESS").get().val()
listaTFecha = []
listaId = []
diccTFecha = {}
n = 0
for TFechas, TId in fechaBase.items():
	listaTFecha.append(TFechas)
	for id, datos in TId.items():
		listaId.append(id)
		d = datos["Horas"]
		db.child("A").child("Mis Clases").child(id).child("Nombre").set(datos["Nombre"])
		db.child("A").child("Mis Clases").child(id).child("Intensidad").set(datos["Intensidad"])
		db.child("A").child("Mis Clases").child(id).child("URL").set(datos["URL"])
		db.child("A").child("Mis Clases").child(id).child("Hora").set(d[n])
		db.child("A").child("Mis Clases").child(id).child("Fecha").set(listaTFecha[n])
		n = n + 1
		print(TId)
print(listaId)
print(listaTFecha)'''

"""fechaCompleta = "9:00"
try:
	fechaDate = datetime.strptime(fechaCompleta,'%H:%M')
	print(fechaDate)
except ValueError:
	print(ValueError)"""

"""userBase = db.child("Nutrición").get().val()
listaTFecha = []
listaId = []
diccTFecha = {}
n = 0
for id, datos in userBase.items():
	listaTFecha.append(id)
	if "6256" == datos["Número de Cliente"]:
		print("usuario encontrado")
		break
print(listaTFecha)
print(datos)"""

"""listaP = ["uno", "dos"] + ["2"]
print(listaP)"""

dataUser = {
    # "Cupo":str(cupo),
    "Horas": "10:00",
    # "URL":url,
    "Intensidad": "Alta"
}

# db.child("Fechas").child("Presencial").child("10-10-2021").push(dataUser)
"""idBase = db.child("Fechas").child("Presencial").child("10-10-2021").get().val()
print(idBase)
listaIds = []
for id34, datos in idBase.items():
	print(id34)
	listaIds.append(id34)
print(listaIds)"""
# db.child("Fechas").child("66 + BACK TO BASICS").child("10-10-2021").child(id34).set(dataUser)
# db.child("Fechas").child("Presencial").child("10-10-2021").child(listaIds[0]).remove()
# print(id)

"""my_foods = ['pizza', 'falafel', 'carrot cake']
lista = ["arroz"]
friend_foods = my_foods[:] + lista
print("My favorite foods are:")
print(my_foods)
print("\nMy friend's favorite foods are:")
print(friend_foods)"""

"""fechaBase = db.child("Fechas").child("66 + BACK TO BASICS").get().val()
#print(fechaBase)
listaTFecha = []
listaId = []
listaHoras = []
listaTId = {}
n = 0
for TFechas, TId in fechaBase.items():
	#listaTFecha.append(TFechas)
	#listaTId.update(TId)
	#print(TId)
	#print(listaTFecha[n])
	#widgets.tableWidget_2.setItem(n, 1, QtWidgets.QTableWidgetItem(listaTFecha[n]))
#print(listaTId)
#print(listaTFecha)
	b = 0
	#widgets.tableWidget_2.setRowCount(len(TId))
	#for id, datosT in listaTId.items():
	for id, datosT in TId.items():
		listaId.append(id)
		d = datosT["Horas"]
		listaHoras.append(d)
		horas = ", ".join(listaHoras[b])
		print(horas)
		#m = len(d)
		#print(listaHoras)
		#print(listaTFecha[b])
		print(datosT["Nombre"])
		print(TFechas)
		b = b + 1
	#widgets.tableWidget_2.setItem(b, 0, QtWidgets.QTableWidgetItem(datosT["Nombre"]))
	#widgets.tableWidget_2.setItem(b, 1, QtWidgets.QTableWidgetItem(listaTFecha[b]))
	#widgets.tableWidget_2.setItem(b, 2, QtWidgets.QTableWidgetItem(d[m]))

#print(listaId)"""

"""fechaBase = db.child("Fechas").child(nivel).get().val()
					if fechaBase != None:
						listaTFecha = []
						listaId = []
						widgets.tableWidget_2.clearContents()
						n = 0
						widgets.tableWidget_2.setRowCount(len(fechaBase))
						for TFechas, TId in fechaBase.items():
							listaTFecha.append(TFechas)
							widgets.tableWidget_2.setItem(n, 1, QtWidgets.QTableWidgetItem(listaTFecha[n]))
							print(listaTFecha)
							n = n + 1
						b = 0
						widgets.tableWidget_2.setRowCount(len(TId))
						for id, datosT in TId.items():
							listaId.append(id)
							#print(listaId)
							d = datosT["Horas"]
							m = len(d)
							print(d)
							widgets.tableWidget_2.setItem(b, 0, QtWidgets.QTableWidgetItem(datosT["Nombre"]))
							#widgets.tableWidget_2.setItem(b, 1, QtWidgets.QTableWidgetItem(listaTFecha[b]))
							#widgets.tableWidget_2.setItem(b, 2, QtWidgets.QTableWidgetItem(d[m]))
							b = b + 1
						print(listaTFecha)
						print(listaId)"""

"""datosProducto = {
    "Nombre": "Suscripción anual + Nutrición",
    "Precio": "10200",
    "beneficio1": "Clases automaticas",
    "beneficio2": "Seguimiento personalizado",
    "beneficio3": "Dieta personalizada"
}

db.child("Products prueba").child("Online").child("150").set(datosProducto)"""
