class Moneda:
    codigos = {"ARS": 1200.0, "USD": 1.0, "EUR": 0.92}

    def __init__(self, cantidad, tipo):
        self.cantidad = cantidad
        self.tipo = tipo

    def convertir(self, codigo):
        cantidad_a_dolares = self.cantidad / self.codigos[self.tipo]
        cantidad_convertida = cantidad_a_dolares * self.codigos[codigo]
        return cantidad_convertida


if __name__ == "__main__":
    dinero = Moneda(920, "ARS")
    dolares = dinero.convertir("USD")
    print(f"{dinero.cantidad} {dinero.tipo} son {dolares:.2f} USD")
    dinero = Moneda(920, "USD")
    pesos = dinero.convertir("ARS")
    print(f"{dinero.cantidad} {dinero.tipo} son {pesos:.2f} ARS")
