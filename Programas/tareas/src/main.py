from models.task import crear_tabla
from controllers.task_controller import (
    nueva_tarea,
    listar_tareas,
    cambiar_estado,
    eliminar_tarea,
)


def menu():
    while True:
        accion = input(
            "Agregar Tarea (1), Listar Tareas (2), Marcar tarea (3), Eliminar tarea (4), salir (e): "
        )

        if accion == "1":
            titulo = input("Nombre de la tarea: ")
            descripcion = input("Descripción de la tarea: ")
            nueva_tarea(titulo, descripcion)
        if accion == "2":
            listar_tareas()
        if accion == "3":
            id_tarea = input("ID para cambiar el estado de la tarea: ")
            cambiar_estado(id_tarea)
        if accion == "4":
            id_tarea = input("ID para eliminar tarea: ")
            eliminar_tarea(id_tarea)
        if accion == "e":
            break


if __name__ == "__main__":
    crear_tabla()
    menu()
