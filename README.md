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
