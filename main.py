from Paquete_Principal import random_manager
from Relaciones import creacion
import time
def menu_inicio():
    print("__________________________________________________________________")
    print("")
    print("Bienvenido a la simulación de un chat")
    print("")

    num_usuarios = int(input("Ingrese el número de usuarios: "))
    if num_usuarios<=1:
        print("Debe de haber más de un usuario en la simulación.")
        menu_inicio()

    print("")
    print("Ingrese la cantidad de tiempo en el que se darán las conversaciones de los usuarios")


    unidad = input("unidad de medida 'mes' o 'año': ")
    if unidad!="mes" and unidad!= "año":
        print("Ingrese una respuesta acertada.")
        menu_inicio()

    cantidad = int(input("Cantidad de tiempo(número de meses o años): "))
    if cantidad<1:
        print("La cantidad de tiempo debe ser mayor o igual a 1.")
        menu_inicio()

    personas= random_manager.crear_simulacion(num_usuarios, cantidad, unidad)
    return personas

def verchat(relaciones,personas):
    for b in personas:
        print(f"Chat de: {b.nombre}")
        print(" ")
        b.imprimirchats()
        print("_____________________________________________________________________________________________________")
    menu2(relaciones,personas)
def imprimirrelaciones(relaciones,personas):
    print("\n")
    for id,lista in relaciones.items():
        dueño= personas[id]
        print(f"Las relaciones de {dueño.nombre} son:" ,end="")
        for relacion in lista:
            end="->"
            if relacion== lista[len(lista)-1]:
                end=""
            amigo= personas[relacion.persona2]
            amistad= relacion.relacion
            print(f"[Amigo:{amigo.nombre}|Amistad:{amistad}]", end=end)
        print("\n________________________________________")
    menu2(relaciones,personas)
def relacionmasfuerte(relaciones, personas):
    print("_________________________________________________________________________________________________")
    mas_fuertes={persona.id:[] for persona in personas}
    for persona in personas:
        id=persona.id
        relacion= relaciones[id]
        max= relacion[0].relacion
        for a in range(0,len(relacion),1):
            rel= relacion[a].relacion
            if max<rel:
                max=rel
        print(f"La relación más fuerte de {persona.nombre} es de {max} y la tiene con: ")
        for rel in relacion:
            if rel.relacion==max:
                print(f" - {personas[rel.persona2].nombre} ")
                mas_fuertes[id].append(rel)

    print("__________________________________________________________")
    max=mas_fuertes[0][0].relacion
    for b in range(0,len(mas_fuertes),1):
        rel=mas_fuertes[b][0].relacion
        if max<rel:
            max= rel

    print(f"La relación más fuerte de todas es de {max} y la poseen:  ")
    finales=[]
    for a in range(0,len(mas_fuertes),1):
        rel= mas_fuertes[a]
        if rel[0].relacion==max:
            finales.append(rel[0].persona1)
            for b in range (0,len(rel),1):
                if rel[b].persona2 not in finales:
                    print(f"- {personas[a].nombre} y {personas[rel[b].persona2].nombre}")
    menu2(relaciones,personas)


def mas_amigos(relaciones,personas):
    print("__________________________________________________________________________________")
    max= len(relaciones[0])
    for id,relacion in relaciones.items():
        if len(relacion)>max:
            max=len(relacion)
    print(f"La persona con más amigos tiene {max} amistades y esta es:  ")
    for id, relacion in relaciones.items():
        if len(relacion) ==max:
            print(f" -{personas[id].nombre}")
    menu2(relaciones,personas)

def error(relaciones,personas):
    print("Ingres un valor válido.")
    menu2(relaciones,personas)

def menu2(relaciones,personas):
    time.sleep(2)
    print("")
    print("________________________________________________________________________________")
    print("A continuación podrá elegir las acciones a realizar sobre los chats creados.")
    print("1. Ver el chat de las usuarios.")
    print("2. Ver las amistades de los usuarios.")
    print("3. Conocer las relaciones más fuertes.")
    print("4. Conocer la persona o personas con más amigos.")
    print("5. Salir")
    opcion= int(input("\nIngrese el número correspondiente a la acción a realizar: "))

    match opcion:

        case 1:
            verchat(relaciones,personas),
        case 2:
            imprimirrelaciones(relaciones,personas),
        case 3:
            relacionmasfuerte(relaciones,personas),
        case 4:
            mas_amigos(relaciones,personas)
        case 5:
            print("Su proceso ha finalizado")

        case _:
            error(relaciones,personas)



if __name__ == '__main__':
    personas= menu_inicio()
    relaciones= creacion.establecer_relaciones(personas)
    menu2(relaciones,personas)





