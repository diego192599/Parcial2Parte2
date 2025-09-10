class Pedido:
    def __init__(self, nombre_cliente, producto, cantidad, prioridad):
        self.nombre_cliente = nombre_cliente
        self.producto = producto
        self.cantidad = cantidad
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre_cliente};{self.producto};{self.cantidad};{self.prioridad}"


class GestorPedidos:
    def __init__(self, archivo="pedidos.log"):
        self.archivo = archivo

    def guardar(self, pedido):
        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(str(pedido) + "\n")


class Notificador:
    def notificar(self, pedido):
        if pedido.prioridad.upper() == "URGENTE":
            print(f"Pedido URGENTE de {pedido.nombre_cliente}: {pedido.producto} x{pedido.cantidad}")


class SistemaCafeteria:
    def __init__(self):
        self.gestor = GestorPedidos()
        self.notificador = Notificador()

    def registrar_pedido(self):
        nombre = input("Nombre del cliente: ")
        producto = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        prioridad = input("Prioridad (NORMAL/URGENTE): ").upper()

        pedido = Pedido(nombre, producto, cantidad, prioridad)
        self.gestor.guardar(pedido)
        self.notificador.notificar(pedido)
        print("Pedido registrado.")
