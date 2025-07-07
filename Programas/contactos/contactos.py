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


# nuevo_contacto
def nuevo_contacto(nombre, telefono):
    id_contacto = str(uuid.uuid4())
    nuevo_contacto = {
        "id": id_contacto,
        "nombre": nombre.capitalize(),
        "telefono": telefono,
    }

    return nuevo_contacto


# validaciones
def validarInputs(contactos, nombre, telefono):
    if not nombre:
        return "El nombre no puede esta vacío"    
    if not telefono:
        return "El teléfono no puede estar vacío"    
    for contacto in contactos:
        if (
            contacto["nombre"].lower() == nombre.lower()
            or contacto["telefono"] == telefono
        ):
            return "El nombre o número de contacto ya existe"

    return None


# agregar contacto
def agregar_contacto(contactos, nombre, telefono):
    mensaje_error = validarInputs(contactos, nombre, telefono)
    if mensaje_error:
        print(mensaje_error)

    contactos.append(nuevo_contacto(nombre, telefono))
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
            telefono = input("Número de telefono: ")
            agregar_contacto(contactos, nombre, telefono)

        if accion == "d":
            break


if __name__ == "__main__":
    main()
