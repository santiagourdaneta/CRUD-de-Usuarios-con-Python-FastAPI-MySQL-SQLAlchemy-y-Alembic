# app/database/seed.py
import os
from datetime import date
from sqlalchemy.orm import Session

# Importa tus componentes de sesión y modelos
# Asume que app/database/session.py ahora tiene get_db o SessionLocal directamente accesible
from app.database.session import get_engine, get_session_local, Base # Importa Base para asegurarte de que los modelos se carguen
from app.models.user import User
from app.schemas.user import UserCreate
from app.crud.user import create_user
from app.core.config import settings

# Para hashear contraseñas
from passlib.context import CryptContext
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Para generar datos aleatorios
from faker import Faker
fake = Faker('es_ES') # Puedes usar 'en_US' o el locale que prefieras

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def generate_random_user_data():
    """Genera datos de usuario aleatorios usando Faker."""
    name = fake.name()
    # Genera un email más robusto para unicidad
    email = f"{fake.user_name()}.{fake.random_int(min=100, max=999)}@{fake.free_email_domain()}".lower()
    password = "password123" # Contraseña base, será hasheada
    telefono = fake.phone_number()
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=60)

    return {
        "name": name,
        "email": email,
        "password": password,
        "telefono": telefono,
        "fecha_nacimiento": fecha_nacimiento.isoformat() # Formato 'YYYY-MM-DD'
    }

def seed_database(num_users_to_seed: int = 50): # Cambiado a 50 por defecto
    print(f"Iniciando el proceso de siembra de datos para {num_users_to_seed} usuarios...")

    # Usa la configuración de tu aplicación para obtener la URL de la DB
    db_url = settings.DB_URL
    engine_instance = get_engine(db_url)
    SessionLocal = get_session_local(engine_instance) # Obtiene el factory de sesión

    db: Session = SessionLocal() # Crea una sesión de base de datos

    try:
        # Asegurarse de que el usuario 'admin' (o un usuario inicial importante) exista
        admin_email = "admin@example.com"
        existing_admin = db.query(User).filter(User.email == admin_email).first()
        if not existing_admin:
            print(f"Creando usuario administrador: {admin_email}")
            admin_data = {
                "name": "Admin User",
                "email": admin_email,
                "password": get_password_hash("adminpassword"),
                "telefono": "1112223334",
                "fecha_nacimiento": "1985-05-10"
            }
            admin_user_in = UserCreate(**admin_data)
            create_user(db=db, user=admin_user_in)
        else:
            print(f"Usuario administrador {admin_email} ya existe. Saltando.")


        # Generar y añadir los N usuarios adicionales
        users_added_count = 0
        for i in range(num_users_to_seed):
            user_data = generate_random_user_data()

            # Verificar si el email ya existe para evitar duplicados
            existing_user = db.query(User).filter(User.email == user_data["email"]).first()
            if not existing_user:
                print(f"[{i+1}/{num_users_to_seed}] Creando usuario: {user_data['email']}")
                user_data["password"] = get_password_hash(user_data["password"])

                user_in = UserCreate(**user_data)
                create_user(db=db, user=user_in)
                users_added_count += 1
            else:
                # Si el email generado aleatoriamente ya existe
                print(f"[{i+1}/{num_users_to_seed}] Usuario {user_data['email']} ya existe (generado aleatoriamente duplicado o ya existente). Saltando.")

            # Commit cada cierto número de usuarios para no tener una transacción gigante
            if (i + 1) % 10 == 0: # Commit cada 10 usuarios para 50
                db.commit()
                print(f"--- Commit intermedio: {users_added_count} usuarios añadidos hasta ahora ---")


        db.commit() # Confirma los cambios restantes
        print(f"Siembra de datos completada exitosamente. Se añadieron {users_added_count} nuevos usuarios.")

    except Exception as e:
        db.rollback() # En caso de error, deshaz los cambios
        print(f"Ocurrió un error durante la siembra de datos: {e}")
        import traceback
        traceback.print_exc() # Imprime el error completo para depuración
    finally:
        db.close() # Asegúrate de cerrar la sesión

if __name__ == "__main__":
    # Asegúrate de que la DB_URL esté configurada correctamente
    # para tu entorno de desarrollo/producción al ejecutar este script.
    print(f"Usando DB_URL: {settings.DB_URL}")
    seed_database(num_users_to_seed=50) # Llama con 50 usuarios por defecto