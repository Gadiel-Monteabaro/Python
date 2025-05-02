"""
Escribe un programa que tenga un menú para gestionar una lista de contactos:
        a. Agregar Contacto
        b. Eliminar Contacto
        c. Mostrar Contacto
        d. Salir
"""

import os
import json
import uuid

CONTACTOS = os.path.join(os.path.dirname(__file__), "contacto.json")


# cargar contactos
def cargar_contactos():
    if os.path.exists(CONTACTOS):
        try:
            with open(CONTACTOS, "r", encoding="utf-8") as archivo:
                return json.load(archivo)  # pasar de json a diccionario
        except (json.JSONDecodeError, TypeError) as error:
            print(f"Error al cargar los contactos: {error}")
    return []


# guardar contactos
def guardar_contactos(contactos):
    if os.path.exists(CONTACTOS):
        try:
            with open(CONTACTOS, "w", encoding="utf-8") as archivo:
                json.dump(contactos, archivo, indent=2)  # pasar de diccionario a json
        except (json.JSONDecodeError, TypeError) as error:
            print(f"Error al cargar los contactos: {error}")


# agregar contacto
def agregar_contacto(contactos, nombre, telefono):
    for contacto in contactos:
        if contacto["nombre"].lower() == nombre.lower():
            print("El contacto ya ha sido agregado")
            return

    id_contacto = str(uuid.uuid4())
    nuevo_contacto = {
        "id": id_contacto,
        "nombre": nombre.capitalize(),
        "telefono": telefono,
    }
    contactos.append(nuevo_contacto)

    guardar_contactos(contactos)
    print("El contacto fue agregado correctamente")


def main():
    contactos = cargar_contactos()

    while True:
        accion = input(
            "Desea agregar un contacto (a), mostrar contacto (b), eliminar contacto (c) o salir (d):"
        )

        if accion == "a":
            nombre = input("Nombre del contacto: ")
            if not nombre:
                print("Ingresar nombre del contacto")
                continue
            telefono = input("Número de telefono: ")
            if not telefono:
                print("Ingresar número del contacto")
                continue
            agregar_contacto(contactos, nombre, telefono)


if __name__ == "__main__":
    main()
