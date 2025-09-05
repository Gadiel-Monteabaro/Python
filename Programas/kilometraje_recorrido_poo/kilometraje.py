"""
Kilometraje recorrido. Crea una clase vehiculo que permita llevar el kilometraje recorrido. Agrega atributos para definir color, marca, modelo y patetente del vehiculo y metodos para: 1 - Conducir el auto (debe aceptar la cantidad de kilometros y sumarlo al kilometraje recorrido), 2 - Muestre en pantalla los datos del vehiculo y el correspondiente kilometraje. Ademas, escrribe un app de cosila que permita al usuario conducir varios kilometros y mostrar el kilometraje actual hasta que decidad detenerse. Al finalizar debera mostrar los datos del vehiculo y el kilometraje total recorrido.
"""


class Vehiculo:
    def __init__(self, color, marca, modelo, patente):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.patente = patente
        self._kilometraje = 0

    @property
    def kilometraje(self):
        return self._kilometraje

    @kilometraje.setter
    def kilometraje(self, value):
        if value < 0:
            raise ValueError("El kilometraje no puede ser negativo.")
        self._kilometraje = value
