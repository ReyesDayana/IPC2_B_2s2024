class Enviar:
    def __init__(self, tienda, cliente, direccion,ordenes, estado):
        self.tienda = tienda
        self.cliente = cliente
        self.direccion = direccion
        self.ordenes = ordenes
        self.estado = estado
        self.next = None
        self.prev = None