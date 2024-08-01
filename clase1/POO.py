#Ejemplo POO
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.estado = 'disponible'

    def prestar(self):
        if self.estado == 'disponible':
            self.estado = 'prestado'
            return True
        return False
    
    def devolver(self):
        if self.estado == 'prestado':
            self.estado= 'disponible'
            return True
        return False
    
    def __str__(self):
        return f"'{self.titulo}' por {self.autor} ({self.estado})"

class Miembro:

    def __init__(self, nombre):
        self.nombre = nombre
        self.libros_prestados = []

    def tomar_prestado(self, libro):
        if libro.prestar():
            self.libros_prestados.append(libro)
            print(f"{self.nombre} ha tomado prestado el libro {libro.titulo}")
        else:
            print(f"{self.nombre} no puedo prestar el libro {libro.titulo}")   

    def devolver_libro(self, libro):
        if libro in self.libros_prestados and libro.devolver():
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro {libro.titulo}")
        else:
            print(f"{self.nombre} no puedo devolver el libro")
    
    def __str__(self):
        libros = ', '.join([libro.titulo for libro in self.libros_prestados]) or "ninguno"
        return f"Miembro: {self.nombre}, Libros prestados: {libros}"

libro1 = Libro("1984" , "Geoge Orwell")
libro2 = Libro("Cien años de Soledad", "Gabriel Garcia Márquez")
libro3 = Libro("El principito", "Antoine de Saint-Exupéry")

miembro1 = Miembro("Dayana")


miembro1.tomar_prestado(libro1)
miembro1.tomar_prestado(libro2)
miembro1.tomar_prestado(libro3)

print(libro1)
print(libro2)
print(libro3)

miembro1.devolver_libro(libro1)
print(libro1)