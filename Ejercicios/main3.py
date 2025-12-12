
from ejercicio3.cuentabancaria import CuentaCorriente, CuentaAhorro,Banco

banco = Banco("Banco Ejemplo")

cc1 = CuentaCorriente("1001", "Juan Pérez", 200000, linea_credito=100000)
cc2 = CuentaCorriente("1002", "Ana Díaz", 50000, linea_credito=50000)

ca1 = CuentaAhorro("2001", "María López", 300000, tasa_interes=0.01) 
ca2 = CuentaAhorro("2002", "Pedro Soto", 100000, tasa_interes=0.015)  

banco.agregar_cuenta(cc1)
banco.agregar_cuenta(cc2)
banco.agregar_cuenta(ca1)
banco.agregar_cuenta(ca2)


cc1.deposito(50000)
cc1.retiro(100000)   
cc1.retiro(300000)   

ca1.deposito(20000)
ca1.retiro(50000)    
ca1.retiro(500000)   

    
ca1.aplicar_interes()
ca2.aplicar_interes()

print("=== Cuentas del banco ===")
for c in banco.listar_cuentas():
    print(c.mostrar_info())

   
numero_buscar = "2001"
cuenta = banco.buscar_cuenta(numero_buscar)

if cuenta is not None:
    print("\n=== Historial de movimientos de la cuenta", numero_buscar, "===")
    for mov in cuenta.historial_movimientos():
            print(mov)
    else:
        print("La cuenta no existe.")

   
total = banco.saldo_total()
print("\nSaldo total administrado por el banco:", total)