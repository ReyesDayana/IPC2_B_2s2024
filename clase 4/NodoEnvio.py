class Envio:
    def __init__(self, cliente, estado, direccion):
        self.cliente = cliente
        self.estado = estado
        self.direccion = direccion
        self.next = None