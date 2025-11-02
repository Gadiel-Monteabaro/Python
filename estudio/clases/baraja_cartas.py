class Carta:
    # constructor
    def __init__(self, palo, valor):
        self._palo = palo
        self._valor = valor

    def __str__(self):
        return f"{self.valor} de {self.palo}"

    def __getitem__(self, clave):
        return f"{self.palo}" if clave == "palo" else f"{self.valor}"

    @property
    def valor(self):
        return f"{self._valor}"

    @property
    def palo(self):
        return f"{self._palo}"


carta = Carta("Copa", "9")
print(carta.__getitem__("valor"))
print(carta.valor)
print(carta.palo)

"""
  Baraja de cartas, Crea una clase Carta que represente una carta de la baraja. Implementa los métodos __str__ y __getitem__ para mostrar la carta y acceder a sus atributos ( ejemplo palo y valor )
"""
