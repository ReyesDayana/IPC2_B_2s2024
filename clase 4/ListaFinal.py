from NodoFinal import Enviar
import os
import webbrowser

class ListaFinal:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

    def Agregar(self, tienda, cliente,direccion, ordenes, estado):
        nuevo_enviar = Enviar(tienda, cliente,direccion, ordenes, estado)
        if self.cabeza == None:
            self.cabeza = nuevo_enviar
            self.ultimo = nuevo_enviar
            self.tamanio += 1
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

    def GraficarLista(self):
        contador = 0
        graficar = "digraph G { \n"
        graficar += "node[shape=box] \n"
        graficar += "label= \"Envios finales\" \n"
        auxiliar: Enviar = self.cabeza
        for envio in range(self.tamanio):
            nodoenvio = "envio" + str(contador)
            contador += 1
            graficar += nodoenvio + "[label=\"Tienda: " + auxiliar.tienda + " \nCliente: " + auxiliar.cliente + "\n Direccion: " + auxiliar.direccion + "\n Numero de ordenes: " + str(
                auxiliar.ordenes) + " \"] \n"
            auxiliar = auxiliar.next

        aux: Enviar = self.cabeza
        contador = 0
        while aux.next is not None:
            nodoenvio = "envio" + str(contador)
            contadoranterior = contador - 1
            contadorsiguiente = contador + 1
            nodosiguienteenvio = "envio" + str(contadorsiguiente)
            nodoanteriortenvio = "envio" + str(contadoranterior)
            if aux == self.cabeza:
                graficar += "{rank=same; " + nodoenvio + " ->" + nodosiguienteenvio + "}\n";
            else:
                graficar += "{rank=same; " + nodoenvio + " ->" + nodosiguienteenvio + "}\n";
                graficar += "{rank=same; " + nodoenvio + " ->" + nodoanteriortenvio + "}\n";
            aux = aux.next
            contador += 1

        graficar += "}"
        dot = "envios.txt"
        with open(dot, 'w') as grafo:
            grafo.write(graficar)
        result = "envios.pdf"
        os.system("dot -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)