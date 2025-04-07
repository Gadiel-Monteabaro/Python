# Crea una lista de números que cuente el número de veces que aparece el número ingresado por el usuario.
lista = [12, 1, 2, 5, 4, 6, 8, 4, 2, 1, 55, 4, 74, 2]
num = int(input("Ingresar un número: "))

def contar_numeros(num):
  count = 0
  for i in lista:
    if i == num:
      count += 1
  print(count)

contar_numeros(num)