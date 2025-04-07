# Escribe un programa que pida al usuario el radio de un circulo y calcule el área
import math
radio_circulo = float(input("Introduce el radio del circulo: "))
area_circulo = math.pi * radio_circulo ** 2
print("El area del circulo es: ", round(area_circulo, 2))
