# Escribe un programa que pregunte al usuario la hora actual t del reloj y un número entero de horas h, que indique qué hora marcará el reloj dentro de h horas
t = int(input("Ingrese la hora actual: "))
h = int(input("Ingrese cantidad de horas: "))

hora = (t + h) % 24

print(hora)
