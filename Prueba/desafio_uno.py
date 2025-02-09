# Modifica el siguiente código (que identifica el mayor de dos números) a
# fin de encontrar ahora el mayor de 3 números.
numero_1 = 12
numero_2 = -5
numero_3 = 8
if numero_1 > numero_2:
    print(f"El mayor de los dos números es: {numero_1}")
else:
    print(f"El mayor de los dos números es: {numero_2}")


if numero_1 > numero_2 and numero_1 > numero_3:
    print(f"El mayor de los tres números es: {numero_1}")
elif numero_2 > numero_1 and numero_2 > numero_3:
    print(f"El mayor de los tres números es: {numero_2}")
else:
    print(f"El mayor de los tres números es: {numero_3}")
