# app/database/session.py

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Define la URL de la base de datos desde una variable de entorno o usa una por defecto.
# Asegúrate de que esta URL sea correcta.
DATABASE_URL = os.getenv("DATABASE_URL", "mysql+mysqlconnector://root:@localhost/your_test_db")

# 1. Creamos el objeto 'engine' que usará SQLAlchemy para conectarse a la DB.
# Es crucial que esta variable se defina y esté disponible para la importación.
engine = create_engine(DATABASE_URL)

# 2. Creamos la clase 'Base' para que nuestros modelos la hereden.
# Alembic y los modelos la usarán para conocer las tablas.
Base = declarative_base()

# 3. Creamos una clase de sesión local para nuestras transacciones.
# Es crucial que esta variable se defina y esté disponible para la importación.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 4. Una función de conveniencia para obtener una sesión.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()