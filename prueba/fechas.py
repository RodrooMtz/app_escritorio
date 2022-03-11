import datetime
import time
from dateutil.relativedelta import relativedelta
from datetime import datetime
from PyQt5.QtMultimedia import QCamera, QCameraInfo, QCameraImageCapture

"""mesActual = "01-03-2021"
mesSiguiente = "01-04-2021"

fecha1 = time.strptime(mesActual, '%d-%m-%Y')
fecha2 = time.strptime(mesSiguiente, '%d-%m-%Y')

unMes = fecha1 + fecha2
print(unMes)"""
"""HoraFecha = datetime.now()
vigencia = ""
membresia = input("introduce la opcion: ")
if membresia != "Ninguna":
    if membresia == "Anual":
        vigencia = datetime.strftime((HoraFecha + relativedelta(years=1)), '%d-%m-%Y')
    if membresia == "Mensual":
        vigencia = datetime.strftime((HoraFecha + relativedelta(months=1)), '%d-%m-%Y')
    if membresia == "Diaria":
        vigencia = datetime.strftime((HoraFecha + relativedelta(days=1)), '%d-%m-%Y')
    print(vigencia)
else:
    print("Ninguna")"""
"""print(HoraFecha)
haceUnAño = HoraFecha + relativedelta(months=1)
# haceUnAño = HoraFecha + datetime.timedelta(days=365/12)
print(str(haceUnAño))"""

"""fecha = "2-3-2021"
fechaC = datetime.strptime(fecha, '%d-%m-%Y')
print(fechaC)
fechaS = datetime.strftime(fechaC, '%d-%m-%Y')
print(fechaS)"""
"""membresia = "Mensual"  # widgets.cmbTipoMembresia.currentText()
HoraFecha = datetime.now()
vigencia = ""
if membresia != "Ninguna":
	if membresia == "Anual":
		vigencia = datetime.strftime((HoraFecha + relativedelta(years=1)), '%d-%m-%Y')

	if membresia == "Mensual":
		vigencia = datetime.strftime((HoraFecha + relativedelta(months=2)), '%d-%m-%Y')
		print(vigencia)
	if membresia == "Diaria":
		vigencia = datetime.strftime((HoraFecha + relativedelta(days=1)), '%d-%m-%Y')
else:
	vigencia = "Ninguna"""

"""fecha = datetime.today().strftime('%Y-%m-%d')

fechaF = datetime.strptime(fecha, "%Y-%m-%d")

fechaEpoch = fechaF.timestamp()

print(fechaEpoch)
"""

"""hora = "03:00"
fecha = "17-08-2021"

horaFecha = fecha + " " + hora
fechaf = datetime.strptime(horaFecha, "%d-%m-%Y %H:%M")
fechaEpoch = fechaf.timestamp()
vigencia = 1631584128

hoy = time.time()

print(fechaEpoch)

if vigencia < fechaEpoch < hoy:
    print("hola")
else:
    print("adios")"""

ahora = datetime.now()
expiracion = 1
if float(expiracion) < 1:
    mas2Semanas = ahora + relativedelta(weeks=2)
    epochVigencia1 = mas2Semanas.timestamp()
else:
    masNMeses = ahora + relativedelta(months=int(expiracion))
    epochVigencia1 = masNMeses.timestamp()
    print(int(epochVigencia1))
    vigenciaE = str(epochVigencia1)[:-7]
    print(vigenciaE)

"""datetime.now()
print(datetime.now().strftime("%d-%m-%Y"))"""
