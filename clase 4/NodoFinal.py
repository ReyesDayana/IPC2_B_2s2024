class Enviar:
    def __init__(self, tienda, cliente, ordenes, estado):
        self.tienda = tienda
        self.cliente = cliente
        self.ordenes = ordenes
        self.estado = estado
        self.next = None
        self.prev = None