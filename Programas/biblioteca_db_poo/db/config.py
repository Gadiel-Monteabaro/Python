import mysql.connector
from mysql.connector import errorcode
import logging


logger = logging.getLogger("mysql.connector")
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(stream_handler)


class DB:

    @staticmethod
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
            logger.error(err)
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                raise Exception("Usuario o contraseña incorrectos.")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                raise Exception("La base de Datos no existe.")
            else:
                Exception(err)
