import time
import random

def busqueda_lineal(lista, elemento):
    inicio = time.time()
    for i in range(len(lista)):
        if lista[i] == elemento:
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            return i, tiempo_ejecucion
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return -1, tiempo_ejecucion

def busqueda_binaria(lista, elemento):
    inicio = time.time()
    izquierda, derecha = 0, len(lista) - 1
    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2
        if lista[medio] == elemento:
            fin = time.time()
            tiempo_ejecucion = fin - inicio
            return medio, tiempo_ejecucion
        elif lista[medio] < elemento:
            izquierda = medio + 1
        else:
            derecha = medio - 1
    fin = time.time()
    tiempo_ejecucion = fin - inicio
    return -1, tiempo_ejecucion

# Solicitar al usuario el tamaño de la lista y el elemento a buscar
tamanio_lista = int(input("Ingrese el tamaño de la lista: "))
elemento = int(input("Ingrese el elemento a buscar: "))

# Generar una lista aleatoria de números entre 1 y 1000
lista = [random.randint(1, 1000) for _ in range(tamanio_lista)]

opcion = input("Selecciona una opción (L para búsqueda lineal, B para búsqueda binaria): ")

if opcion.upper() == "L":
    indice, tiempo = busqueda_lineal(lista, elemento)
    if indice != -1:
        print(f"Elemento encontrado en la posición {indice} (Tiempo de ejecución: {tiempo} segundos)")
    else:
        print("Elemento no encontrado")

elif opcion.upper() == "B":
    # Asegurémonos de que la lista esté ordenada para la búsqueda binaria
    lista.sort()
    indice, tiempo = busqueda_binaria(lista, elemento)
    if indice != -1:
        print(f"Elemento encontrado en la posición {indice} (Tiempo de ejecución: {tiempo} segundos)")
    else:
        print("Elemento no encontrado")

else:
    print("Opción no válida. Por favor, selecciona 'L' o 'B'.")
