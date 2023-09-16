def burbuja(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def burbuja_optimizada(arr):
    n = len(arr)
    intercambiado = True
    while intercambiado:
        intercambiado = False
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                intercambiado = True

def main():
    print("Seleccione el método de ordenamiento:")
    print("1. Burbuja")
    print("2. Burbuja optimizada")
    
    opcion = int(input("Ingrese 1 o 2 para seleccionar el método: "))
    
    if opcion != 1 and opcion != 2:
        print("Opción no válida.")
        return
    
    n = int(input("Ingrese el tamaño de la lista: "))
    
    if n <= 0:
        print("El tamaño de la lista debe ser mayor que cero.")
        return
    
    arr = []
    
    for i in range(n):
        elemento = int(input(f"Ingrese el elemento {i + 1}: "))
        arr.append(elemento)
    
    if opcion == 1:
        burbuja(arr)
        print("Lista ordenada usando metodo de burbuja:", arr)
    else:
        burbuja_optimizada(arr)
        print("Lista ordenada usando metodo de burbuja o1
              ptimizada:", arr)

if __name__ == "__main__":
    main()
