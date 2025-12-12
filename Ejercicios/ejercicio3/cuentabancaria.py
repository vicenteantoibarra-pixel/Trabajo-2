
class CuentaBancaria:
    def __init__(self, numero, titular, saldo_inicial, tipo_cuenta):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo_inicial
        self.tipo_cuenta = tipo_cuenta
        self.movimientos = []  

    def deposito(self, monto):
        if monto <= 0:
            print("Monto de depósito no válido.")
            return
        self.saldo += monto
        self.movimientos.append(f"DEPÓSITO {monto}")

    def retiro(self, monto):
        return False

    def mostrar_info(self):
        return f"Cuenta {self.numero} - {self.titular} - {self.tipo_cuenta} - Saldo: {self.saldo}"

    def historial_movimientos(self):
        return self.movimientos


class CuentaCorriente(CuentaBancaria):
    def __init__(self, numero, titular, saldo_inicial, linea_credito):
        super().__init__(numero, titular, saldo_inicial, "Cuenta Corriente")
        self.linea_credito = linea_credito

    def retiro(self, monto):
        if monto <= 0:
            print("Monto de retiro no válido.")
            return False

        if self.saldo - monto < -self.linea_credito:
            print("No se puede realizar el retiro, supera la línea de crédito.")
            return False

        self.saldo -= monto
        self.movimientos.append(f"RETIRO {monto}")
        return True


class CuentaAhorro(CuentaBancaria):
    def __init__(self, numero, titular, saldo_inicial, tasa_interes):
        super().__init__(numero, titular, saldo_inicial, "Cuenta de Ahorro")
        self.tasa_interes = tasa_interes  

    def retiro(self, monto):
        if monto <= 0:
            print("Monto de retiro no válido.")
            return False

        if monto > self.saldo:
            print("No hay saldo suficiente para el retiro.")
            return False

        self.saldo -= monto
        self.movimientos.append(f"RETIRO {monto}")
        return True

    def aplicar_interes(self):
        interes = self.saldo * self.tasa_interes
        self.saldo += interes
        self.movimientos.append(f"INTERÉS {round(interes, 2)}")


class Banco:
    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregar_cuenta(self, cuenta):
        if self.buscar_cuenta(cuenta.numero) is not None:
            print("Ya existe una cuenta con ese número.")
        else:
            self.cuentas.append(cuenta)

    def buscar_cuenta(self, numero):
        for c in self.cuentas:
            if c.numero == numero:
                return c
        return None

    def existe_cuenta(self, numero):
        return self.buscar_cuenta(numero) is not None

    def saldo_total(self):
        total = 0
        for c in self.cuentas:
            total += c.saldo
        return total

    def listar_cuentas(self):
        return self.cuentas
