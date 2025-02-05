usuarioPassword = input("Ingrese su contraseña: ")
password = "HolaMundo!"

if usuarioPassword == "":
    print("Por favor, ingrese una contraseña")
elif usuarioPassword == password:
    print("Contraseña ingresada correctamente")
else:
    print("La contraseña ingresada es incorrecta")
