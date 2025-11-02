# Escribe un programa que permita realizar la división de dos números siempre y cuando el denominador no sea 0.
primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

if segundo_numero == 0:
    print("No se puede dividir por cero")
else:
    division = primer_numero / segundo_numero
    print(f"{division}")
