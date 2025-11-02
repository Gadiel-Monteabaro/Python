class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # atributo privado
        self._edad = edad  # atributo protegido

    def __str__(self):
        return f"Nombre: {self.__nombre} \nEdad: {self._edad}"

    @property  # decorador getter
    def nombre(self):
        return self.__nombre

    @nombre.setter  # decorador setter
    def nombre(self, nombre):
        self.__nombre = nombre

    @property  # decorador getter
    def edad(self):
        return self._edad

    @edad.setter  # decorador setter
    def edad(self, edad):
        self._edad = edad


# instancia
persona = Persona("Gadiel", "28")
print(persona)

# setters
persona.nombre = "Monteabaro"
persona.edad = "30"
print(persona)
