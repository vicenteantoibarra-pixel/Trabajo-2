# ejercicio1/clases/vehiculos.py

class Vehiculo:
    def __init__(self, identificador, marca, modelo, anio):
        self.identificador = identificador
        self.marca = marca
        self.modelo = modelo
        self.anio = anio

    def descripcion(self):
        return f"{self.identificador} - {self.marca} {self.modelo} ({self.anio})"

    def consumo(self, km):
        return 0


class Automovil(Vehiculo):
    def __init__(self, identificador, marca, modelo, anio, puertas):
        super().__init__(identificador, marca, modelo, anio)
        self.puertas = puertas

    def consumo(self, km):
        if self.puertas <= 3:
            km_por_litro = 15
        else:
            km_por_litro = 12
        return km / km_por_litro


class Motocicleta(Vehiculo):
    def __init__(self, identificador, marca, modelo, anio, cilindrada):
        super().__init__(identificador, marca, modelo, anio)
        self.cilindrada = cilindrada

    def consumo(self, km):
        if self.cilindrada <= 150:
            km_por_litro = 30
        else:
            km_por_litro = 22
        return km / km_por_litro


class Camion(Vehiculo):
    def __init__(self, identificador, marca, modelo, anio, capacidad_ton):
        super().__init__(identificador, marca, modelo, anio)
        self.capacidad_ton = capacidad_ton

    def consumo(self, km):
        if self.capacidad_ton <= 5:
            km_por_litro = 7
        else:
            km_por_litro = 4
        return km / km_por_litro


class Flota:
    def __init__(self):
        # guardo los vehículos en un diccionario
        self.vehiculos = {}

    def agregar_vehiculo(self, vehiculo):
        if vehiculo.identificador in self.vehiculos:
            print("Ya existe un vehículo con esa patente.")
        else:
            self.vehiculos[vehiculo.identificador] = vehiculo

    def eliminar_vehiculo(self, identificador):
        if identificador in self.vehiculos:
            del self.vehiculos[identificador]

    def buscar_vehiculo(self, identificador):
        return self.vehiculos.get(identificador)

    def listar_vehiculos(self):
        return list(self.vehiculos.values())

    def consumo_total(self, km):
        total = 0
        for v in self.vehiculos.values():
            total += v.consumo(km)
        return total

    def consumos_por_vehiculo(self, km):
        resultado = {}
        for ident, v in self.vehiculos.items():
            resultado[ident] = v.consumo(km)
        return resultado
