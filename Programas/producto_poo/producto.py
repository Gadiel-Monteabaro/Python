class Inventario:
    # constructor
    def __init__(self):
        self.productos = []

    def agregar_producto(self, nombre, precio, stock):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                print("El producto ingresado ya existe.")
                return

        nuevo_producto = Producto(nombre, precio, stock)
        self.productos.append(nuevo_producto)
        print("Producto Agregado")

    def buscar_producto(self, nombre):
        for producto in self.productos:
            if producto.nombre.lower() == nombre.lower():
                return producto

        return None

    def mostrar_inventario(self):
        if not self.productos:
            print("Inventario vacío.")
            return
        print("Inventario:")
        for producto in self.productos:
            print(producto.listar_producto())


class Producto:
    # constructor
    def __init__(self, nombre, precio, stock=0):
        self._nombre = nombre
        self._precio = precio
        self.stock = stock

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, precio):
        if precio is None:
            raise ValueError("El precio no puede estar vacío.")
        if precio < 0:
            raise ValueError("El precio debe ser mayor a cero.")
        self._precio = precio

    def actualizar_stock(self, cantidad):
        if not isinstance(cantidad, int):
            raise ValueError("La cantidad debe ser un número entero.")
        self.stock += cantidad

    def total_producto(self):
        return self.stock * self._precio

    def listar_producto(self):
        return f"Producto: {self.nombre} | Precio: ${self.precio} | Stock: {self.stock} | Total: ${self.total_producto()}"


def main():
    inventario = Inventario()

    while True:
        accion = input(
            "Agregar producto (1), Actualizar stock de un producto (2), Mostrar productos (3) "
        )
        if accion == "1":
            nombre = input("Ingresar nombre del producto: ")
            precio = int(input("Ingresar el precio del producto: "))
            stock = int(input("Ingresar la cantidad del producto: "))
            inventario.agregar_producto(nombre, precio, stock)

        if accion == "2":
            nombre = input("Ingresar nombre del producto: ")
            producto = inventario.buscar_producto(nombre)

            if producto:
                cantidad = int(input("Ingresar la cantidad."))
                producto.actualizar_stock(cantidad)

        if accion == "3":
            inventario.mostrar_inventario()


if __name__ == "__main__":
    main()
"""
  Nombre, Precio, Stock siendo obligatorios nombre y precio
  El stock debe comenzar con 0
  _Metodos actualizar stock, calcular el total del inventario y poder ver los datos
  Aplicación de consola
  Mostrar los datos del producto, stock e inventario final
"""
