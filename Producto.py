precio = round(float(input("Ingresar el precio del producto: ")), 2)
cantidad = int(input("Ingresar la cantidad de productos: "))

if precio > 100 or (precio > 50 and cantidad < 10):
    print("Caro")
else:
    print("Barato")
