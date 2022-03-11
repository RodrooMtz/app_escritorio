import pyrebase
import urllib.request
from PyQt5.QtGui import QPixmap, QIcon
import cv2
import imutils
import tempfile, os, sys
from PIL import Image, ExifTags
from PIL.ExifTags import TAGS
import piexif

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
storage = firebase.storage()

"""image = Image.open("Foto2.jpg")
girada = image.rotate(0)
resize = girada.resize((800, 900))

w = image.width
print(w)
h = image.height
print(h)"""


"""rotate = image.rotate(180)
print(int(rotate))"""

"""for orientation in ExifTags.TAGS.keys():
	if ExifTags.TAGS[orientation]=='Orientation':
		break

exif = reducida.getexif()

if exif[orientation] == 3:
	image=reducida.rotate(180, expand=True)
elif exif[orientation] == 6:
	image=reducida.rotate(270, expand=True)
elif exif[orientation] == 8:
	image=reducida.rotate(90, expand=True)
image.show()"""


#url = storage.child("Nutrición").child("2RbLSLYeJGefsJQ3bx7YXjXmEb83").child("22-09-2021").child("Foto3").get_url(None)
#with tempfile.TemporaryDirectory() as temp:
	#print("directorio en uso: ", temp)
	#storage.child("Nutrición").child("2RbLSLYeJGefsJQ3bx7YXjXmEb83").child("27-09-2021").child("Foto1").download(temp + "/foto1.jpg")

"""image = cv2.imread(temp + "/foto1.jpg")

	newImg = cv2.resize(image, (1280,800))

	Rotated_image = imutils.rotate(newImg, angle=270) 
	
	cv2.imshow("Rotated", Rotated_image) 
	cv2.waitKey(0)"""

"""def _fix_image_rotation(image):
	orientation_to_rotation_map = {
		3: Image.ROTATE_180,
		6: Image.ROTATE_270,
		8: Image.ROTATE_90,
	}
	try:
		exif = _get_exif_from_image(image)
		orientation = _get_orientation_from_exif(exif)
		rotation = orientation_to_rotation_map.get(orientation)
		if rotation:
			image = image.transpose(rotation)
	except Exception as e:
		pass
	finally:
		return image


def _get_exif_from_image(image):
	exif = {}

	if hasattr(image, '_getexif'):  # only jpegs have _getexif
		exif_or_none = image._getexif()
		if exif_or_none is not None:
			exif = exif_or_none

	return exif


def _get_orientation_from_exif(exif):
	ORIENTATION_TAG = 'Orientation'
	orientation_iterator = (
		exif.get(tag_key) for tag_key, tag_value in ExifTags.TAGS.items()
		if tag_value == ORIENTATION_TAG
	)
	orientation = next(orientation_iterator, None)
	return orientation"""



"""im = Image.open("Foto2.jpg")

reducida = im.resize((800, 900))

girar = _fix_image_rotation(reducida)

girar.show()"""




#download("C:/Users\Desarrollo\Desktop/foto3.jpg")

"""data = urllib.request.urlopen(url).read()
pixmap = QPixmap()
pixmap.loadFromData(data) 
image = cv2.imread(pixmap)

Rotated_image = imutils.rotate(image, angle=90) 
  
cv2.imshow("Rotated", Rotated_image) 
cv2.waitKey(0)"""
#widgets.btnImgNut3.setIcon(pixmap)
#widgets.btnImgNut3.setIconSize(QSize(100, 100))
# Crea un archivo temporal en modo texto

"""temporal3 = tempfile.NamedTemporaryFile()

# Muestra nombre y ruta del archivo temporal creado
print(temporal3, temporal3.name)

# Escribe en el archivo temporal
temporal3.write(b'Temporal')

# Comprueba si existe el archivo temporal
if os.path.exists(temporal3.name):
    print("El archivo temporal existe")

# Cierra y suprime el archivo temporal
#temporal3.close()

# Comprueba si se ha borrado el archivo temporal
if not os.path.exists(temporal3.name):
    print("El archivo temporal ya no existe")"""

#with tempfile.TemporaryDirectory() as temp:
#	print("directorio en uso: ", temp)

tempdir7 = tempfile.TemporaryDirectory()

# Crea archivo temporal en el directorio anterior

storage.child("Nutrición").child("2RbLSLYeJGefsJQ3bx7YXjXmEb83").child("21-10-2021").child("Foto1")

image1 = cv2.imread(tempdir7.name + "/foto1.jpg")
newImg1 = cv2.resize(image1, (900,800))
cv2.imshow("Foto1", newImg1)
cv2.waitKey(0)

print(tempdir7)

