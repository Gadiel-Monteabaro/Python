from db import get_connection


def nueva_tarea(titulo, descripcion):
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                query = "INSERT INTO tareas (titulo, descripcion) VALUES (%s,%s)"
                cursor.execute(query, (titulo, descripcion))
        print(f"Tarea creada correctamente.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
