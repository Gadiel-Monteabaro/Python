# Escribe un programa que pida al usuario los dos catetos de un triángulo rectángulo y calcule la hipotenusa.
cateto_1 = float(input("Ingresar el valor del cateto 1: "))
cateto_2 = float(input("Ingresar el valor del cateto 2: "))

hipotenusa = (cateto_1**2 + cateto_2**2) ** 0.5

print("La hipotenusa es: ", round(hipotenusa, 2))
