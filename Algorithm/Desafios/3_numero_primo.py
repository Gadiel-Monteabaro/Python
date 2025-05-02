# Escribir un programa que pida al usuario un número entero y muestre por pantalla si es un número primo o no
def numero_primo(n):
    if n < 2:
        return f"El número {n} no es primo."

    for i in range(2, n):
        if n % i == 0:
            return f"El número {n} no es primo."

    return f"El número {n} es primo."


n = int(input("Ingresar un número entero positivo:"))


print(numero_primo(n))
