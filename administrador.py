productos = []

def agregar_producto(nombre, cantidad):
    for producto in productos:
        if producto['nombre'] == nombre:
            producto['cantidad'] += cantidad
            return
    productos.append({'nombre': nombre, 'cantidad': cantidad})

def actualizar_producto(nombre, cantidad):
    for producto in productos:
        if producto['nombre'] == nombre:
            producto['cantidad'] = cantidad
            return
    print(f"Producto {nombre} no encontrado.")
    mostrar_inventario()

def mostrar_inventario():
    for producto in productos:
        print(
            f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}")

agregar = input("Desea agregar un producto? (s/n): ")

if agregar == 's':
    nuevo_producto = input("Ingrese el nombre del producto: ")
    nueva_cantidad = int(input("Ingrese la cantidad del producto: "))
    agregar_producto(nuevo_producto, nueva_cantidad)

actualizar = input("Desea actualizar la cantidad de un producto? (s/n): ")

if actualizar == 's':
    producto = input("Ingrese el nombre del producto: ")
    cantidad = int(input("Ingrese la nueva cantidad del producto: "))
    actualizar_producto(producto, cantidad)
  
mostrar_inventario()
