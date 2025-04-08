# Escribe un programa que a partir de un número entero positivo, muestre por pantalla si es primo o no.
numero = int(input("Ingresar un número: "))

if numero % numero and numero % 1 == 0:
  print("El número", numero, "es primo")
else:
  print("El número", numero, "no es primo")  