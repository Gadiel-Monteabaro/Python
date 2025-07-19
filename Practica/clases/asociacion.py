class Producto:
    # constructor
    def __init__(self, nombre, precio, cantidad, categoria, proveedor):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.categoria = categoria
        self.proveedor = proveedor

        self.categoria.agregar_producto(self)
        self.proveedor.agregar_producto(self)

    def __str__(self):
        return f"Producto: {self.nombre} \nPrecio: {self.precio} \nCantidad: {self.cantidad} \nCategoria: {self.categoria} \nProveedor: {self.proveedor}"


class Categoria:
    # constructor
    def __init__(self, categoria):
        self.categoria = categoria
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __str__(self):
        return f"La categoria {self.categoria} tiene {len(self.productos)} productos."


class Proveedor:
    # constructor
    def __init__(self, proveedor):
        self.proveedor = proveedor
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def __str__(self):
        return f"El proveedor {self.proveedor} tiene {len(self.productos)} productos."


comida = Categoria("Comida")
proveedor = Proveedor("La Granja")

producto1 = Producto("Harina", 0.8, 250, comida, proveedor)
producto2 = Producto("Lacteo", 0.5, 50, comida, proveedor)
producto3 = Producto("Manteca", 0.3, 75, comida, proveedor)

print(producto1)
print(producto2)
print(producto3)

print(proveedor)
print(comida)


# Crear una jerarquía de asociación que ilustre de Productos, Categoria y Proveedor

# Asociación
"""
| relación entre dos o más clases
| permite modelar relaciones entre objetos, flexibilidad
| las clases relacionadas pueden tener una estructura de dependencia mutua
| cada clase mantiene su propia responsabilidad y estado
| la relación entre ellas se establece a través de objetos individuales
"""
