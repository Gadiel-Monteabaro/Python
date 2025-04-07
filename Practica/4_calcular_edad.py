from datetime import datetime

nombreUsuario = input("Ingrese su nombre: ")
añoNacimiento = int(input("Ingrese su año de nacimiento: "))

edad = datetime.now().year - añoNacimiento

print(f"Hola {nombreUsuario}, tu edad es {edad} años.")
