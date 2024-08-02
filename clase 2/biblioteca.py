from Libro import Libro
from persona import Lector, Bibliotecario

class Biblioteca:
    def __init__(self, nombre):
        self.nombre=nombre
        self.libros = {}
        self.miembros = {}

    def __str__(self):
        return f"Biblioteca: {self.nombre}"
    def agregarLibro(self, libro):
        if libro.id_libro in self.libros:
            self.libros[libro.id_libro].copias += libro.copias
        else:
            self.libros[libro.id_libro] = libro
        print(f"Libro {libro.titulo} agregado. Total de copias {self.libros[libro.id_libro].copias}")

    def eliminarLibro(self, libro):
        if libro.id_libro in self.libros:
            if self.libros[libro.id_libro].copias > 1:
                self.libros[libro.id_libro].copias -= 1
            else:
                del self.libros[libro.id_libro]
            print(f"Libro: {libro.titulo} eliminado.")


    def agregar_miembro(self, persona):
        self.miembros[persona.id_number] = persona

    def eliminar_miembro(self, persona):
        if persona.id_number in self.miembros:
            del self.miembros[persona.id_number]
            print("Persona Agregada")
        else:
            print(f"Persona no encontrada")

    def prestar_libro(self, lector, libro):
        if libro.id_libro in self.libros and self.libros[libro.id_libro].copias > 0:
            lector.prestar_libro(libro)
            self.libros[libro.id_libro].copias -=1
            print(f"Libro {libro.titulo} prestado")
    def devolver_libro(self, lector, libro):
        lector.devolver_libro(libro)
        if libro.id_libro in self.libros:
            self.libros[libro.id_libro].copias +=1
        else:
            self.libros[libro.id_libro] = libro
        print(f"Se ha devuelto el libro")