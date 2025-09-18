from dao.libro_dao import LibroDAO
from services.biblioteca import Biblioteca


def main():
    libro_dao = LibroDAO()
    biblioteca = Biblioteca(libro_dao)

    # Ejemplo de uso: Agregar un libro
    biblioteca.agregar_libro("Cien Años de Soledad", "Gabriel García Márquez")
    print("Libro agregado a la biblioteca.")


if __name__ == "__main__":
    main()
