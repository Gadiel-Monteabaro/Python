class Matematica:
    PI = 3.14159  # Variable de clase

    @staticmethod
    def suma(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def multiplicación(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b != 0:
            return a / b
        else:
            raise ValueError("No se puede dividir por cero")


print(Matematica.PI)
print(Matematica.suma(5, 3))
print(Matematica.resta(10, 4))
print(Matematica.multiplicación(7, 3))
print(Matematica.division(9, 3))

# Clase estática
"""
_No se puede hederar y no se puede instanciar directamente
_No se necesita crear la instancia de la clase para acceder a sus métodos
"""
