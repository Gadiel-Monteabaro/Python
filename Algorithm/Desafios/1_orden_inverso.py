# Escriba un programa que pida al usuario un entero de tres dígitos, y entregue el número con los digitos en orden inverso

numero = input("Ingresar un numero de tres dígitos: ")

numero_inverso = ""

for i in range(len(numero) - 1, -1, -1):
    numero_inverso += numero[i]

print(numero_inverso)
