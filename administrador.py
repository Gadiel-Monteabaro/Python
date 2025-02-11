import json
import os

INVENTARIO = 'inventario.json'

# Cargar los productos del inventario
def cargar_inventario():
  if os.path.exists(INVENTARIO):
    with open(INVENTARIO, 'r', encoding="utf-8") as archivo:
      return json.load(archivo) 
  return []

# Guardar los productos en el inventario
def guardar_inventario(productos):
  with open(INVENTARIO, 'w', encoding="utf-8") as archivo:
    json.dump(productos, archivo, indent=4)

# Agregar un producto al inventario
def agregar_producto(productos, nombre, cantidad):
  for producto in productos:
    if producto['nombre'] == nombre:
      producto['cantidad'] += cantidad
      return
  productos.append({'nombre': nombre, 'cantidad': cantidad})
  guardar_inventario(productos)

# Actualizar un producto en el inventario
def actualizar_producto(productos, nombre, cantidad):
  for producto in productos:
    if producto['nombre'].lower() == nombre.lower():
      producto['cantidad'] = cantidad
      guardar_inventario(productos)
      return
  print(f"Producto {nombre} no encontrado.")

# Mostrar el inventario
def mostrar_inventario(productos):
  for producto in productos:
    print(
      f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}")


productos = cargar_inventario()

agregar = input("Desea agregar un producto? (s/n): ")

if agregar == 's':
  nuevo_producto = input("Ingrese el nombre del producto: ")
  nueva_cantidad = int(input("Ingrese la cantidad del producto: "))
  agregar_producto(productos,nuevo_producto, nueva_cantidad)

actualizar = input("Desea actualizar la cantidad de un producto? (s/n): ")

if actualizar == 's':
  producto = input("Ingrese el nombre del producto: ")
  cantidad = int(input("Ingrese la nueva cantidad del producto: "))
  actualizar_producto(productos, producto, cantidad)

mostrar_inventario(productos)
