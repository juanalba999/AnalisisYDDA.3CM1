# Suma
def sumar (a, b):
    return a + b

# Resta
def restar (a, b):
    return a - b

# Multiplicacion
def multiplicar (a, b):
    return a * b

# Division
def dividir (a, b):
    if b != 0:
        return a / b
    else:
        return "no puedes dividir por cero :( "

# Menu

while True:
    print("Calculadora basica: ")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicacion")
    print("4. Division")
    print("5. Salir")
    
    opcion = input("Selecciona una operacion: ")
    
    if opcion == '5':
        print("Gracias por usar esta calculadora :) ")
        break
    
    if opcion not in ('1', '2', '3', '4','5'):
        print("Por favor selecciona una opción válida :/ ")
        continue

    num1 = float(input("Ingresa el primer numero: "))
    num2 = float(input("Ingresa un segundo numero: "))
    
    if opcion == '1':
        print("Resultado:", sumar(num1, num2))
    elif opcion == '2':
        print("Resultado:", restar(num1, num2))
    elif opcion == '3':
        print("Resultado:", multiplicar(num1, num2))
    elif opcion == '4':
        print("Resultado:", dividir(num1, num2))
    
