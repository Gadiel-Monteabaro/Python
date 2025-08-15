import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
USER = os.getenv("USER")
PASS = os.getenv("PASS")
PORT = os.getenv("PORT")


def get_connection():
    try:
        conn = psycopg2.connect(
            host=HOST,
            dbname=DB_NAME,
            user=USER,
            password=PASS,
            port=PORT,
        )
        return conn
    except Exception as e:
        print(f"Error: {e}")
        return None
