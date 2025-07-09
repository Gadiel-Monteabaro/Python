class Personaje:
    # constructor
    def __init__(self, nombre, vidas):
        self.nombre = nombre
        self.vidas = vidas

    # suma
    def __add__(self, cantidad):
        nueva_vida = self.vidas + cantidad
        return Personaje(self.nombre, nueva_vida)

    # resta
    def __sub__(self, cantidad):
        self.vidas -= cantidad
        return Personaje(self.nombre, self.vidas)


# Inmutabilidad
# No tocar self, trabajar con copias y devolver nuevos valores
if __name__ == "__main__":
    heroe = Personaje("Guerrero", 100)
    heroe_mejorado = heroe + 10
    heroe_debil = heroe - 10
    print(f"Nombre:{heroe_mejorado.nombre} Vida:{heroe_mejorado.vidas}")
    print(f"Nombre:{heroe.nombre} Vida:{heroe.vidas}")
    print(f"Nombre:{heroe_debil.nombre} Vida:{heroe_debil.vidas}")
