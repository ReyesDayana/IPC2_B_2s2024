class Persona:
    def __init__(self, nombre, edad, id_number):
        self.nombre = nombre
        self.edad = edad
        self.id_number = id_number
    def __str__(self):
        return f"{self.name}, ID:{self.id_number}, Edad: {self.edad}"

class Lector(Persona):
    def __init__(self, nombre, edad, id_number):
        super().__init__(nombre, edad, id_number)
        self.libros_prestados = []

    def prestar_libro(self, libro):
        self.libros_prestados.append(libro)
        print(f"{self.nombre} prestó el libro {libro.titulo}")

    def devolver_libro(self, libro):
        if libro in self.libros_prestados:
            self.libros_prestados.remove(libro)
            print(f"{self.nombre} ha devuelto el libro {libro.titulo}")
        else:
            print(f"{self.nombre} no tiene el libro ")

class Bibliotecario(Persona):
    def __init__(self, nombre, edad, id_number, id_empleado):
        super().__init__(nombre, edad, id_number)
        self.id_empleado = id_empleado

    def __str__(self):
        return f"{super().__str__()}, Id emeplado: {self.id_empleado}"

    def añadirLibro(self, biblioteca, libro):
        biblioteca.agregarLibro(libro)
        print(f"{self.nombre} ha añadido el libro {libro.titulo} a la biblioteca")

    def eliminarLibro(self, biblioteca, libro):
        biblioteca.eliminarLibro(libro)
        print(f"{self.nombre} ha eliminado el libro {libro.titulo} de la biblioteca")