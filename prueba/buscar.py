from datetime import datetime

import pyrebase
import time

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
numCliente = "1241G"
lista2 = []

storage = firebase.storage()
storage.child("logo.png").put("Fondo-Compu.png")
usuarios = db.child("Usuarios").get().val()
empleados = db.child("Empleados").get().val()

nombre = "rodrigo martinez"
tipo = "Recepcionista"
contrasena = "1234"

for idEmpleado, datos in empleados.items():
	print(idEmpleado)
	print(datos["Nombre"])
	if nombre == datos["Nombre"] and tipo == datos["Tipo"] and contrasena == datos["Contrasena"]:
		print("usuario correcto")
		break
	else:
		print("usuario incorrecto")
		break
		


"""for usuario, datos in usuarios.items():
	print(usuarios["Edad"][0])"""

"""clases = db.child("Fechas").child("19-08-2021").get().val()
for tipo, datos in clases.items():
	if tipo == "Presencial":
		print(datos)
		print(tipo)	"""
"""data = {"Numero de Cliente":"10", "Responsable":"Rodrigo", "PaymentIntent":"pi_4567", "Invoice":"paid"}
db.child("Suscripciones").push(data)"""
#db.child("Suscripciones").child("Numero de Cliente").set("Numero de Cliente")
#db.child("Suscripciones").child("Responsable").set("response")
#db.child("Suscripciones").child("Responsable").set("response.text")		

"""fechaBase = db.child("Fechas").child("15-08-2021").child("hibrida").get().val()
for clases in fechaBase.keys():
	lista.append(clases)
print(lista)"""
"""fechaBase = db.child("Usuarios").child("7j6whvMDwrbavcWs3l9BCdOvmqu1").child("Mis Clases").get().val()
for clases, fechas in fechaBase.items():
	lista2.append(fechas["Fecha"])"""


"""def fechaMayor(lista2):
	for indice in range(1, len(lista2)):

		valorActual = lista2[indice]
		posicion = indice

		while posicion > 0 and lista2[posicion - 1] < valorActual:
			lista2[posicion] = lista2[posicion - 1]
			posicion = posicion - 1
		lista2[posicion] = valorActual
	fechaF = datetime.strptime(lista2[0], "%d-%m-%Y")
	fechaEpoch = fechaF.timestamp()
	return fechaEpoch



print(fechaMayor(lista2))
fechaHoy = time.time()
print(str(fechaHoy))"""

"""fechaHoy = time.time()
if fechaHoy <= float(str(fechaMayor)):
	print("True")
else:
	print("false")"""

"""usuarios = db.child("Usuarios").get().val()
for usuario, datos in usuarios.items():

	if numCliente == datos["Numero de Cliente"]:
		# print("usuario encontrado")
		da = datos["Stripe"]
		dat = da["Suscripción"]
		print(dat["StatusSus"])
		break
	else:
		print("usuario no encontrado")"""

