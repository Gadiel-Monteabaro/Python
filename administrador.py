import json
import os

INVENTARIO = 'inventario.json'

# Cargar los productos del inventario
def cargar_inventario():
  if os.path.exists(INVENTARIO):
    with open(INVENTARIO, 'r', encoding="utf-8") as archivo:
      return json.load(archivo)   # convertir el archivo a un diccionario, permitiendo acceder a los datos
  return []

# Guardar los productos en el inventario
def guardar_inventario(productos):
  with open(INVENTARIO, 'w', encoding="utf-8") as archivo:
    json.dump(productos, archivo, indent=2) 

# Agregar un producto al inventario
def agregar_producto(productos, nombre, cantidad):
  for producto in productos:
    if producto['nombre'].lower() == nombre.lower():
      producto['cantidad'] += cantidad
      return
  count = len(productos)
  productos.append({'id': count + 1,'nombre': nombre, 'cantidad': cantidad})
  guardar_inventario(productos)
  
# Actualizar un producto en el inventario
def actualizar_producto(productos, nombre, cantidad):
  for producto in productos:
    if producto['nombre'].lower() == nombre.lower():
      producto['cantidad'] = cantidad
      guardar_inventario(productos)
      print("Producto actualizado.")
      return

# Mostrar el inventario
def mostrar_inventario(productos):
  for producto in productos:
    print(
      f"Producto: {producto['nombre']}, Cantidad: {producto['cantidad']}")
    
def main():
  productos = cargar_inventario()
  
  while True:
    accion = input("Desea agregar un producto (a), actualizar un producto (u), mostrar inventario (m) o salir (s): ")
    
    if accion == 'a':
      nombre = input("Ingrese el nombre del producto: ")
      cantidad = int(input("Ingrese la cantidad del producto: "))
      try:
        agregar_producto(productos, nombre, cantidad)
        print("Producto agregado")
      except ValueError:
        print("Error: La cantidad debe ser un número entero.")

    elif accion == 'u':
      producto = input("Ingrese el nombre del producto: ")
      cantidad = int(input("Ingrese la nueva cantidad del producto: "))
      try:
        actualizar_producto(productos, producto, cantidad)
      except ValueError:
        print("Error: La cantidad debe ser un número entero.")
        
    elif accion == 'm':
      mostrar_inventario(productos)
      
    elif accion == 's':
      print("Programa finalizado.")
      break
    
    else:
      print("Error: Acción no válida.")

# Ejecutar el programa sin importarlo, cuando se importa se ignorará
if __name__ == '__main__':
  main()
