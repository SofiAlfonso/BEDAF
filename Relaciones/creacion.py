from Relaciones import Relacion

#Se organizan las fechas con un set, de modo que no hayan fechas repetidas, así se sabe cuántos días hablaron
def detectarfrecuencia(mensajes):
    fechas=[]
    for mensaje in mensajes:
        fecha= str(mensaje.fecha.year)+"-"+str(mensaje.fecha.month)+"-"+str(mensaje.fecha.day)
        fechas.append(fecha)
    return len(set(fechas))

def establecer_relaciones(personas):
    relaciones={persona.id:[] for persona in personas} #grafo, representado en un diccionario (lista de adyacencia)
    for persona in personas:
        id_dueño= persona.id
        chats= persona.chats
        for chat in chats:
            mensajes= chat.mensajes
            cantidad= len(mensajes)
            id_amigo= chat.receptor.id
            frecuencia= detectarfrecuencia(mensajes) #Cuántos días se escribieron
            amistad= cantidad*frecuencia
            relacion= Relacion.Relacion(id_dueño,id_amigo,amistad)
            relaciones[id_dueño].append(relacion)
    return relaciones




