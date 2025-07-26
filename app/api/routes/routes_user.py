from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database.session import SessionLocal
from app.schemas.user import UserCreate, UserResponse
from app.crud.user import create_user, get_user, get_users, delete_user
from app.crud.user import get_user_by_email
from app.api.dependencies.bd import get_db


router = APIRouter(prefix="/users", tags=["Users"])

@router.post("/", response_model=UserResponse)
def create(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = get_user_by_email(db,user.email)
    if(existing_user): 
        raise HTTPException(status_code=400, detail="El email ya está registrado")
    else:
        return create_user(db, user)

@router.get("/", response_model=list[UserResponse])
def read_all(db: Session = Depends(get_db)):
    return get_users(db)


@router.get("/{user_id}", response_model=UserResponse)
def read_one(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No se encontro el usuario")
    return user

@router.delete("/{user_id}", response_model=UserResponse)
def delete(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="No se pudo eliminar el usuario")
    return user