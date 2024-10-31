from Nodo import Nodo
import os
import webbrowser

class ListaDoble():
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0
    
    def AgregarValor(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.valor_unico = self.tamanio
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
        else:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
    
    def ImprimirLista(self):
        auxiliar: Nodo = self.cabeza
        for nodos in range(self.tamanio):
            print(f"unico: {auxiliar.valor_unico}, Valor: {auxiliar.valor}")
            auxiliar = auxiliar.siguiente
    
    def Graficar(self):
        graficar = "digraph G { \n"
        graficar += "node[shape=box] \n"
        graficar += "label= \"Lista doblemente enlazada\" \n"
        auxiliar: Nodo = self.cabeza
        for nodos in range(self.tamanio):
            nodo = "nodo"+str(auxiliar.valor_unico)
            graficar+= nodo+"[label=\"Valor :"+str(auxiliar.valor)+" \"]\n"
            auxiliar = auxiliar.siguiente

        aux: Nodo = self.cabeza
        while aux.siguiente is not None:
            nodo = "nodo"+str(aux.valor_unico)
            nodosiguiente = "nodo"+str(aux.siguiente.valor_unico)
            if aux != self.cabeza:
                nodoanterior = "nodo"+str(aux.anterior.valor_unico)
                graficar+= "{rank = same; "+nodo+" -> "+nodosiguiente+"} \n"
                graficar+= "{rank = same; "+nodo+" -> "+nodoanterior+"} \n"
            else:
                graficar+= "{rank = same; "+nodo+" -> "+nodosiguiente+"} \n"
            aux= aux.siguiente
        if aux == self.ultimo:
            nodo = "nodo"+str(aux.valor_unico)
            nodoanterior = "nodo"+str(aux.anterior.valor_unico)
            graficar+= "{rank = same; "+nodo+" -> "+nodoanterior+"} \n"
        graficar += "}"
        dot = "Lista_doble.txt"
        with open(dot, "w")as grafo:
            grafo.write(graficar)
        result =  "Lista_doble.jpg"
        os.system("dot -Tjpg "+ dot + " -o "+ result)
        webbrowser.open(result)

lista = ListaDoble()
lista.AgregarValor(1)
lista.AgregarValor(2)
lista.AgregarValor(3)
lista.AgregarValor(4)
lista.AgregarValor(5)
lista.AgregarValor(6)
lista.ImprimirLista()
lista.Graficar()

