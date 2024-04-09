from fastapi import APIRouter, Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from models.User_model import User
import schemas.User_Schema as schemas
from db.session import get_db
from . import auth
import bcrypt
from datetime import timedelta
from jose import JWTError
from .auth import create_jwt_token, ACCESS_TOKEN_EXPIRE_MINUTES , get_current_user
from Exception.GlobalExceptions import *
import logging


router = APIRouter()



@router.get("/", tags=["Home"])
def home_page(request: Request):
    logging.info("Home page accessed")
    return {"message": "Welcome to the homepage"}


@router.get("/users", tags=["User"])
def get_all_users(current_user: str = Depends(get_current_user),db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users


@router.get("/users/{user_id}", tags=["User"])
def get_user_by_id(user_id: int, current_user: str = Depends(get_current_user),db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.post("/signup/user", tags=["User"])
def create_user(user: schemas.Request_User_Model, db: Session = Depends(get_db)):
    
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")


    hashed_password = bcrypt.hashpw(
        user.password.encode("utf-8"), bcrypt.gensalt()
    )
    db_user = User(email=user.email, password=hashed_password, name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


@router.post("/signin", response_model=dict)
def sign_in_user(user: schemas.Login_Model, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.email == user.email).first()
    if existing_user is None or not bcrypt.checkpw(user.password.encode('utf-8'), existing_user.password.encode('utf-8')):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)  
    jwt_token = auth.create_jwt_token(data={"sub": existing_user.email}, expires_delta=expires)

    return {"token": jwt_token}


@router.put("/users/{user_id}", tags=["User"])
def update_user(user_id: int, user: schemas.Request_User_Model,current_user: str = Depends(get_current_user), db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user


@router.patch("/users/change-password", tags=["User"])
def change_password(email: str, password_data: schemas.Request_Password_Change, db: Session = Depends(get_db)):
    db_user = db.query(User).filter(models.User.email == email).first()
    
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")

    hashed_password = bcrypt.hashpw(
        password_data.new_password.encode("utf-8"), bcrypt.gensalt()
    )
    
    db_user.password = hashed_password
    db.commit()
    db.refresh(db_user)
    
    return {"message": "Password changed successfully"}

@router.delete("/users/{user_id}", tags=["User"])
def delete_user_by_id(user_id: int, current_user: str = Depends(get_current_user),db: Session = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(db_user)
    db.commit()
    return {"message": "User deleted successfully"}


@router.delete("/users", tags=["User"])
def delete_all_users(current_user: str = Depends(get_current_user),db: Session = Depends(get_db)):
    db.query(User).delete()
    db.commit()
    return {"message": "All users deleted successfully"}
