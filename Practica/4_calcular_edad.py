# Escribe un programa que pida al usuario su año de nacimiento, calcule su edad y genere un mensaje de saludo personalizado que incluya su nombre y la edad calculada.
from datetime import datetime

nombreUsuario = input("Ingrese su nombre: ")
añoNacimiento = int(input("Ingrese su año de nacimiento: "))

edad = datetime.now().year - añoNacimiento

print(f"Hola {nombreUsuario.capitalize()}, tu edad es {edad} años.")
