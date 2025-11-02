# Escribe un programa que solicite al usuario que ingrese una contraseña y confirme la contraseña. El programa debe verificar si ambas contraseñas coinciden y no están vacías.
usuarioPassword = input("Ingrese su contraseña: ")
password = "HolaMundo!"

if usuarioPassword == "":
    print("Por favor, ingrese una contraseña")
elif usuarioPassword == password:
    print("Contraseña ingresada correctamente")
else:
    print("La contraseña ingresada es incorrecta")
