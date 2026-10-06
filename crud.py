from database import SessionLocal
from models import Libro


def agregar_libro(titulo, autor, genero, estado):
    session = SessionLocal()

    try:
        nuevo_libro = Libro(
            titulo=titulo,
            autor=autor,
            genero=genero,
            estado=estado
        )

        session.add(nuevo_libro)
        session.commit()

        print("Libro agregado correctamente.")

    except Exception as e:
        session.rollback()
        print(f"Error al agregar el libro: {e}")

    finally:
        session.close()


def mostrar_libros():
    session = SessionLocal()

    try:
        libros = session.query(Libro).all()

        if not libros:
            print("No hay libros registrados.")
            return

        print("\n--- LISTA DE LIBROS ---")

        for libro in libros:
            print(
                f"ID: {libro.id} | "
                f"Título: {libro.titulo} | "
                f"Autor: {libro.autor} | "
                f"Género: {libro.genero} | "
                f"Estado: {libro.estado}"
            )

    except Exception as e:
        print(f"Error al mostrar los libros: {e}")

    finally:
        session.close()


def buscar_libros(texto):
    session = SessionLocal()

    try:
        resultados = session.query(Libro).filter(
            (Libro.titulo.ilike(f"%{texto}%")) |
            (Libro.autor.ilike(f"%{texto}%")) |
            (Libro.genero.ilike(f"%{texto}%"))
        ).all()

        if not resultados:
            print("No se encontraron libros.")
            return

        print("\n--- RESULTADOS DE BÚSQUEDA ---")

        for libro in resultados:
            print(
                f"ID: {libro.id} | "
                f"Título: {libro.titulo} | "
                f"Autor: {libro.autor} | "
                f"Género: {libro.genero} | "
                f"Estado: {libro.estado}"
            )

    except Exception as e:
        print(f"Error al buscar libros: {e}")

    finally:
        session.close()


def actualizar_libro(id_libro, titulo, autor, genero, estado):
    session = SessionLocal()

    try:
        libro = session.get(Libro, id_libro)

        if libro is None:
            print("No se encontró un libro con ese ID.")
            return

        libro.titulo = titulo
        libro.autor = autor
        libro.genero = genero
        libro.estado = estado

        session.commit()

        print("Libro actualizado correctamente.")

    except Exception as e:
        session.rollback()
        print(f"Error al actualizar el libro: {e}")

    finally:
        session.close()


def eliminar_libro(id_libro):
    session = SessionLocal()

    try:
        libro = session.get(Libro, id_libro)

        if libro is None:
            print("No se encontró un libro con ese ID.")
            return

        session.delete(libro)
        session.commit()

        print("Libro eliminado correctamente.")

    except Exception as e:
        session.rollback()
        print(f"Error al eliminar el libro: {e}")

    finally:
        session.close()