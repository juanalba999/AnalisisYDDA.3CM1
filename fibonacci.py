def fibonacci(n):
    fib_sequence = [0, 1] 
    while fib_sequence[-1] + fib_sequence[-2] <= n:
        next_number = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_number)
    return fib_sequence

try:
    n = int(input("Ingresa un valor para generar la sucesión de Fibonacci: "))
    if n < 0:
        print("Ingresa un número no negativo.")
    else:
        result = fibonacci(n)
        print("Sucesión de Fibonacci hasta", n, "es:", result)
except ValueError:
    print("Ingresa un número válido :/ ")
