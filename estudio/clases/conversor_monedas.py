class Moneda:
    codigos = {"ARS": 1200.0, "USD": 1.0, "EUR": 0.92}

    def __init__(self, cantidad, tipo):
        self.cantidad = cantidad
        self.tipo = tipo

    def convertir(self, codigo):
        cantidad_a_dolares = self.cantidad / self.codigos[self.tipo]
        cantidad_convertida = cantidad_a_dolares * self.codigos[codigo]
        return cantidad_convertida

    def __add__(self, other):
        cantidad_usd = self.cantidad / self.codigos[self.tipo]
        cantidad_other = other.cantidad / self.codigos[other.tipo]
        suma = cantidad_usd + cantidad_other
        return Moneda(suma, "USD")

    def __str__(self):
        return f"Total {self.cantidad:.2f} {self.tipo}"


if __name__ == "__main__":
    dinero1 = Moneda(920, "ARS")
    dolares = dinero1.convertir("USD")
    print(f"{dinero1.cantidad} {dinero1.tipo} son {dolares:.2f} USD")
    dinero2 = Moneda(920, "USD")
    pesos = dinero2.convertir("ARS")
    print(f"{dinero2.cantidad} {dinero2.tipo} son {pesos:.2f} ARS")

    suma = dinero1 + dinero2
    print(suma)
