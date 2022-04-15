# Nombre: Angelica Saenz Lacayo
#
# Objetivos:
# 1.Hacer un menu.

#Menu: funcion para hacer menu
import random


def menu():
    print("[1] Lista de emparejamiento")
    print("[2] Ordenar jugadores")
    print("[3] Lista inicial de jugadores")
    print("[4] Lista de cada division")
    print("[5] Jugador con mayor division y puntuacion")
    print("[6] Jugador con menor division y puntuacion")
    print("[7] Promedio por division")
    print("[8] Promedio de puntuación dada una división")
    print("[9] Promedio de puntuación de todas las divisiones")
    print("[10] Cantidad de jugadores por división")
    print("[11] Cantidad de jugadores totales")
    print("[0] Salir del programa")

#tamano de la lista
lista = 30
# Generando lista de floats
lista_de_jugadores = random.sample(range(4, 90), lista)
float_list = [x / 10 for x in lista_de_jugadores]

#Diccionario para guardar datos
valores = {'Hierro': [],
               'Bronce': [],
               'Plata': [],
               'Oro': [],
               'Platino': [],
               'Diamante': [],
               'Maestro': [],
               'Gran Maestro': [],
               "Retador": []
               }


#Ordenar los jugadores en las listas
def ordernarjugadores():
    for jugador in sorted(float_list, reverse=True):
        if 0 <= jugador <= 0.99:
            print("Division Hierro")
            print("-" * 40)
        elif 1 <= jugador <= 1.99:
            print("Division Bronce")
            print("-" * 40)
        elif 2 <= jugador <= 2.99:
            print("Division Plata")
            print("-" * 40)
        elif 3 <= jugador <= 3.99:
            print("Division Oro")
            print("-" * 40)
        elif 4 <= jugador <= 4.99:
            print("Division Platino")
            print("-" * 40)
        elif 5 <= jugador <= 5.99:
            print("Division Diamante")
            print("-" * 40)
        elif 6 <= jugador <= 6.99:
            print("Division Maestro")
            print("-" * 40)
        elif 7 <= jugador <= 7.99:
            print("Division Gran Maestro")
            print("-" * 40)
        elif 8 <= jugador <= 8.99:
            print("Division Retador")
            print("-" * 40)
        else:
            print("No pertenece a ninguna division")
            print("-" * 40)


def ubicacionjugadores():
    # Asignacion de jugadores con respecto a la lista
    for jugador in float_list:
        if 0 <= jugador <= 0.99:
            valores['Hierro'].append(jugador)
        elif 1 <= jugador <= 1.99:
            valores['Bronce'].append(jugador)
        elif 2 <= jugador <= 2.99:
            valores['Plata'].append(jugador)
        elif 3 <= jugador <= 3.99:
            valores['Oro'].append(jugador)
        elif 4 <= jugador <= 4.99:
            valores['Platino'].append(jugador)
        elif 5 <= jugador <= 5.99:
            valores['Diamante'].append(jugador)
        elif 6 <= jugador <= 6.99:
            valores['Maestro'].append(jugador)
        elif 7 <= jugador <= 7.99:
            valores['Gran Maestro'].append(jugador)
        elif 8 <= jugador <= 8.99:
            valores['Retador'].append(jugador)

    for k, v in valores.items():
        print(k)
        print(v)
        print("-------------")


def lista_ini_jugadores():
    for k in valores:
        print(k)


def maxdivpts():
    list_emparejamiento_actual = []

    for k, v in valores.items():
        if any(v):
            list_emparejamiento_actual.append(k)

    res_max = max(float_list, key=lambda x: float(x))
    print(res_max)
    print(list_emparejamiento_actual[-1])

def mindivpts():
    list_emparejamiento_actual = []

    for k, v in valores.items():
        if any(v):
            list_emparejamiento_actual.append(k)

    res_min = min(float_list, key=lambda x: float(x))
    print(res_min)
    print(list_emparejamiento_actual[0])

#Promedio
def promedio(lst):
    return sum(lst)/len(lst)




menu()
opcion = int(input("Digite alguna opcion: "))

while opcion != 0 :
    if opcion == 1:
        print(float_list)
    elif opcion == 2:
        ordernarjugadores()
    elif opcion == 3:
        lista_ini_jugadores()
    elif opcion == 4:
        ubicacionjugadores()
    elif opcion == 5:
        maxdivpts()
    elif opcion == 6:
        mindivpts()
    elif opcion == 7:
        print("qw")
    elif opcion == 8:
        print("Eligio opcion 8")
    elif opcion == 9:
        print(promedio(float_list))
    elif opcion == 10:
        print("Eligio opcion 10")
    elif opcion == 11:
        print("Eligio opcion 11")
    else:
        print("Opcion invalida")

    print()
    menu()
    opcion = int(input("Digite alguna opcion: "))

print("Gracias por usar el programa")


