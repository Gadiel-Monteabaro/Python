# Escribe un programa que solicite al usuario su nombre, edad y número de teléfono. Verifica que ninguno de estos datos esté vacío o sea un valor falso (por ejemplo, 0).
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
telefono = input("Ingrese su número de teléfono: ")

if nombre == "" or edad == 0 or telefono == "":
    print("Por favor, llene todos los campos")
else:
    print("Gracias por registrarte")
