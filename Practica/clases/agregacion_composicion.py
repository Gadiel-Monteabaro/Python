class Motor:
    def __init__(self, potencia):
        self.potencia = potencia

    def girar(self):
        return f"Girando motor de {self.potencia} vatios."


# Composición
# Un objeto compuesto por otros objetos más pequeños
# _todo contiene mas objetos _parte, su ciclo de vida esta controlado por _todo
class BrazoRobotico:
    def __init__(self, longitud):
        self.longitud = longitud
        self.motor = Motor(100)  # Composición

    def mover(self):
        self.motor.girar()
        return f"Brazo de {self.longitud}cm se mueve."


class Herramienta:
    def __init__(self, nombre):
        self.nombre = nombre

    def usar(self):
        return f"Usando {self.nombre}"


# Agregación
# _todo tiene referencia a otros objetos _parte
# _parte pueden existir, independiente de _todo
class Robot:
    def __init__(self, nombre):
        self.nombre = nombre
        self.brazo = BrazoRobotico(50)  # Composición
        self.herramientas = []  # Agregación

    def agregar_herramienta(self, herramienta):
        self.herramientas.append(herramienta)

    def trabajar(self):
        self.brazo.mover()
        for herramienta in self.herramientas:
            print(herramienta.usar())
        return f"{self.nombre} está trabajando."


destornillador = Herramienta("destornillador")
tornillo = Herramienta("tornillo")

robot = Robot("Gadiel")
robot.agregar_herramienta(destornillador)
robot.agregar_herramienta(tornillo)

print(robot.trabajar())
