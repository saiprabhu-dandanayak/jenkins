

from fastapi import Depends, HTTPException, status
from jose import JWTError, jwt
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
import secrets
import bcrypt
from db.session import sessionLocal
import os
from dotenv import load_dotenv


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

load_dotenv()

SECRET_KEY = secrets.token_hex(32)
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("TOKEN_EXPIRE_MINUTES"))

def create_jwt_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f" payload --------->{payload}")
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    return email
