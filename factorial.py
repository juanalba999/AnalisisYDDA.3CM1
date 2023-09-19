def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

try:
    n = int(input("Ingresa un número para calcular su factorial: "))
    if n < 0:
        print("Ingresa un número no negativo")
    else:
        result = factorial(n)
        print("El factorial de", n, "es:", result)
except ValueError:
    print("Ingresa un número válido :/ ")
