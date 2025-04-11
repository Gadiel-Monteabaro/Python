# Hacer un programa que solicite por teclado dos número y muestre la suma , la resta ,la multiplicación y la división de esos números

# Solicitar los número a operar
numero_uno = float(input("Ingresar el número uno: "))  #
numero_dos = float(input("Ingresar el número dos: "))  #

suma = numero_uno + numero_dos
# Imprimir la suma
print(f"Suma: {round(suma, 2)}")

resta = numero_uno - numero_dos
# Imprimir la resta
print(f"Resta: {round(resta, 2)}")

multiplicacion = numero_uno * numero_dos
# Imprimir la multiplicación
print(f"Multiplicación: {round(multiplicacion, 2)}")

division = numero_uno / numero_dos
# Imprimir la división
print(f"División: {round(division, 2)}")