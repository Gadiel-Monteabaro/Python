import mysql.connector
from mysql.connector import errorcode


def connect_to_db():
    try:
        return mysql.connector.connect(
            host="localhost",
            user="root",
            password="2693-/3962Ga@",
            database="biblioteca",
            port=3306,
        )
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario o contraseña incorrectos.")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("La base de Datos no existe.")
        else:
            print(err)
    return None
