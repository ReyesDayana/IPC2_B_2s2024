from Nodo import Nodo
import os
import webbrowser

class Lista:
    def __init__(self):
        self.primero= None
        self.ultimo = None
        self.tamanio = 0
    
    def AgregarNodo(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.valor_unico = self.tamanio
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
        else:
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
        self.ultimo.siguiente = self.primero
    
    def ImprimirLista(self):
        auxiliar : Nodo = self.primero
        while True:
            print(f"Valor: {auxiliar.valor}")
            if auxiliar.siguiente == self.primero:
                break
            auxiliar = auxiliar.siguiente

    def Graficar(self):
        graficar = "digraph G { \n"
        graficar += "node[shape=box] \n"
        graficar += "label= \"Lista circular\" \n"
        auxiliar: Nodo = self.primero
        for nodos in range(self.tamanio):
            nodo = "nodo"+str(auxiliar.valor_unico)
            graficar += nodo +"[label= \"Valor: "+str(auxiliar.valor)+"\"] \n"
            auxiliar = auxiliar.siguiente
        
        aux: Nodo = self.primero
        for i in range(self.tamanio):
            nodo ="nodo"+str(aux.valor_unico)
            nodosiguiente = "nodo"+str(aux.siguiente.valor_unico)
            graficar += "{rank=same; "+ nodo+" -> "+ nodosiguiente+"}\n"
            aux = aux.siguiente
        graficar += "}"
        dot = "circular.txt"
        with open(dot, "w") as grafo:
            grafo.write(graficar)
        result = "cirular.pdf"
        os.system("dot -Tpdf " + dot + " -o " + result)
        webbrowser.open(result)

    def devolvervalor(self, indice):
        auxiliar: Nodo = self.primero
        for i in range(self.tamanio):
            if auxiliar.valor_unico == indice:
                return auxiliar.valor
            auxiliar = auxiliar.siguiente
        return None

lista = Lista()
lista.AgregarNodo(1)
lista.AgregarNodo(2)
lista.AgregarNodo(3)
valor = lista.devolvervalor(0)
print(f"El valor que me devolvio es: {valor}")
lista.ImprimirLista()
lista.Graficar()