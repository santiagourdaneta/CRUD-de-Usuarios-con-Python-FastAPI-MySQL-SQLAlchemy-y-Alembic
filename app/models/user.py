from sqlalchemy import Column, Integer, String, Date
from app.database.session import Base


class User(Base):
    __tablename__ = "users"


    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    password = Column(String(255), nullable=False)
    telefono = Column(String(255), nullable=False)
    fecha_nacimiento = Column(Date, nullable=False)
    email = Column(String(255), unique=True, nullable=False)