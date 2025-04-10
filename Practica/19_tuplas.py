coloresFavoritos = ("Turqueza", "Azul", "Verde")
print(coloresFavoritos[1])

numeros = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

numeroIngresado = int(input("Ingrese un número: "))

if numeroIngresado in numeros:
    print("El número ingresado se encuentra en la tupla")
else:
    print("El número ingresado no se encuentra en la tupla")

comprobar = False
for i in numeros:
    if i == numeroIngresado:
        comprobar = True
        break

if comprobar:
    print("El número ingresado se encuentra en la tupla")
else:
    print("El número ingresado no se encuentra en la tupla")
