from db import get_connection


def crear_tabla():
    conn = get_connection()

    try:
        with conn:
            with conn.cursor() as cursor:
                query = "CREATE TABLE IF NOT EXISTS tareas (id SERIAL PRIMARY KEY,titulo VARCHAR(255) NOT NULL,descripcion TEXT,estado BOOLEAN DEFAULT FALSE)"
                cursor.execute(query)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()
