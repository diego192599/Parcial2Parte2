class Pedido:
    def __init__(self, nombre_cliente, producto, cantidad, prioridad):
        self.nombre_cliente = nombre_cliente
        self.producto = producto
        self.cantidad = cantidad
        self.prioridad = prioridad

    def __str__(self):
        return f"{self.nombre_cliente};{self.producto};{self.cantidad};{self.prioridad}"


class GestionPedidos:
    def __init__(self):
        self.clientes = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("pedidos.log", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if linea:
                        nombre, producto, cantidad, prioridad = linea.split(";")
                        self.clientes[nombre] = Pedido(
                            producto=producto,
                            cantidad=cantidad,
                            prioridad=prioridad
                        )
            print("Cliente Guardado")
        except FileNotFoundError:
            print("No existe el archivo pedidos.log se creará uno nuevo al guardar.")
        except ValueError:
            print("Error al leer el archivo. Verifique el formato de las líneas.")

    def guardar_clientes(self):
        with open("pedidos.log", "w", encoding="utf-8") as archivo:
            for nombre, dato in self.clientes.items():
                archivo.write(f"{nombre}, {dato.producto}, {dato.cantidad}, {dato.prioridad}")

    def agregar_clientes(self):
        contador = 0
        while True:
            contador += 1
            print("----\n Agregar clientes----")
            nombre = input("Ingrese el nombre del cliente: ")
            producto = input("Ingrese el nombre del producto del clinete: ")
            cantidad = int(input("Ingrese la cantidad de producto que lleva el clinete: "))
            prioridad = int(input("Seleccione una opcion de la cual es el cliente si es (Urgente=1 o Normal=2): "))
            if prioridad == 1:
                print("El producto del cliente es urgente se le colocara mayor prioridad a este pedido ")

            elif prioridad == 2:
                print("El producto del clinete es normal")

            else:
                print("Error no esa opcion no se encuentra disponible")
