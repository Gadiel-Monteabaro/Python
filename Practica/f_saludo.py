# Escribe una función que reciba como parámetros un nombre y devuelva un saludo personalizado
name = input("¿Cual es tu nombre? \n")

def saludo(name):
  return f"Hola, {name}!"

print(saludo(name))