class Libro:
    # constructor
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    # string, llamada interna, lo que devuelve es lo que se imprime
    def __str__(self):
        return f"El libro {self.titulo} de {self.autor} tiene {self.paginas} paginas"

    # longitud, devuelve la longitud de nuestro objeto
    def __len__(self):
        return self.paginas


libro = Libro(titulo="Hola Mundo", autor="Gadiel", paginas=250)
print(libro)
