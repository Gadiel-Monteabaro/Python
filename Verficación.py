nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))
telefono = input("Ingrese su número de teléfono: ")

if nombre == "" or edad == 0 or telefono == "":
    print("Por favor, llene todos los campos")
else:
    print("Gracias por registrarte")
