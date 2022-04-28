import random
import statistics
import sys
#tamano de la lista
lista = 10

#Generando lista de floats
lista_de_jugadores = random.sample(range(5, 100), lista)
float_list = [x/10 for x in lista_de_jugadores]

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

#Asignacion de jugadores con respecto a la lista
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
    elif 8 <= jugador:
        valores['Retador'].append(jugador)


def promedio(lst):
    return sum(lst)/len(lst)


# for k, v in valores.items():
#     print(k)
#     print(v)
#     print("-------------")
#
#
# for k, v in valores.items():
#     if any(v):
#         print(promedio(v))


def promedio_por_division():
    for k, v in valores.items():
        print(k)
        if any(v):
            pmd = promedio(v)
        print(pmd)



print(promedio_por_division())



# for k, v in valores.items():
#     if any(v):
#         count_elements = len(v)
#         print("Cantidad de jugadores: ", count_elements)
# for k, v in valores.items():
#     print(k)
#     if any(v):
#         count_elements = len(v)
#         print("Cantidad de jugadores: ", count_elements)
#     else:
#         print("No posee jugadores")
#     print("-------------")

# counter = 0
# for i in valores:
#     counter+=1
# print(counter)



# for k in valores:
#     print(k)



# print("Jugador con mayor division y puntuacion")
# print(max(valores[max(valores)].items()))
# print(max(valores.values()))
#
# res_min = min(float_list,key=lambda x:float(x))
# res_max = max(float_list,key=lambda x:float(x))
# print(res_max)
# print(res_min)
# print("-------------")
# print("Jugador con menor division y puntuacion")
# print(min(valores))
# print(min(valores.values()))

# list_emparejamiento_actual = []
#
# for k, v in valores.items():
#     if any(v):
#         list_emparejamiento_actual.append(k)
#
# res_min = min(float_list,key=lambda x:float(x))
# res_max = max(float_list,key=lambda x:float(x))
# print(list_emparejamiento_actual[-1])
# print(res_max)
# print(list_emparejamiento_actual[0])
# print(res_min)
#
# print(valores)


# players = {
#     "bronce": [50, 73, 20],
#     "gold": [100, 200, 120],
#     "platinum": [430, 500, 600],
#     "diamond": [700, 850, 943],
# }
#
#
# def avg(points: list) -> float:
#     avg = 0
#     for v in points:
#         avg += v
#     avg /= len(points)
#     return avg
#
#
# div_averages = [avg(v) for (_, v) in players.items()]
# total_avg = avg(div_averages)
# print(div_averages)
# print(total_avg)
#
#
# from statistics import mean
# players = { "bronce": [50,73,20], "gold": [100,200,120], "platinum": [430, 500, 600], "diamond": [700, 850, 943], }
# div_averages = [mean(v) for (_,v) in players.items()]
# total_avg = mean(div_averages)
# print(div_averages)
# print(total_avg)