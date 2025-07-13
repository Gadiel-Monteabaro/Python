class Contacto:
    # constructor
    def __init__(self, nombre, apellido, telefono):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

    def __str__(self):
        return f"Nombre: {self.nombre} \nApellido: {self.apellido} \nTelefono: {self.telefono}"

    def __setitem__(self, key, value):
        if key == "nombre":
            self.nombre = value
        elif key == "apellido":
            self.apellido = value
        elif key == "telefono":
            self.telefono = value
        else:
            raise "Clave inválida"


contacto = Contacto("Gadiel", "Silva", "3518053549")
print(contacto)
contacto.__setitem__("telefono", "3518053559")
print(contacto)
contacto.__setitem__("apellido", "Monteabaro")
print(contacto)

"""
  Agenda de contactos, Crea una clase contacto que almacene informacion sobre personas en una agenda, implementar __str__ y __setitem__ para mostrar detalles y modificar atributos.
"""
