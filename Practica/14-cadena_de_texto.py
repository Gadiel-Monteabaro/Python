# Escribe un programa que cuente los caracteres de una cadena de texto proporcionada por el usuario utilizando el for.
texto = input("Escribe un texto: ")
contador = 0

for i in texto:
    contador += 1
    
print("El texto tiene", contador, "caracteres")