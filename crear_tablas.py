from database import engine, Base
from models import Libro

print("Creando tablas...")

Base.metadata.create_all(engine)

print("Tablas creadas correctamente.")