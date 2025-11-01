class Libro:
    def __init__(self, titulo, autor, estado=True):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} - Estado: {self.estado}"

    def prestar(self):
        if self.estado:
            self.estado = False
        return "prestado" if not self.estado else "no disponible"

    def devolver(self):
        if not self.estado:
            self.estado = True
        return "disponible" if self.estado else "no devuelto"
