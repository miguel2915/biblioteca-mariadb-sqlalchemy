# Biblioteca Personal

Aplicación de biblioteca personal desarrollada en Python. La aplicación permite administrar libros utilizando MariaDB como sistema gestor de base de datos y SQLAlchemy como ORM.

## Funciones principales

La aplicación permite:

1. Agregar libros.
2. Actualizar información de libros.
3. Eliminar libros.
4. Mostrar todos los libros registrados.
5. Buscar libros por título, autor o género.
6. Salir del programa.

## Tecnologías utilizadas

- Python 3.14
- MariaDB
- SQLAlchemy
- MariaDB Connector/Python

## Estructura del proyecto

```text
biblioteca-python/
│
├── app.py
├── crud.py
├── database.py
├── models.py
├── crear_tablas.py
├── requirements.txt
└── README.md

1. Instalación de MariaDB
Primero se debe instalar MariaDB Server en el equipo.
Durante la instalación se debe configurar una contraseña para el usuario root.
Después de instalar MariaDB, se debe comprobar que el servicio de MariaDB esté ejecutándose en Windows.
2. Crear la base de datos
Abrir la consola de MariaDB utilizando el usuario root.
Ejecutar:
CREATE DATABASE biblioteca;

Para comprobar que la base de datos fue creada:
SHOW DATABASES;

Debe aparecer la base de datos:
biblioteca

3. Configuración de la conexión
La conexión con MariaDB se encuentra en el archivo database.py.
La aplicación utiliza SQLAlchemy para conectarse a MariaDB mediante el conector de MariaDB para Python.
La configuración contiene:
- Usuario
- Contraseña
- Servidor
- Puerto
- Nombre de la base de datos
El servidor utilizado es:
localhost

El puerto utilizado por MariaDB es:
3306

El nombre de la base de datos es:
biblioteca

4. Instalación de las dependencias
Abrir una terminal dentro de la carpeta del proyecto y ejecutar:
pip install -r requirements.txt

Las principales dependencias utilizadas son:
SQLAlchemy
mariadb

5. Crear las tablas
Después de crear la base de datos, ejecutar:
python crear_tablas.py

Este archivo utiliza SQLAlchemy para crear automáticamente las tablas definidas en los modelos.
La tabla principal utilizada por la aplicación es:
libros

La tabla contiene los siguientes campos:
Campo	Tipo	Descripción
id	Integer	Identificador único del libro
titulo	String	Título del libro
autor	String	Autor del libro
genero	String	Género del libro
estado	String	Estado de lectura


6. Ejecutar la aplicación
Para iniciar el programa:
python app.py

Se mostrará un menú con las siguientes opciones:
===== BIBLIOTECA PERSONAL =====
1. Agregar libro
2. Actualizar libro
3. Eliminar libro
4. Mostrar todos los libros
5. Buscar libro
6. Salir

7. Estados de lectura
Al agregar o actualizar un libro se puede seleccionar uno de los siguientes estados:
1. Pendiente
2. Leyendo
3. Terminado

8. SQLAlchemy y ORM
SQLAlchemy es una biblioteca de Python que permite trabajar con bases de datos utilizando código Python.
En este proyecto se utiliza el enfoque ORM (Object-Relational Mapping).
El ORM permite representar las tablas de la base de datos mediante clases de Python.
Por ejemplo, la tabla libros está representada mediante la clase:
class Libro(Base):


Cada objeto Libro representa un registro de la tabla libros.
Esto permite realizar operaciones como agregar, consultar, modificar y eliminar registros utilizando objetos y métodos de Python en lugar de escribir directamente todas las consultas SQL.
9. Manejo de errores
La aplicación utiliza manejo de excepciones mediante try, except y finally.
Esto permite controlar errores que puedan ocurrir durante las operaciones con la base de datos.
Cuando ocurre un error durante una operación de modificación, se utiliza:
session.rollback()


para evitar que una operación incompleta quede guardada en la base de datos.
10. Flujo de funcionamiento
El funcionamiento general de la aplicación es:
Usuario
   ↓
app.py
   ↓
crud.py
   ↓
SQLAlchemy ORM
   ↓
MariaDB
   ↓
Base de datos biblioteca

11. Comandos principales
Instalar dependencias:
pip install -r requirements.txt

Crear las tablas:
python crear_tablas.py

Ejecutar la aplicación:
python app.py

