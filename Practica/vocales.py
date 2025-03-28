texto = input("Escribe un texto: ")
vocales = "aeiouAEIOU"
cantidad_de_vocales = 0

for i in texto:
    if i in vocales:
        cantidad_de_vocales += 1

print(f"La cantidad de vocales en el texto es: {cantidad_de_vocales}")
