from NodoEnvio import Envio

class ListaEnvios:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

    def AgregarEnvio(self,  cliente, estado, direccion):
        nuevo_envio = Envio(cliente, estado, direccion)
        if self.cabeza == None:
            self.cabeza = nuevo_envio
            self.ultimo = nuevo_envio
            self.tamanio += 1
        else:
            self.ultimo.next = nuevo_envio
            self.ultimo = nuevo_envio
            self.tamanio += 1


    def ImprimirLista(self):
        auxiliar: Envio = self.cabeza
        for envio in range(self.tamanio):
            print(f"Cliente: {auxiliar.cliente}, Direccion: {auxiliar.direccion}, Estado: {auxiliar.estado}")
            auxiliar = auxiliar.next