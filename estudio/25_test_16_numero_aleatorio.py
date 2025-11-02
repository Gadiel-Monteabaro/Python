import random


def juego_adivinar_numero():
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
                print(
                    f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos."
                )
                break
        except ValueError:
            print("Por favor, introduce un número válido.")


# Ejecutar el juego
juego_adivinar_numero()
