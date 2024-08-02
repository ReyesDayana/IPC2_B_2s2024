from Libro import Libro
from persona import Lector, Bibliotecario
from biblioteca import Biblioteca


def main():
    biblioteca = Biblioteca("Biblioteca USAC")

    libro1 = Libro("1984","Geoge Orwell", "0001", 5)
    libro2 = Libro("Cien años de Soledad", "Gabriel Garcia Márquez","002", 1)
    libro3 = Libro("El principito", "Antoine de Saint-Exupéry", "003", 9)

    lector = Lector("Dayana",22, "L001")
    bibliotecario = Bibliotecario("Ottoniel", 22, "P002", "B001")

    bibliotecario.añadirLibro(biblioteca,libro1)
    bibliotecario.añadirLibro(biblioteca, libro2)

    # Agregar miembros a la biblioteca
    biblioteca.agregar_miembro(lector)
    biblioteca.agregar_miembro(bibliotecario)

    # Préstamo de libros
    biblioteca.prestar_libro(lector, libro1)
    biblioteca.prestar_libro(lector, libro2)

    # Devolución de libros
    biblioteca.devolver_libro(lector, libro1)
    biblioteca.devolver_libro(lector, libro2)

    # Remover libros de la biblioteca
    bibliotecario.eliminarLibro(biblioteca, libro1)
if __name__ == "__main__":
    main()