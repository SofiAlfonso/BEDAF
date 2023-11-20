import random
from Paquete_Principal import Persona

def imprimir_personas(personas):
    print(f"A la simulación han ingresado {len(personas)} usuarios: ")
    for a in personas:
        print(f" - {a.nombre}")
    print(" ")

def organizarchats(personas):
    for persona in personas:
        chats= persona.chats
        for chat in chats:
            arreglo= chat.mensajes
            n= len(arreglo)
            for i in range(n - 1):
                for j in range(n - 1 - i):
                    if arreglo[j].fecha > arreglo[j + 1].fecha:
                        arreglo[j], arreglo[j + 1] = arreglo[j + 1], arreglo[j]

def crear_simulacion(num_personas,cantidad, unidad):
    nombres=["María","Sofía","Isabella","Valentina","Emma","Martina","Lucía","Victoria","Luciana","Valeria","Camila","Julieta","Ximena","Sara","Daniela","Emilia","Renata","Mía","Catalina","Julia","Elena","Olivia","Regina","Paula","Natalia","Mariana","Samantha","María","Antonella","Gabriela","Emily","María José","Zoe","Alma","Alejandra","Armando", "Arturo", "Augusto", "Aurelio","Benjamín","Benedicto","Bernarndo","Boris","Braulio","Brian","Bruno","Caín","Camilo","Carlos","Casimiro","César", "Christian","Christopher","Cristóbal","Claudio","Clemente","Constancio","Constantino","Cristian","Cristóbal","Daniel","Dario","David"]
    apellidos=["Rodriguez","Martinez", "Garcia", "Gomez", "Lopez","Gonzalez", "Hernandez","Sanchez", "Perez","Ramirez","Diaz","Torres",	"Muñoz","Rojas","Moreno","Vargas","Ortiz","Jimenez","Castro","Gutierrez","Alvarez","Valencia","Ruiz","Suarez","Herrera","Romero","Quintero","Morales","Giraldo","Rivera","Arias","Florez","Marin","Castillo"]

    personas=[]
    for i in range(0,num_personas,1):
        nombre= random.choice(nombres) +"_"+ random.choice(apellidos)
        chats=[]
        personas.append(Persona.Persona(nombre,i,chats))

    if unidad=="mes":
        mensajes= random.randint(num_personas*cantidad,30*num_personas*cantidad)
    elif unidad=="año":
        mensajes = random.randint(num_personas*cantidad*12,30*num_personas*cantidad*12)

    for a in range(0, mensajes,1):
        listo= True
        emisor= random.choice(personas)
        receptor= random.choice(personas)
        while listo:
            if emisor==receptor:
                receptor= random.choice(personas)
            else:
                listo= False
        emisor.enviarmensaje(emisor,receptor,cantidad,unidad)

    imprimir_personas(personas)
    organizarchats(personas)

    return personas
