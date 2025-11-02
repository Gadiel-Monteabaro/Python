class Personaje:
    # constructor
    def __init__(self, nombre, vida, poder):
        self.nombre = nombre
        self.vida = vida
        self.poder = poder
        self.daño_base = self.daño()

    def mover(self):
        return f"{self.nombre} se esta moviendo."

    def saltar(self):
        return f"{self.nombre} está saltando."

    def caer(self):
        return f"{self.nombre} ha caído."


class Tirador(Personaje):
    # constructor
    def __init__(self, nombre, vida, poder):
        super().__init__(nombre, vida, poder)
        self.daño_flecha = 2

    def daño(self):
        return self.poder * 1.5

    def lanzar_flecha(self):
        return f"{self.nombre} hizo un daño de {self.daño() * self.daño_flecha}"


class Mago(Personaje):
    # constructor
    def __init__(self, nombre, vida, poder):
        super().__init__(nombre, vida, poder)
        self.daño_meteorito = 1.3

    def meteorito(self):
        return f"{self.nombre} hizo un daño de {self.daño() * self.daño_meteorito}"


tirador = Tirador("Ashe", 100, 25)
print(tirador.lanzar_flecha())
mago = Mago("Skender", 100, 25)
print(mago.meteorito())

"""
Programa basadao en la programación orientada a objetos (POO)

a_ Crear una clase base llamada Personaje
  _atributos - nombre, vida y poder.
  _métodos - mover, saltar y caer.
 
b_ Crear clases derivadas para cada personaje especifico
    _herencia - estas clases heredarán de la clase Personaje
    _atributos - adicionales
    _metodos - lanzar fuego
"""
