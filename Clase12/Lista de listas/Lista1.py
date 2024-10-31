from NodoLista1 import Nodouno
from Lista2 import Lista
import os
import webbrowser


class ListaTiendas:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

    def agregarNombre(self, nombres, valores):
        nueva_tienda = Nodouno(nombres, valores)
        if self.cabeza is None:
            self.cabeza = nueva_tienda
            self.ultimo = nueva_tienda
            self.tamanio += 1
        else:
            self.ultimo.next = nueva_tienda
            self.ultimo = nueva_tienda
            self.tamanio += 1

    def imprimirTiendas(self):
        current: Nodouno = self.cabeza
        for i in range(self.tamanio):
            print(f"-------Nombre: {current.nombre}---------------")
            aux = current.valores.cabeza
            for i in range(current.valores.tamanio):
                print(f"Valor:  {aux.valor}")
                aux = aux.next
            current = current.next

    def Graficar(self):
        contador=0
        contador2=0
        graficar = "digraph G { \n"
        graficar += "node[shape=box] \n"
        graficar += "label= \"Lista de listas\" \n"
        auxiliar: Nodouno = self.cabeza
        for nodos in range(self.tamanio):
            nodo = "principal" + str(contador)
            contador += 1
            graficar += nodo + "[label=\"nombre: "+auxiliar.nombre+ " \"] \n"
            temp = auxiliar.valores.cabeza
            for i in range(auxiliar.valores.tamanio):
                nodovalor = "valor"+str(contador2)
                contador2 += 1
                graficar += nodovalor + "[label=\"Valor: " + str(temp.valor) + " \"] \n"
                temp = temp.next
            auxiliar = auxiliar.next

        aux: Nodouno = self.cabeza
        contador = 0
        contador2 = 0
        for i in range(self.tamanio):
            nodo = "principal" + str(contador)
            contadorsiguiente = contador + 1
            nodosiguiente = "principal" + str(contadorsiguiente)
            if aux != self.ultimo:
                graficar += "{rank=same; " + nodo + " ->" + nodosiguiente + "}\n"
            contador += 1
            temp = aux.valores.cabeza
            for i in range(aux.valores.tamanio):
                nodoenvio = "valor"+str(contador2)
                contadorsiguiente = contador2 + 1
                nodosiguienteenvio = "valor" + str(contadorsiguiente)
                if temp == aux.valores.cabeza:
                    graficar += "{ " + nodo + " ->" + nodoenvio + "}\n"
                    graficar += "{ " + nodoenvio + " ->" + nodosiguienteenvio + "}\n"
                else:
                    if temp != aux.valores.ultimo:
                        graficar += "{ " + nodoenvio + " ->" + nodosiguienteenvio + "}\n"
                temp = temp.next
                contador2 += 1
            aux = aux.next
        graficar += "}"
        dot = "listadelistas.txt"
        with open(dot, 'w') as grafo:
            grafo.write(graficar)
        result = "listadelistas.pdf"
        os.system("dot -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)

listaprincipal = ListaTiendas()
listasecundaria = Lista()

listasecundaria.AgregarNodo(1)
listasecundaria.AgregarNodo(2)
listasecundaria.AgregarNodo(3)
listasecundaria.AgregarNodo(4)

listaprincipal.agregarNombre("numeros", listasecundaria)

listasecundaria2  = Lista()
listasecundaria2.AgregarNodo(5)
listasecundaria2.AgregarNodo(6)
listasecundaria2.AgregarNodo(7)
listasecundaria2.AgregarNodo(8)
listaprincipal.agregarNombre("mas numeros", listasecundaria2)

listaprincipal.imprimirTiendas()
listaprincipal.Graficar()