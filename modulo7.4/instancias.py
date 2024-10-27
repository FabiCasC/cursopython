class Libro: 
    def __init__(self, titulo, autor, año_de_publicacion):
        self.titulo = titulo
        self.autor = autor
        self.año_de_publicacion = año_de_publicacion
        self.disponible = True
    
    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"El libro {self.titulo} ha sido prestado"
        else: 
            return f"El libro {self.titulo} no está disponible para el préstamo"
        
    def devolver(self):
        if not self.disponible:
            self.disponible = True
            return f"El libro {self.titulo} ha sido devuelto y ahora está disponible."
        else: 
            return f"El libro {self.titulo} ya estaba disponible"

class Autor: 
    def __init__(self, nombre, pais):
        self.nombre = nombre
        self.pais = pais
        self.libros = []

    def agregar_libros(self, libro):
        self.libros.append(libro)

    def mostrar_libros(self):
        if self.libros:
            print(f"Libros de {self.nombre}:")
            for libro in self.libros: 
                print(f"{libro.titulo} ({libro.año_de_publicacion})")
        else: 
            print(f"{self.nombre} no tiene libros registrados")

class Miembro: 
    def __init__(self, nombre): 
        self.nombre = nombre
        self.prestamos = []
    
    def tomar_prestado(self, libro): 
        if libro.disponible:
            libro.prestar()
            self.prestamos.append(libro)
            return f"{self.nombre} ha tomado prestado {libro.titulo}"
        else:
            return f"{libro.titulo} no está disponible."

    def devolver_libro(self, libro):
        if libro in self.prestamos: 
            libro.devolver()
            self.prestamos.remove(libro)
            return f"{self.nombre} ha devuelto {libro.titulo}"
        else: 
            return f"{self.nombre} no tiene el libro {libro.titulo} en su lista de préstamos"

# Ejemplo de uso

# Crear autores
autor1 = Autor("Gabriel", "Colombia")
autor2 = Autor("Jane Austen", "Inglaterra")

# Crear libros con el autor correspondiente
libro1 = Libro("Cien años de soledad", autor1, 1972)
libro2 = Libro("Orgullo y prejucio", autor2, 1813)

autor1.agregar_libros(libro1)
autor2.agregar_libros(libro2)

miembro1 = Miembro("Juan")
miembro2 = Miembro("Ana")

print(miembro1.tomar_prestado(libro1))
print(miembro2.tomar_prestado(libro2))

print(miembro1.tomar_prestado(libro2))

print(miembro1.devolver_libro(libro1))

autor1.mostrar_libros()