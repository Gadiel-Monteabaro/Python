# Escribe un programa que genere un número aleatorio entre 1 y 100 y permita al usuario adivinar el número. El programa debe brindar pistas (ej. el número secreto es mayor) y debe continuar pidiendo al usuario que adivine hasta que acierte. Al finalizar, debe mostrar el número de intentos.
import random


def adivinar_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    print("¡Adivina el número entre 1 y 100!")

    while True:
        try:
            adivinanza = int(input("Introduce tu adivinanza: "))
            intentos += 1

            if adivinanza < numero_secreto:
                print("El número secreto es mayor.")
            elif adivinanza > numero_secreto:
                print("El número secreto es menor.")
            else:
                print(f"Adivinaste el número {numero_secreto} en {intentos} intentos.")
                break
        except ValueError:
            print("Por favor, introduce un número válido.")


adivinar_numero()
