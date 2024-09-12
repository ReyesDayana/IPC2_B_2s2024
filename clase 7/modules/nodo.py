class NodoAlumno:
    def __init__(self, nombre, carnet):
        self.nombre= nombre
        self.carnet = carnet
        self.siguiente = None
        self.anterior = None