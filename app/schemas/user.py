from pydantic import BaseModel, EmailStr, ConfigDict 
from datetime import date

class UserBase(BaseModel):
    name: str
    telefono: str
    fecha_nacimiento: date    
    email: EmailStr

class UserCreate(UserBase):
    password: str                 

class UserResponse(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)