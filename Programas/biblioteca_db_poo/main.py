from dao.libro_dao import LibroDAO
from services.biblioteca import Biblioteca


def main():
    libro_dao = LibroDAO()
    biblioteca = Biblioteca(libro_dao)

    while True:
        accion = input("Agregar libro (1), Listar biblioteca (2) ó salir (3) ")

        if accion == "1":
            titulo = input("Igresar titulo del libro: ")
            autor = input("Ingresar autor del libro: ")
            biblioteca.agregar_libro(titulo, autor)

        if accion == "2":
            biblioteca.listar_libros()

        if accion == "3":
            break


if __name__ == "__main__":
    main()
