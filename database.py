from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Datos de conexión a MariaDB
USUARIO = "root"
CONTRASENA = "pandorar27"
HOST = "localhost"
PUERTO = 3306
BASE_DATOS = "biblioteca"

# Cadena de conexión
DATABASE_URL = (
    f"mariadb+mariadbconnector://{USUARIO}:{CONTRASENA}"
    f"@{HOST}:{PUERTO}/{BASE_DATOS}"
)

# Crear conexión con MariaDB
engine = create_engine(DATABASE_URL, echo=False)

# Crear sesiones
SessionLocal = sessionmaker(bind=engine)

# Clase base para los modelos ORM
Base = declarative_base()