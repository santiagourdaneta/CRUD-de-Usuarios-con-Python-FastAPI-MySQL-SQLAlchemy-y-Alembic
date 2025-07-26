<<<<<<< HEAD
#  FastAPI Users API

CRUD de usuarios utilizando **FastAPI**, **MySQL** y **SQLAlchemy**, con validación de datos mediante **Pydantic**. El proyecto está estructurado siguiendo buenas prácticas para producción.

---

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [MySQL](https://www.mysql.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://docs.pydantic.dev/)
- [Uvicorn](https://www.uvicorn.org/)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

## 🧱 Estructura del proyecto

```
├── app/
│ ├── main.py
│ ├── api/
│ │ └── routes_user.py
│ ├── crud/
│ │ └── user.py
│ ├── models/
│ │ └── user.py
│ ├── schemas/
│ │ └── user.py
│ ├── database/
│ │ └── session.py
│ └── core/
│ └── config.py
├── .env
├── requirements.txt
├── db_users.sql
└── README.md
```

## 🧪 Endpoints principales
### 🔹1. `GET /users/` — Obtener todos los usuarios

**Descripción:** Lista todos los usuarios de la base de datos.

**Respuesta exitosa:**

```json
[
  {
    "id": 1,
    "name": "Milagros Cabrera",
    "email": "mili@example.com",
    "telefono": "3511234567",
    "fecha_nacimiento": "2000-01-01"
  },
  {
    "id": 2,
    "name": "Juan Pérez",
    "email": "juan@example.com",
    "telefono": "3519876543",
    "fecha_nacimiento": "1995-05-20"
  }
]
```
### 2.🔹 GET /users/{id} — Obtener un usuario por ID
Descripción: Devuelve los datos del usuario correspondiente al ID indicado.

Respuesta exitosa:
```json
{
  "id": 1,
  "name": "Milagros Cabrera",
  "email": "mili@example.com",
  "telefono": "3511234567",
  "fecha_nacimiento": "2000-01-01"
}
```
Error si no existe:

```json
{
  "detail": "No encontrado"
}
```

### 3.🔹 POST /users/ — Crear nuevo usuario
Descripción: Crea un nuevo usuario en la base de datos.

Cuerpo de solicitud (JSON):
```json
{
  "name": "Milagros Cabrera",
  "email": "mili@example.com",
  "password": "clave1234",
  "telefono": "3511234567",
  "fecha_nacimiento": "2000-01-01"
}
```
Respuesta exitosa:

```json
{
  "id": 1,
  "name": "Milagros Cabrera",
  "email": "mili@example.com",
  "telefono": "3511234567",
  "fecha_nacimiento": "2000-01-01"
}
```
🛑 Nota: El campo password se recibe pero no se devuelve por seguridad.

### 4.🔹 DELETE /users/{id} — Eliminar usuario
Descripción: Elimina el usuario indicado por su ID.

Respuesta exitosa:

```json
{
  "id": 1,
  "name": "Milagros Cabrera",
  "email": "mili@example.com",
  "telefono": "3511234567",
  "fecha_nacimiento": "2000-01-01"
}
```
Error si no existe:

```json
{
  "detail": "No encontrado"
}
```
---

##  Crear el entorno virtual

```bash
python -m venv venv
# Activar entorno en Windows:
.\venv\Scripts\Activate.ps1
# O en CMD:
venv\Scripts\activate
```

## ⚙️ Requisitos previos
- Python 3.10+
- MySQL instalado localmente (ej. MySQL Workbench)

### 1. Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/fastapi-users-api.git
cd tu-repo
```
### 2.  Instalar dependencias
```bash
pip install -r requirements.txt
```
### 3. Crear la base de datos en MySQL
Abrí MySQL Workbench o terminal y ejecuta 
```bash
mysql -u root -p < db_users.sql
```

### 4.  Crear el archivo .env
```bash
DB_URL=mysql+pymysql://usuario:contraseña@localhost/tubasededatos
```
### 5.  Ejecutar el servidor
```bash
uvicorn main:app --reload
```
=======
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


>>>>>>> 67266a2afc3a02c929a4909076492a8a55e5ac55
