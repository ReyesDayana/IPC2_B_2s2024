from NodoFinal import Enviar

class ListaFinal:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

    def Agregar(self, tienda, cliente, ordenes, estado):
        nuevo_enviar = Enviar(tienda, cliente, ordenes, estado)
        if self.cabeza == None:
            self.cabeza = nuevo_enviar
            self.ultimo = nuevo_enviar
            self.tamanio = 0
        else:
            nuevo_enviar.prev = self.ultimo
            self.ultimo.next = nuevo_enviar
            self.ultimo = nuevo_enviar
            self.tamanio += 1

    def ImprimirLista(self):
        auxiliar: Enviar = self.cabeza
        for i in range(self.tamanio):
            print(f"Tienda: {auxiliar.tienda}, Cliente: {auxiliar.cliente}, numero de ordenes: {auxiliar.ordenes}")
            auxiliar = auxiliar.next