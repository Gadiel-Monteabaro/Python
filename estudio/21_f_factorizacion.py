# Escribe una función que permita calcular el factorial de un número
def factorial(num):
    acumulador = 1

    if not isinstance(num, int) or num < 0:
        raise ValueError("El valor debe ser un número entero no negativo.")

    for i in range(1, num + 1):
        acumulador = acumulador * i

    return acumulador


def factorialWhile(num):
    acumulador = 1
    contador = 1

    if not isinstance(num, int) or num < 0:
        raise ValueError("El valor debe ser un número entero no negativo.")

    while contador <= num:
        acumulador = acumulador * contador
        contador += 1

    return acumulador


print("Calculadora Factorial.")
numero = int(input("Ingresar un número entero positivo \n"))
print(f"Calculo factorial con For : {factorial(numero)}")
print(f"Calculo factorial con While : {factorialWhile(numero)}")
