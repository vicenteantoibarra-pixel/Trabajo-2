
from ejercicio4.productoventa import ProductoFisico, ProductoDigital, Carrito


libro = ProductoFisico(
    codigo="P001",
    nombre="Libro Python Básico",
    precio=15000,
    stock=10,
    categoria_envio="liviano"
)

polera = ProductoFisico(
    codigo="P002",
    nombre="Polera Negra Talla M",
    precio=12000,
    stock=5,
    categoria_envio="estandar"
)

curso_online = ProductoDigital(
    codigo="D001",
    nombre="Curso Online POO",
    precio=30000,
    stock=50,  
    licencia_comercial=False
)

licencia_software = ProductoDigital(
    codigo="D002",
    nombre="Licencia Software Pro",
    precio=50000,
    stock=20,
    licencia_comercial=True
)


print("=== Productos disponibles ===")

for p in [libro, polera, curso_online, licencia_software]:
    print(p.descripcion(), "-", p.tipo())


carrito = Carrito()

print("\nAgregando productos al carrito...\n")

carrito.agregar_producto(libro, 2)          
carrito.agregar_producto(polera, 1)         
carrito.agregar_producto(curso_online, 1)   
carrito.agregar_producto(licencia_software, 1)  


carrito.agregar_producto(polera, 10)

print("=== Detalle del carrito ===")
for item in carrito.detalle_items():
     prod = item["producto"]
print(
    f"{prod.nombre} ({prod.tipo()}) - Cantidad: {item['cantidad']} "
    f"- Total producto: ${item['total']}"
    )


subtotal = carrito.subtotal_sin_recargos()
recargos = carrito.total_recargos()
total = carrito.total_general()

print("\nSubtotal sin recargos:", subtotal)
print("Total recargos (envíos/licencias):", recargos)
print("Total general a pagar:", total)


print("\nEliminando producto P001 (libro) del carrito...")
carrito.eliminar_producto("P001")

print("\nDetalle del carrito luego de eliminar:")
for item in carrito.detalle_items():
    prod = item["producto"]

print(
    f"{prod.nombre} ({prod.tipo()}) - Cantidad: {item['cantidad']} "
    f"- Total producto: ${item['total']}"
    )

print("\nStock actual del libro después de eliminar del carrito:", libro.stock)


