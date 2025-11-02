class Tarea:
    def __init__(self, titulo, descripcion, completada=False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada

    def marcar_completada(self):
        self.completada = True

    def marcar_no_completada(self):
        self.completada = False

    def __str__(self):
        estado = "Completada" if self.completada else "No completada"
        return f"Tarea: {self.titulo} Estado: {estado}"


if __name__ == "__main__":
    tarea = Tarea("Hacer gym", "20 min de cardio")
    print(tarea)