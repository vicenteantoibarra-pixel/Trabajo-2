
from ejercicio2.gestorempleados import Vendedor, Gerente, Practicante, Empresa


empresa = Empresa("Mi Empresa S.A.")

vendedor1 = Vendedor(
    nombre="Juan Pérez",
    rut="11.111.111-1",
    sueldo_base=500000,
    porcentaje_comision=0.05, 
    ventas_mes=2000000
)

gerente1 = Gerente(
    nombre="María López",
    rut="22.222.222-2",
    sueldo_base=1000000,
    bono_fijo=300000
)

practicante1 = Practicante(
    nombre="Pedro Soto",
    rut="33.333.333-3",
    valor_hora=4000,
    horas_trabajadas=80
)
vendedor2 = Vendedor(
nombre="Ana Díaz",
rut="44.444.444-4",
sueldo_base=450000,
porcentaje_comision=0.03,
ventas_mes=1000000,
activo=False
)

empresa.agregar_trabajador(vendedor1)
empresa.agregar_trabajador(gerente1)
empresa.agregar_trabajador(practicante1)
empresa.agregar_trabajador(vendedor2)


print("=== Trabajadores registrados (todos) ===")
for t in empresa.listar_todos():
    print(t.resumen())

print("\n=== Trabajadores activos y sueldo final del mes ===")
for t in empresa.listar_activos():
    sueldo_final = t.calcular_sueldo_final()
    tipo = type(t).__name__
    print(f"{t.nombre} ({tipo}) -> Sueldo final: {sueldo_final}")


total = empresa.gasto_total_mensual()
print("\nGasto total mensual en sueldos (solo activos):", total)


