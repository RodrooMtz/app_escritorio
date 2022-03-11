import random
import cv2
import pyrebase
import random

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
storage = firebase.storage()
db = firebase.database()

video = cv2.VideoCapture(0)
a = 0
#token = "ca294015-4f37-4a28-9e0d-ff51847f5824"
#token = 
while True:
    
    check, frame = video.read()

    cv2.imshow("video", frame)

    if not check:
        break

    key = cv2.waitKey(1)

    if key%256 == 97: # letra a
        num = random.randint(1, 1000)
        img_name = "imagen_{}.png".format(num)
        cv2.imwrite(img_name, frame)
        storage.child("imagen_{}.png".format(num)).put(img_name)
        #token = str(storage.credentials.access_token())
        #url = storage.child("imagen_{}.png".format(num)).get_url()
        #db.child("Usuarios").child("aWEBFAuKjjT4DkB8UNQAeN5CPZz2").child("URLImage").set("gs://resilience66-abd3e.appspot.com/imagen_{}.png".format(num))
        print("{} written".format(img_name))
        #print(url) 
        a += 1
video.release()
cv2.destroyAllWindows()