from models.task import crear_tabla
from controllers.task_controller import nueva_tarea


def menu():
    while True:
        accion = input("Agregar Tarea (1): ")

        if accion == "1":
            titulo = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            nueva_tarea(titulo, descripcion)


if __name__ == "__main__":
    crear_tabla()
    menu()
