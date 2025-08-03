class Rectangulo:
    def __init__(self, largo, ancho):
        self._largo = largo
        self._ancho = ancho

    @property
    def largo(self):
        return self._largo

    @largo.setter
    def largo(self, largo):
        if largo <= 0:
            raise ValueError("El largo debe ser mayor a cero")
        self._largo = largo

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        if ancho <= 0:
            raise ValueError("El ancho debe ser mayor a cero")
        self._largo = ancho

    def area(self):
        return self._ancho * self._largo

    def perimetro(self):
        return 2 * (self._largo + self._ancho)


def main():
    while True:
        accion = input("Calcular Área (a), Calcular Perímetro (p), salir(s) ")

        if accion == "a":
            largo = int(input("Largo del rectacngulo: "))
            ancho = int(input("Ancho del rectacngulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print(rectangulo.area())

        if accion == "p":
            largo = int(input("Largo del rectacngulo: "))
            ancho = int(input("Ancho del rectacngulo: "))
            rectangulo = Rectangulo(largo, ancho)
            print(rectangulo.perimetro())

        if accion == "s":
            break


if __name__ == "__main__":
    main()
