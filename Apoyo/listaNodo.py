from Nodo import Libro

class ListaLibros:
    def __init__(self):
        self.cabeza = None

    def agregarLibro(self,  titulo, autor, anio, editorial):
        nuevo_libro = Libro(titulo, autor, anio, editorial)
        if not self.cabeza:
            self.cabeza = nuevo_libro
            self.cabeza.next = nuevo_libro
        else:
            current = self.cabeza
            while current.next != self.cabeza:
                current = current.next
            current.next = nuevo_libro
            nuevo_libro.next = self.cabeza  # Cierre del ciclo

    def imprimirLibros(self):
        current = self.cabeza
        while True:
            print(f"Titulo: {current.titulo}, Autor:  {current.autor}, Año: {current.anio}, Editorial: {current.editorial}")
            if current.next == self.cabeza:
                break
            current = current.next
libros = ListaLibros()
libros.agregarLibro("Matar a un ruiseñor", "Harper Lee", 1960, " J.B. Lippincott & Co.")
libros.agregarLibro("Beloved", "Toni Morrison", 1987, "Alfred A. Knopf")
libros.agregarLibro("Emma", "Jane Austen", 1815, "John Murray")
libros.agregarLibro("Guerra", "Sebastian Junger", 2010, "Twelve")
libros.agregarLibro("Paz", "Richard Bausch", 2008, "Alfred A. Knopf")
libros.imprimirLibros()