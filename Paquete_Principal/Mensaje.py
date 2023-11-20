import random
import datetime
class Mensaje:

    def __init__(self,id_emisor,id_receptor,mensaje,fecha,estado):
        self.id_emisor=id_emisor
        self.id_receptor= id_receptor
        self.mensaje= mensaje
        self.fecha=fecha
        self.estado= estado #mensaje enviado o recibido

    def mensajerandom(self):
        mensajes=["hola", "¿cómo estás?", "Te quiero", "Eres un muy buen amigo", "Luces bien hoy", "Estoy bien, y tú?", "¿Quieres salir?", "¿Qué haces?", "¡Que bien!", "Te extraño", "Hasta mañana", "Adiós"]
        mensaje= random.choice(mensajes)
        return mensaje


    def fecharandom(self,num,dec):
        final= datetime.datetime(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)

        if dec == "mes":
            mes=int(final.month)-num
            if mes>=1:
                if mes!=2:
                    inicio= datetime.datetime(int(final.year),mes,30)
                else:
                    inicio = datetime.datetime(int(final.year), mes, 28)
            else:
                mes=12+mes
                if mes != 2:
                    inicio = datetime.datetime(final.year -1, mes, 30)
                else:
                    inicio = datetime.datetime(final.year-1, mes, 28)

        else:
            inicio = datetime.datetime(int(final.year)-num, 1, 1)

        date= inicio +(final-inicio)*random.random()

        return date

