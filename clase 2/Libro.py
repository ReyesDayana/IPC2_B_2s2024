class Libro:
    def __init__(self, titulo, autor, id_libro, copias):
        self.titulo = titulo
        self.autor = autor
        self.id_libro = id_libro
        self.copias = copias

    def __str__(self):
        return f"{self.titulo}, autor: {self.autor}, id: {self.id_libro}. copias: {self.copias}"