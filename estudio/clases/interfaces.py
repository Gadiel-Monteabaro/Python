# Interfaces
"""
_Un contrato que define el conjunto de metodos que las clases deben cumplir
"""

# Interface Informal
"""
_clases con métodos definidos pero no implementados
"""


class Forma:
    def calcular_area(self):  # Interface informal
        pass


class Circulo(Forma):
    # constructor
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return 3.14 * self.radio**2


class Rectangulo(Forma):
    # constructor
    def __init__(self, ancho, alto):
        self.ancho = ancho
        self.alto = alto

    def calcular_area(self):
        return self.alto * self.ancho


def calcular_total(formas):
    total = 0
    for forma in formas:
        total += forma.calcular_area()
    return total


formas = [Circulo(6), Rectangulo(16, 8)]

total = calcular_total(formas)
print(total)


# Interface formal
"""
_Usando el modulo ABC (Abstract Base Classes)
_una forma de crear interfaces a través de metaclases
_cualquier clase debe implementar calcular_area, sino no se puede instanciar
"""

from abc import ABC, abstractmethod


class Forma(ABC):
    @abstractmethod
    def calcular_area(self):
        pass
