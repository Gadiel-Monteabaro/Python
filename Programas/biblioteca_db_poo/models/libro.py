class Libro:
    def __init__(self, titulo, autor, estado=True):
        self.titulo = titulo
        self.autor = autor
        self.estado = estado

    def __str__(self):
        return f"'{self.titulo}' por {self.autor} - Estado: {self.estado}"

    def prestar(self):
        if self.estado == "disponible":
            self.estado = "prestado"
            return True
        return False

    def devolver(self):
        if self.estado == "prestado":
            self.estado = "disponible"
            return True
        return False
