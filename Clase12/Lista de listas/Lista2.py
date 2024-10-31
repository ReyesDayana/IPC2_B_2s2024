from NodoLista2 import Nododos
import os
import webbrowser
from graphviz import Digraph

class Lista:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0
    def AgregarNodo(self, valor):
    
        nuevo_nodo = Nododos(valor)
       
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio += 1
        else:
            self.ultimo.next = nuevo_nodo
            self.ultimo = nuevo_nodo
            self.tamanio +=1
    
    def ImprimirLista(self):
        auxiliar = self.cabeza
        for i in range(self.tamanio):
            print(f"Valor:{auxiliar.valor} ")
            auxiliar = auxiliar.next
    
    def Graficar(self):
        graficarlista = "digraph G{ \n"
        graficarlista += "node[shape=box] \n"
        graficarlista += "label= \"Lista Simple\" \n"
        auxiliar: Nododos = self.cabeza
        for nodos in range(self.tamanio):
            nodo = "nodo"+str(auxiliar.valor)
            graficarlista += nodo + "[label = \"Valor: "+str(auxiliar.valor)+"\"]\n"
            auxiliar = auxiliar.next
        
        aux: Nododos = self.cabeza
        while aux.next is not None:
            nodo = "nodo"+str(aux.valor)
            nodonext = "nodo"+str(aux.next.valor)
            graficarlista += "{rank=same; " +nodo+ "->"+nodonext+"}\n"
            aux = aux.next
        graficarlista += "}"
        dot ="Nodos.txt"
        with open(dot, 'w') as grafo:
            grafo.write(graficarlista)
        result = "Nodos.pdf"
        os.system("dot -Tpdf "+dot+" -o "+result)
        webbrowser.open(result)
    
    def GraficarLista(self):
        dot = Digraph()
        auxliar: Nododos = self.cabeza
        for nodos in range(self.tamanio):
            dot.node(str(auxliar.valor), label= f"Valor: {str(auxliar.valor)}")
            auxliar= auxliar.next
        aux: Nododos = self.cabeza
        while aux.next is not None:
            dot.edge(str(aux.valor), str(aux.next.valor))
            aux= aux.next
        
        dot.render('Lista', format='png', cleanup=True, view=True)
        print("Grafico generado")