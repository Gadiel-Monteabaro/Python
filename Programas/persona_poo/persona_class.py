class Persona:
    # constructor
    def __init__(self, nombre="", edad=0, dni=""):
        self._nombre = nombre
        self._edad = edad
        self._dni = dni

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, edad):
        self._edad = edad

    @property
    def dni(self):
        return self._dni

    @dni.setter
    def dni(self, dni):
        self._dni = dni

    def mostrar(self):
        print(f"nombre: {self.nombre}")
        print(f"edad: {self.edad} años")
        print(f"dni: {self.dni}")

    def esMayorDeEdad(self):
        return self.edad >= 18


def main():
    print("Crear Persona")
    nombre = input("Ingrese su nombre: ")
    edad = int(input("Ingrese su edad: "))
    dni = input("Ingrese su dni: ")

    persona = Persona(nombre, edad, dni)
    persona.mostrar()

    if persona.esMayorDeEdad():
        print("Es mayor de edad")
    else:
        print("No es mayor de edad")


if __name__ == "__main__":
    main()
