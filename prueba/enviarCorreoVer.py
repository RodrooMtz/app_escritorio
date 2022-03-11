import pyrebase

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

auth.sign_in_with_email_and_password("doceunowoow@hotmail.com", "123456789")
usuario = auth.current_user
dictUser = dict(usuario)
idToken = dictUser['idToken']
#self.uid = dictUser['localId']
#self.fotoUser(idToken)
# print(str(auth.current_user))
# print(type(idToken))
print(str(idToken))
auth.send_email_verification(idToken)

