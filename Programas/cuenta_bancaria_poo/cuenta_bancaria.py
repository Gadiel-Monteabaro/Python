class CuentaBancaria:

    # constructor
    def __init__(self, nro_cuenta, nombre, apellido, saldo=100000):
        self._nro_cuenta = nro_cuenta
        self._nombre = nombre
        self._apellido = apellido
        self.saldo = saldo

    @property
    def nro_cuenta(self):
        return self._nro_cuenta

    @nro_cuenta.setter
    def nro_cuenta(self, nro_cuenta):
        if not str(nro_cuenta).isdigit() or int(nro_cuenta) <= 0:
            raise ValueError("El número de cuenta debe ser un entero positivo.")
        self._nro_cuenta = nro_cuenta

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = nombre

    @property
    def apellido(self):
        return self._apellido

    @apellido.setter
    def apellido(self, apellido):
        if not apellido:
            raise ValueError("El apellido no puede estar vacío.")
        self._apellido = apellido

    def _validar_deposito(self, monto):
        if monto <= 0:
            raise ValueError("El monto debe ser mayor que cero.")

    def depositar(self, deposito):
        self._validar_deposito(deposito)
        self.saldo += deposito
        return self.saldo

    def extraer(self, deposito):
        self._validar_deposito(deposito)
        if self.saldo - deposito >= 0:
            self.saldo -= deposito
        else:
            print("Saldo insuficiente")

        return self.saldo

    def ver_saldo(self):
        return self.saldo


# menu para simular la app de consola
def menu():
    cuenta_bancaria = CuentaBancaria(
        nro_cuenta=input("Ingrese el número de cuenta: "),
        nombre=input("Ingrese su nombre: "),
        apellido=input("Ingrese su apellido: "),
    )

    while True:
        accion = input(
            "Seleccione una acción: (1) Depositar, (2) Retirar, (3) Ver saldo, (4) Salir: "
        )

        if accion == "1":
            deposito = int(input("Ingrese el monto a depositar: "))
            cuenta_bancaria.depositar(deposito)
            print(f"Depósito realizado. Nuevo saldo: {cuenta_bancaria.ver_saldo()}")

        if accion == "2":
            retiro = int(input("Ingrese el monto a retirar: "))
            cuenta_bancaria.extraer(retiro)
            print(f"Retiro realizado. Nuevo saldo: {cuenta_bancaria.ver_saldo()}")

        if accion == "3":
            print(f"Saldo actual: {cuenta_bancaria.ver_saldo()}")

        if accion == "4":
            print("Saliendo del programa.")
            break


if __name__ == "__main__":
    menu()


"""
Cuenta Bancaria. Crea una clase CuentaBancaria con los siguientes atributos obligatorios numero de cuenta, nombre y apellido. El saldo debe comenzar con 100.000. Agrega e implementa metodos para: 1- depositar ( debe aceptar un valor entero y sumarlo al saldo ), 2- retirar ( debe aceptar un valor entero y restarlo al saldo solo si hay dinero suficiente para retirar en la cuenta ) y 3- ver saldo. Ademas, escribe una app de consola que permita al usuario depositar, retirar o ver saldo hasta que decida detenerse. Al finalizar debera mostrar los datos de la cuenta y el saldo
"""
