from NodoPersona import Persona
import os
import webbrowser
class Personas:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

    def agregarPersona(self, nombre, edad):
        nueva_persona = Persona(nombre, edad)
        if self.cabeza is None:
            self.cabeza = nueva_persona
            self.ultimo = nueva_persona
            self.tamanio += 1
        else:
            self.ultimo.siguiente = nueva_persona
            self.ultimo= nueva_persona
            self.tamanio += 1
    def Graficar(self):
        contador = 0
        graficarlista = "digraph G { \n"
        graficarlista += "node[shape=box] \n"
        graficarlista += "label= \"Personas\" \n"
        auxiliar: Persona = self.cabeza
        for persona in range(self.tamanio):
            nodopersona = "alumno" + str(contador)
            contador += 1
            graficarlista += nodopersona + "[label=\"Nombre: " + auxiliar.nombre +  "\n Edad: " + str(auxiliar.edad) + " \"] \n"
            auxiliar = auxiliar.siguiente

        contador = 0
        aux: Persona = self.cabeza
        while aux.siguiente is not None:
            nodopersona = "alumno" + str(contador)
            contadoraux = contador + 1
            contador += 1
            nodosiguintepersona = "alumno" + str(contadoraux)
            graficarlista += "{rank=same; " + nodopersona + " ->" + nodosiguintepersona + "}\n";
            aux = aux.siguiente
        graficarlista += "}"
        dot = "personas.txt"
        with open(dot, 'w') as grafo:
            grafo.write(graficarlista)
        result = "static/personas.jpg"
        os.system("dot -Tjpg " + dot + " -o " + result)

