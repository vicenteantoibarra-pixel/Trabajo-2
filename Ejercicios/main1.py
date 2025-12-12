
from ejercicio1.flotavehiculos import Automovil, Motocicleta, Camion, Flota

flota = Flota()

auto1 = Automovil("AA11", "Toyota", "Yaris", 2020, 4)
moto1 = Motocicleta("BB22", "Honda", "CG", 2021, 150)
camion1 = Camion("CC33", "Mercedes", "1114", 2015, 8)

flota.agregar_vehiculo(auto1)
flota.agregar_vehiculo(moto1)
flota.agregar_vehiculo(camion1)

print("=== Vehículos en la flota ===")
for v in flota.listar_vehiculos():
    print(v.descripcion())

km = 150
print("\n=== Consumo estimado para", km, "km ===")
consumos = flota.consumos_por_vehiculo(km)

for ident, litros in consumos.items():
    v = flota.buscar_vehiculo(ident)
    print(v.descripcion(), "->", round(litros, 2), "litros")

    total = flota.consumo_total(km)
    print("\nConsumo total de la flota:", round(total, 2), "litros")

    print("\nEliminando vehículo AA11...")
    flota.eliminar_vehiculo("AA11")

    print("Vehículos restantes:")
    for v in flota.listar_vehiculos():
        print(v.descripcion())
