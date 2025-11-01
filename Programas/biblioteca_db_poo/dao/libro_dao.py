import mysql.connector
from db.config import DB
from models.libro import Libro


class LibroDAO:
    def __init__(self):
        self.connect_to_db = DB.connect_to_db()
        self.cursor = self.connect_to_db.cursor()
        self.crear_tabla()

    def crear_tabla(self):
        try:
            self.cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS libros (
                    id_libro INT AUTO_INCREMENT PRIMARY KEY,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(255) NOT NULL,
                    estado BOOLEAN DEFAULT TRUE
                )
                """
            )
            self.connect_to_db.commit()
        except mysql.connector.Error as err:
            raise Exception(f"Error al crear la tabla: {err}")

    def create(self, libro):
        with self.connect_to_db.cursor() as cursor:
            try:
                sql = "INSERT INTO libros (titulo, autor, estado) VALUES (%s, %s, %s)"
                values = (libro.titulo, libro.autor, libro.estado)
                cursor.execute(sql, values)
                self.connect_to_db.commit()
                self.cursor.close()
            except mysql.connector.Error as err:
                raise Exception(f"Error al insertar el libro: {err}")

    def get_all(self):
        try:
            with self.connect_to_db.cursor(dictionary=True) as cursor:
                sql = "SELECT * FROM libros"
                cursor.execute(sql)
                resultados = cursor.fetchall()  # trae todos los registros
                return [
                    Libro(r["titulo"], r["autor"], r["estado"])
                    for r in resultados
                ]
        except mysql.connector.Error as err:
            raise Exception(f"Error al consultar los libros: {err}")
