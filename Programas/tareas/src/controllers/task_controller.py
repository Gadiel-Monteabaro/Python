from db import get_connection


def nueva_tarea(titulo, descripcion):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                query = "INSERT INTO tareas (titulo, descripcion) VALUES (%s,%s)"
                cursor.execute(query, (titulo, descripcion))
        print(f"Tarea creada.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def listar_tareas():
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                query = "SELECT id, titulo, descripcion, estado FROM tareas ORDER BY id"
                cursor.execute(query)
                tareas = cursor.fetchall()
                for tarea in tareas:
                    estado = "Completada" if tarea[3] else "No completada"
                    print(f"{tarea[1]} - {tarea[2]} - Estado: {estado}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def cambiar_estado(task_id):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                query = "SELECT estado FROM tareas WHERE id = %s"
                cursor.execute(query, (task_id,))
                resultado = cursor.fetchone()

                if resultado is None:
                    print("Tarea no encontrada.")

                estado_actual = resultado[0]
                nuevo_estado = not estado_actual

                query = "UPDATE tareas SET estado = %s WHERE id = %s"
                cursor.execute(query, (nuevo_estado, task_id))
        estado = "Completada" if nuevo_estado else "No Completada"
        print(f"Tarea marcada como {estado}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


def eliminar_tarea(task_id):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                query = "DELETE FROM tareas WHERE id = %s"
                cursor.execute(query, (task_id,))
        print("Tarea eliminada.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()


# Permite filtrar tareas por completadas o no completadas
def filtrar_tareas(estado):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                query = "SELECT id, titulo, descripcion, estado FROM tareas WHERE estado = %s"
                cursor.execute(query, (estado,))
                tareas = cursor.fetchall()
                estado = "completadas" if estado else "no completadas"
                print(f"Tareas {estado}: ")
                for tarea in tareas:
                    estado = "Completada" if tarea[3] else "No completada"
                    print(f"{tarea[1]} - {tarea[2]} - Estado: {estado}")
                if not tareas:
                    print("No hay tareas")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
