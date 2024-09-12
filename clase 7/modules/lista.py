from modules.nodo import NodoAlumno
import xml.etree.ElementTree as ET

class ListaAlumnos:
    def __init__(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0
    
    def agregar_alumno(self, nombre, carnet):
        nuevo_alumno = NodoAlumno(nombre,carnet)
        if self.cabeza is None:
            self.cabeza = nuevo_alumno
            self.ultimo = nuevo_alumno
            self.tamanio +=1
        else:
            self.cabeza.anterior = nuevo_alumno
            nuevo_alumno.siguiente = self.cabeza
            self.cabeza = nuevo_alumno
            self.tamanio += 1

    def quitar_alumno(self):
        self.ultimo = self.ultimo.anterior
        self.ultimo.siguiente = None

    def obtener_alumno_por_carnet(self, carnet):
        actual = self.cabeza
        for i in range(self.tamanio):
            if actual.carnet == carnet:
                return actual
            actual = actual.siguiente
        return None
    
    def generar_html_alumnos(self):
        html = ""
        actual = self.cabeza
        for i in range(self.tamanio):
            html += f'<li><a href="/alumno/{actual.carnet}"> {actual.nombre}</a></li>\n'
            actual = actual.siguiente
        return html
    
    def vaciar_lista(self):
        self.cabeza = None
        self.ultimo = None
        self.tamanio = 0

def leer_alumnos(archivo_xml):
    tree = ET.parse(archivo_xml)
    root = tree.getroot()

    lista_alumnos = ListaAlumnos()

    for alumno in root.findall('alumno'):
        nombre = alumno.text
        carnet = alumno.get('carnet')
        lista_alumnos.agregar_alumno(nombre, carnet)

    return lista_alumnos