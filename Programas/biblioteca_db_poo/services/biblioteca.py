from models.libro import Libro


class Biblioteca:
    def __init__(self, dao):
        self.dao = dao

    def agregar_libro(self, titulo, autor):
        nuevo_libro = Libro(titulo, autor)
        self.dao.create(nuevo_libro)
