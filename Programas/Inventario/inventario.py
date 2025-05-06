"""
Escribe un programa que tenga un menú para gestionar un inventario de productos:
   a. Agregar Producto
   b. Mostrar Inventario
   c. Buscar Producto
   d. Eliminar Producto
   e. Salir
"""

import os
import json
import uuid

INVENTARIO = os.path.join(os.path.dirname(__file__), "inventario.json")


# cargar datos del inventario
def cargar_inventario():
    if os.path.exists(INVENTARIO):
        try:
            with open(INVENTARIO, "r", encoding="utf-8") as archivo:
                # convertir el archivo a un diccionario, permitiendo acceder a los datos
                return json.load(archivo)
        except (json.JSONDecodeError, TypeError) as error:
            print(f"Error al cargar los productos: {error}")
    return []


# guardar datos en el inventario
def guardar_inventario(productos):
    try:
        with open(INVENTARIO, "w", encoding="utf-8") as archivo:
            json.dump(productos, archivo, indent=2)
    except TypeError as error:
        print(f"Error al guardar los datos en el inventario: {error}")


# agregar productos al inventario
def agregar_producto(productos, nombre, cantidad):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print("El producto ya ha sido agregado")
            return

    id_producto = str(uuid.uuid4())
    productos.append(
        {"id": id_producto, "nombre": nombre.lower().capitalize(), "cantidad": cantidad}
    )

    guardar_inventario(productos)
    print(f"Producto {nombre} agregado con {cantidad} unidades.")


# mostrar inventario
def mostrar_inventario(productos):
    if not productos:
        print("El inventario esta vácio.")
        return

    for producto in productos:
        print(f"{producto['nombre']} - {producto['cantidad']}")


# buscar producto
def buscar_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            print(f"{producto['nombre']} - {producto['cantidad']}")
            return
    print(f"El producto no fue encontrado.")


# eliminar producto
def eliminar_producto(productos, nombre):
    for producto in productos:
        if producto["nombre"].lower() == nombre.lower():
            productos.remove(producto)
            guardar_inventario(productos)
            print(f"El producto {producto["nombre"]} fue eliminado correctamente.")
            return
    print(f"El producto no fue encontrado.")


# ejecución del programa
def main():
    productos = cargar_inventario()

    while True:
        accion = input(
            "Desea agregar un producto (a), mostrar inventario (b), buscar producto (c), eliminar producto (d) o salir (e): "
        )

        if accion == "a":
            nombre = input("Ingresar nombre del producto: ").strip().lower()
            if not nombre:
                print("Por favor ingresar el nombre del producto")
                continue

            while True:
                try:
                    cantidad = int(input("Ingresar cantidad del producto: ").strip())
                    if cantidad <= 0:
                        print("La cantidad debe ser un número positivo.")
                        continue
                    break
                except ValueError:
                    print(f"Error: ingresar un número válido.")

            agregar_producto(productos, nombre, cantidad)

        if accion == "b":
            mostrar_inventario(productos)

        if accion == "c":
            if not productos:
                print("No hay productos disponibles para buscar.")
                continue

            nombre = input("Ingresar nombre del producto: ").strip()
            if not nombre:
                print("Por favor ingresar el nombre del producto")
                continue

            buscar_producto(productos, nombre)

        if accion == "d":
            nombre = input("Ingresar nombre del producto: ").strip()
            if not nombre:
                print("Por favor ingresar el nombre del producto")
                continue

            eliminar_producto(productos, nombre)

        if accion == "e":
            break


# Ejecutar el programa sin importarlo, cuando se importa se ignorará
if __name__ == "__main__":
    main()
