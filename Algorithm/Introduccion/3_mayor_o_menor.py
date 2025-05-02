# Hacer un programa que solicite una edad y determine si es mayor de edad.

# Solicitar al usuario su nombre y su edad
nombre = input("Ingresar tu nombre: ")
edad = int(input("Ingresar tu edad: "))

# Determinar si es mayor o menor
if edad >= 18:
    print(f"Hola!..{nombre}, sos mayor de edad.")
else:
    print(f"Hola!..{nombre}, sos menor de edad.")
