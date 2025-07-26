# CRUD-de-Usuarios-con-Python-FastAPI-MySQL-SQLAlchemy-y-Alembic
Aplicación backend robusta para la gestión de usuarios (CRUD: Create, Read, Update, Delete). Desarrollada con Python y el microframework FastAPI, utiliza SQLAlchemy para la interacción con una base de datos MySQL. Las migraciones de la base de datos se manejan eficientemente con Alembic, asegurando la consistencia y escalabilidad del esquema.


[![Python](https://img.shields.io/badge/Python-3.13+-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-8.0+-blue?style=for-the-badge&logo=mysql)](https://www.mysql.com/)
[![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-2.0+-red?style=for-the-badge&logo=sqlalchemy)](https://www.sqlalchemy.org/)

## 📝 Descripción

Este proyecto es una API RESTful completa para la gestión de usuarios, construida sobre un sólido stack tecnológico de Python. La aplicación permite realizar todas las operaciones CRUD (Crear, Leer, Actualizar y Eliminar) sobre la entidad de `Usuario`, sirviendo como un excelente punto de partida para cualquier sistema que requiera una gestión de usuarios robusta y escalable.

### **Características Clave:**

* **Python y FastAPI:** Utiliza FastAPI, un microframework ligero y potente, para el manejo de las rutas y la lógica del servidor.
* **MySQL y SQLAlchemy:** Persistencia de datos gestionada con MySQL, con SQLAlchemy como ORM (Object-Relational Mapper) para una abstracción eficiente y segura de la base de datos.
* **Migraciones con Alembic:** Control de versiones del esquema de la base de datos a través de Alembic, facilitando cambios incrementales y reversibles en la estructura de las tablas.
* **Arquitectura Modular:** Código organizado en módulos (`app.models`, `app.database`, etc.) para una fácil lectura, mantenimiento y expansión.

## 🚀 Cómo Empezar

### **Requisitos Previos**

* Python 3.13+
* MySQL 8.0+

### **1. Configuración del Entorno**

Clona este repositorio y navega a la carpeta del proyecto.

```bash
git clone https://github.com/santiagourdaneta/CRUD-de-Usuarios-con-Python-FastAPI-MySQL-SQLAlchemy-y-Alembic/
cd CRUD-de-Usuarios-con-Python-FastAPI-MySQL-SQLAlchemy-y-Alembic

Crea y activa un entorno virtual de Python para aislar las dependencias:
python -m venv venv
# En Windows
.\venv\Scripts\activate
# En macOS/Linux
source venv/bin/activate

2. Instalación de Dependencias
Instala todas las librerías necesarias:

pip install -r requirements.txt

3. Configuración de la Base de Datos
Abre el archivo de configuración de Alembic (alembic.ini) y ajusta la URL de conexión a tu base de datos MySQL.

# alembic.ini
[sqlalchemy]
sqlalchemy.url = mysql+mysqlconnector://<usuario>:<contraseña>@<host>/<nombre_db>

4. Ejecución de Migraciones
Crea la base de datos en MySQL si aún no existe. Luego, aplica las migraciones para crear la tabla de usuarios:

alembic upgrade head

5. Ejecutar la Aplicación
Inicia el servidor de desarrollo de Flask:

uvicorn main:app --reload

🛠️ Endpoints de la API
La API expone los siguientes endpoints para la gestión de usuarios:

Método	Endpoint	Descripción	Cuerpo de la Solicitud
POST	/api/users	Crea un nuevo usuario.	{ "nombre": ..., "email": ... }
GET	/api/users	Obtiene una lista de todos los usuarios.	N/A
GET	/api/users/<id>	Obtiene los detalles de un usuario por ID.	N/A
PUT	/api/users/<id>	Actualiza los datos de un usuario existente.	{ "email": "nuevo@..." }
DELETE	/api/users/<id>	Elimina un usuario por ID.	N/A

🤝 Contribuciones
Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o enviar un pull request.


