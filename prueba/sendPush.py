import FCMManager as fcm
import time

a = "dZvkTDqxSiaJMg3pwUmE1z:APA91bEp2Fmwx16FZRzGHVggu3bLRdV4x1IK1RU8qGpp40y4PFrU6NVUzNYtd7ZC6DXR1kDTnnJ9vxKzNRrC6ldpmnnINAN-cl262vRtkvUA6G1C_myG8Bd9y9uIrSE2EV3OLtv_bou_"

b = "d-JXxi3TSqWOcJ1t4jBaBA:APA91bGGradHb1vZGHyz3g9xD3a5EqYYDwWC4xyhUVB8JBBhojzMMgKOQWxpxA-o54Y4GNkn295WdHhZlpnD6UBxCRc38OvSZ5bcNhCcXFsTfhWE77DadNWjo72iBkVBs7oUd3jmrvle"
tokens = [a]

#fcm.sendPush("Hi", "This is my next msg", tokens)
#fcm.subscribe_to_topic()

#fcm.topics()
#fcm.enviarVarios(tokens)
#fcm.enviarTodos("Buenas buenas", "Mensaje de prueba")
"""opcion = widgets.ntCmbRemitente.currentText()
grupos = db.child("Grupos").get().val()
listaTokens = []

for nivel, tokens in grupos.items():
    if opcion == nivel["Básico"]:
        listaTokens.append(tokens)
        print(listaTokens)
        break
    else:
        print("Usuario no encontrado")"""

"""string = "EMON - 8:00"
characters = "EMON -"

for x in range(len(characters)):
    string = string.replace(characters[x],"")

print(string)"""

for _ in range(1):
	print("holA")
	time.sleep(1)
print("")
