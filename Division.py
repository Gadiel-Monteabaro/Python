primer_numero = int(input("Ingrese el primer número: "))
segundo_numero = int(input("Ingrese el segundo número: "))

if segundo_numero == 0:
    print("No se puede dividir por cero")
else:
    division = primer_numero / segundo_numero
    print(f"{division}")
