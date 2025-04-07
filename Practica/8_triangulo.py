# Escribe un programa que solicite tres lados de un triángulo e indique si es equilátero, isósceles o escaleno.
ladoUno = float(input("Ingrese el primer lado: "))
ladoDos = float(input("Ingrese el segundo lado: "))
ladoTres = float(input("Ingrese el tercer lado: "))

if ladoUno == ladoDos and ladoUno == ladoTres:
    print("Es un triángulo equilátero")
elif ladoUno == ladoDos or ladoUno == ladoTres or ladoDos == ladoTres:
    print("Es un triángulo isósceles")
else:
    print("Es un triángulo escaleno")