class Pedido:
    def __init__(self, nombre_cliente, producto, cantidad, prioridad):
        self.nombre_cliente = nombre_cliente
        self.producto = producto
        self.cantidad = cantidad
        self.prioridad = prioridad.upper()

    def __str__(self):
        return f"{self.nombre_cliente};{self.producto};{self.cantidad};{self.prioridad}"


class GestorPedidos:
    def __init__(self, archivo="pedidos.log"):
        self.archivo = archivo
        self.cargar()

    def guardar(self, pedido: Pedido):
        with open(self.archivo, "a", encoding="utf-8") as f:
            f.write(str(pedido) + "\n")

    def cargar(self):
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return f.readlines()
        except FileNotFoundError:
            return []


class Notificador:
    def notificar(self, pedido: Pedido):
        pass


class NotificadorConsola(Notificador):
    def notificar(self, pedido: Pedido):
        if pedido.prioridad == "URGENTE":
            print(f" Pedido URGENTE de {pedido.nombre_cliente}: {pedido.producto} x{pedido.cantidad}")


class SistemaCafeteria:
    def __init__(self):
        self.gestor = GestorPedidos()
        self.notificadores = [NotificadorConsola()]

    def registrar_pedido(self):
        nombre = input("Nombre del cliente: ")
        producto = input("Producto: ")
        cantidad = int(input("Cantidad: "))
        prioridad = input("Prioridad (NORMAL/URGENTE): ")
        pedido = Pedido(nombre, producto, cantidad, prioridad)
        self.gestor.guardar(pedido)
        for notificador in self.notificadores:
            notificador.notificar(pedido)

        print("Pedido registrado.")

    def mostrar_pedidos(self):
        print("\n Lista de pedidos registrados:")
        pedidos = self.gestor.cargar()
        if not pedidos:
            print("No hay pedidos registrados.")
        else:
            for p in pedidos:
                print(p.strip())

class Pago:
    def __init__(self):
        self.metodo = None
        self.detalle = None

    def agregar_pago(self):
        print("\n Métodos de pago disponibles: Tarjeta | Efectivo")
        opcion_pago = input("Ingrese método de pago: ").strip().lower()

        if opcion_pago == "tarjeta":
            self.metodo = "Tarjeta"
            self.detalle = input("Ingrese los primeros 4 dígitos de la tarjeta: ")
        elif opcion_pago == "efectivo":
            self.metodo = "Efectivo"
            self.detalle = float(input("Ingrese la cantidad a pagar: "))
        else:
            print("Método de pago no válido, se registrará como 'Desconocido'")
            self.metodo = "Desconocido"
            self.detalle = ""

        return self


class Menu:
    def __init__(self):
        self.sistema = SistemaCafeteria()

    def mostrar(self):
        while True:
            print("\n---- Menú de Cafetería ----")
            print("1. Registrar Pedido")
            print("2. Ver Pedidos")
            print("3. Salir")

            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.sistema.registrar_pedido()
            elif opcion == "2":
                self.sistema.mostrar_pedidos()
            elif opcion == "3":
                print("Saliendo del sistema...")
                break
            else:
                print(" Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    menu = Menu()
    menu.mostrar()
