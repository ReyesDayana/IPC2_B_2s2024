from NodoTienda import Tienda
import os
import webbrowser


class ListaTienda:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

    def agregarTienda(self, tienda, zona, lista_envios):
        nueva_tienda = Tienda(tienda, zona)
        nueva_tienda.envio = lista_envios
        if self.cabeza is None:
            self.cabeza = nueva_tienda
            self.ultimo = nueva_tienda
            self.ultimo.next = nueva_tienda
            self.tamanio += 1
        else:
            self.ultimo.next = nueva_tienda
            self.ultimo = nueva_tienda
            self.ultimo.next = self.cabeza
            self.tamanio += 1

    def imprimirTiendas(self):
        auxiliar: Tienda = self.cabeza
        while True:
            print(f"--------Tienda: {auxiliar.tienda}, Zona: {auxiliar.zona}")
            aux = auxiliar.envio.cabeza
            for i in range(auxiliar.envio.tamanio):
                print(f"\tCliente: {aux.cliente}, Direccion: {aux.direccion}, Estado: {aux.estado}")
                aux = aux.next
            if auxiliar.next == self.cabeza:
                break
            auxiliar = auxiliar.next

    def Graficar(self):
        contador = 0
        contador2 = 0
        graficar = "digraph G { \n"
        graficar += "node[shape=box] \n"
        graficar += "label= \"Tiendas y Envios\" \n"
        auxiliar: Tienda = self.cabeza
        for envio in range(self.tamanio):
            nodotienda = "tienda" + str(contador)
            contador += 1
            graficar += nodotienda + "[label=\"Tienda: " + auxiliar.tienda + "\nZona: " + auxiliar.zona + "\"] \n"
            temp = auxiliar.envio.cabeza
            for i in range(auxiliar.envio.tamanio):
                nodoenvio = "envio" + str(contador2)
                contador2 += 1
                graficar += nodoenvio + "[label=\"Cliente: " + temp.cliente + "\nDireccion: " + temp.direccion + "\"] \n"
                temp = temp.next
            auxiliar = auxiliar.next

        aux: Tienda = self.cabeza
        contador = 0
        contador2 = 0

        for i in range(self.tamanio):
            nodotienda = "tienda" + str(contador)
            contadorsiguiente = contador + 1
            nodosiguientetarea = "tienda" + str(contadorsiguiente)
            if aux != self.ultimo:
                graficar += "{rank=same; " + nodotienda + " -> " + nodosiguientetarea + "}\n"
            contador += 1
            temp = aux.envio.cabeza
            for j in range(aux.envio.tamanio):
                nodoenvio = "envio" + str(contador2)
                contadorsiguiente = contador2 + 1
                nodosiguienteenvio = "envio" + str(contadorsiguiente)
                if temp == aux.envio.cabeza:
                    graficar += "{ " + nodotienda +  " -> " + nodoenvio + "} \n"
                    graficar += "{ " + nodoenvio +  " -> " + nodosiguienteenvio + "}\n"
                else:
                    if temp != aux.envio.ultimo:
                        graficar += "{ " + nodoenvio + " -> " + nodosiguienteenvio + "}\n"
                temp = temp.next
                contador2 += 1
            aux = aux.next
        graficar += "}"
        dot = "tiendas.txt"
        with open(dot, "w") as grafo:
            grafo.write(graficar)
        result = "tiendas.pdf"
        os.system("dot -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)
