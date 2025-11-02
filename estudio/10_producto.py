# Escribe un programa que solicite al usuario el precio y la cantidad de un producto. Clasifique el producto como "caro" si el precio es mayor de $100 o si la cantidad es menor que 10 y el precio es mayor de $50. De lo contrario, clasifíquelo como "barato". Incluye condiciones para manejar valores falsos (0 o vacío).
precio = round(float(input("Ingresar el precio del producto: ")), 2)
cantidad = int(input("Ingresar la cantidad de productos: "))

if precio > 100 or (precio > 50 and cantidad < 10):
    print("Caro")
else:
    print("Barato")
