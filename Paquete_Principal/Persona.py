from Paquete_Principal import Mensaje
from Paquete_Principal import Chat
class Persona:

    def __init__(self,nombre,id,chats):
        self.nombre=nombre
        self.id=id
        self.chats=chats

    def recibirmensaje(self, mensaje):
        ms= Mensaje.Mensaje(mensaje.id_emisor,mensaje.id_receptor,mensaje.mensaje,mensaje.fecha,"recibido")
        chats= ms.id_receptor.chats
        emisor= ms.id_receptor
        nuevo= False
        if chats:
            for a in chats:
                if a.receptor== ms.id_emisor:
                    a.mensajes.append(ms)
                    nuevo=False
                    break
                else:
                    nuevo= True
            if nuevo:
                mensajes= []
                chat= Chat.Chat(emisor,ms.id_emisor,mensajes)
                chat.mensajes.append(ms)
                emisor.chats.append(chat)
        else:
            mensajes = []
            chat = Chat.Chat(emisor, ms.id_emisor, mensajes)
            chat.mensajes.append(ms)
            emisor.chats.append(chat)


    def enviarmensaje(self,emisor,receptor,cantidad,unidad):
        chats= emisor.chats
        nuevo= False
        ms = Mensaje.Mensaje(emisor, receptor, "", "", "enviado")
        ms.mensaje = ms.mensajerandom()
        ms.fecha = ms.fecharandom(cantidad, unidad)

        if chats:
            for a in chats:
                if a.receptor== receptor:
                    a.mensajes.append(ms)
                    nuevo= False
                    break
                else:
                    nuevo= True
            if nuevo:
                mensajes= []
                chat= Chat.Chat(emisor,receptor,mensajes)
                chat.mensajes.append(ms)
                emisor.chats.append(chat)
        else:
            mensajes = []
            chat = Chat.Chat(emisor, receptor, mensajes)
            chat.mensajes.append(ms)
            emisor.chats.append(chat)

        receptor.recibirmensaje(ms)

    def imprimirchats(self):
        chats= self.chats
        for a in chats:
            print(f"* dueño: {self.nombre}| amigo: {a.receptor.nombre}| mensajes:")
            mensajes= a.mensajes
            for c in mensajes:
                print(f" - mensaje:{c.mensaje}| fecha: {c.fecha} | estado: {c.estado}")
            print("___________________________________________________________________________________________")