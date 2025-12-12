
class Trabajador:
    def __init__(self, nombre, rut, sueldo_base, activo=True):
        self.nombre = nombre
        self.rut = rut
        self.sueldo_base = sueldo_base
        self.activo = activo 

    def calcular_sueldo_final(self):

        return self.sueldo_base

    def resumen(self):
        estado = "Activo" if self.activo else "Inactivo"
        return f"{self.nombre} - {self.rut} - {estado}"


class Vendedor(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, porcentaje_comision, ventas_mes, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.porcentaje_comision = porcentaje_comision  
        self.ventas_mes = ventas_mes

    def calcular_sueldo_final(self):
        comision = self.ventas_mes * self.porcentaje_comision
        return self.sueldo_base + comision


class Gerente(Trabajador):
    def __init__(self, nombre, rut, sueldo_base, bono_fijo, activo=True):
        super().__init__(nombre, rut, sueldo_base, activo)
        self.bono_fijo = bono_fijo

    def calcular_sueldo_final(self):
        return self.sueldo_base + self.bono_fijo


class Practicante(Trabajador):
    def __init__(self, nombre, rut, valor_hora, horas_trabajadas, activo=True):
        super().__init__(nombre, rut, 0, activo)
        self.valor_hora = valor_hora
        self.horas_trabajadas = horas_trabajadas

    def calcular_sueldo_final(self):
        return self.valor_hora * self.horas_trabajadas


class Empresa:
    def __init__(self, nombre):
        self.nombre = nombre
        self.trabajadores = []

    def agregar_trabajador(self, trabajador):
        self.trabajadores.append(trabajador)

    def listar_todos(self):
        return self.trabajadores

    def listar_activos(self):
        activos = []
        for t in self.trabajadores:
            if t.activo:
                activos.append(t)
        return activos

    def gasto_total_mensual(self):
        total = 0
        for t in self.trabajadores:
            if t.activo:
                total += t.calcular_sueldo_final()
        return total
