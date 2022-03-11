import firebase_admin
from firebase_admin import credentials, messaging

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)


def sendPush(title, msg, registration_token, dataObject=None):
    # See documentation on defining a message payload.
    message = messaging.MulticastMessage(
        notification=messaging.Notification(
            title=title,
            body=msg
        ),
        data=dataObject,
        tokens=registration_token,
    )
    # Send a message to the device corresponding to the provided
    # registration token.
    response = messaging.send_multicast(message)
    # Response is a message ID string.
    if response is not None:
        return 'Notificación enviada'
    else:
        return 'Notificación no enviada'


def enviarTodos(title, body):
    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(
            title=title,
            body=body,
        ),
        topic="/topics/all",
    )
    # Send a message to devices subscribed to the combination of topics
    # specified by the provided condition.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)


def topics(topic, titulo, cuerpo):
    condition = "'Intermedio' in topics"
    # See documentation on defining a message payload.
    message = messaging.Message(
        notification=messaging.Notification(
            title=titulo,
            body=cuerpo,
        ),
        topic=topic,
    )
    # Send a message to devices subscribed to the combination of topics
    # specified by the provided condition.
    response = messaging.send(message)
    if response is not None:
        return 'Notificación enviada'
    else:
        return 'Notificación no enviada'
    # Response is a message ID string.
    # return 'Notificación enviada'


'''# The topic name can be optionally prefixed with "/topics/".
    topic = '/topics/Intermedio'

    # See documentation on defining a message payload.
    message = messaging.Message(
        data = {
            'Atención' : 'Nivel intermedio',
        },
        topic = "Intermedio",
    )
    # Send a message to the devices subscribed to the provided topic.
    response = messaging.send(message)
    # Response is a message ID string.
    print('Successfully sent message:', response)'''


# Create a list containing up to 500 registration tokens.
# These registration tokens come from the client FCM SDKs.
def enviarVarios(registration_tokens):
    message = messaging.MulticastMessage(
        data={"hola": "notificacion 1", "adios": "notificacion 2"},
        tokens=registration_tokens,
    )
    response = messaging.send_multicast(message)
    # See the BatchResponse reference documentation
    # for the contents of response.
    print('{0} messages were sent successfully'.format(response.success_count))


def subscribe_to_topic():
    topic = 'Intermedio'
    # [START subscribe]
    # These registration tokens come from the client FCM SDKs.
    registration_tokens = [
        "dZvkTDqxSiaJMg3pwUmE1z:APA91bEp2Fmwx16FZRzGHVggu3bLRdV4x1IK1RU8qGpp40y4PFrU6NVUzNYtd7ZC6DXR1kDTnnJ9vxKzNRrC6ldpmnnINAN-cl262vRtkvUA6G1C_myG8Bd9y9uIrSE2EV3OLtv_bou_",

        # ...
        "d-JXxi3TSqWOcJ1t4jBaBA:APA91bGGradHb1vZGHyz3g9xD3a5EqYYDwWC4xyhUVB8JBBhojzMMgKOQWxpxA-o54Y4GNkn295WdHhZlpnD6UBxCRc38OvSZ5bcNhCcXFsTfhWE77DadNWjo72iBkVBs7oUd3jmrvle",
    ]

    # Subscribe the devices corresponding to the registration tokens to the
    # topic.
    response = messaging.subscribe_to_topic(registration_tokens, topic)
    # See the TopicManagementResponse reference documentation
    # for the contents of response.
    print(response.success_count, 'tokens were subscribed successfully')
    # [END subscribe]
