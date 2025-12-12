# ejercicio4/clases/productos.py

class Producto:
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock 

    def tipo(self):

        return "Genérico"

    def calcular_total(self, cantidad):
        return self.precio * cantidad

    def descripcion(self):
        return f"{self.codigo} - {self.nombre} - ${self.precio} (stock: {self.stock})"


class ProductoFisico(Producto):
    def __init__(self, codigo, nombre, precio, stock, categoria_envio):
        super().__init__(codigo, nombre, precio, stock)
        self.categoria_envio = categoria_envio

    def tipo(self):
        return "Físico"

    def calcular_total(self, cantidad):
        base = self.precio * cantidad

        if self.categoria_envio == "liviano":
            costo_envio = 2000
        elif self.categoria_envio == "estandar":
            costo_envio = 4000
        else: 
            costo_envio = 7000

        return base + costo_envio


class ProductoDigital(Producto):
    def __init__(self, codigo, nombre, precio, stock, licencia_comercial):
        super().__init__(codigo, nombre, precio, stock)
        self.licencia_comercial = licencia_comercial  

    def tipo(self):
        return "Digital"

    def calcular_total(self, cantidad):
        base = self.precio * cantidad

        if self.licencia_comercial:
            recargo = base * 0.20
        else:
            recargo = 0

        return base + recargo


class Carrito:
    def __init__(self):
        self.items = []

    def agregar_producto(self, producto, cantidad):
        if cantidad <= 0:
            print("La cantidad debe ser mayor a 0.")
            return

        if cantidad > producto.stock:
            print("No hay stock suficiente para agregar este producto.")
            return

        base = producto.precio * cantidad
        total = producto.calcular_total(cantidad)

        producto.stock -= cantidad

        self.items.append({
            "producto": producto,
            "cantidad": cantidad,
            "base": base,
            "total": total
        })

    def eliminar_producto(self, codigo):
        for item in self.items:
            if item["producto"].codigo == codigo:
                prod = item["producto"]
                prod.stock += item["cantidad"]
                self.items.remove(item)
                break

    def detalle_items(self):
        return self.items

    def subtotal_sin_recargos(self):
        subtotal = 0
        for item in self.items:
            subtotal += item["base"]
        return subtotal

    def total_recargos(self):
        recargos = 0
        for item in self.items:
            recargos += (item["total"] - item["base"])
        return recargos

    def total_general(self):
        total = 0
        for item in self.items:
            total += item["total"]
        return total
