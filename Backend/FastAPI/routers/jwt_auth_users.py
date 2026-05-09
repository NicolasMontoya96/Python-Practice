from fastapi import FastAPI,APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta
from pwdlib import PasswordHash

import os
from dotenv import load_dotenv

load_dotenv()
# --- Configuración global ---
ALGORITHM = "HS256" # Algoritmo de cifrado para el JWT
ACCESS_TOKEN_DURATION = 1 # Tiempo de expiración del token en minutos
SECRET =  os.getenv("JWT_SECRET")
# Clave secreta para firma

router = APIRouter()

# Configura OAuth2 con la URL de login
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Inicializa el manejador de contraseñas (Argon2)
pwd_context = PasswordHash.recommended()
#crypt = CryptContext(schemes=["bcrypt"])

# --- Modelos de datos ---
class User(BaseModel):
    """Modelo de usuario con datos públicos."""
    username: str
    full_name: str
    email: str  
    disabled: bool

class UserDB(User):
    """Modelo de usuario que incluye la contraseña para validación interna."""
    password: str


# --- Base de datos simulada ---
users_db = {
    "mouredev":{
        "username": "mouredev",
        "full_name": "Nicolas Montoya",
        "email": "montoyanicolas.com",
        "disabled": False,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$CeTL468vsqbjbtw9RIcUdA$vc2jtNd208mnCzOkDL2lJygmd8xnMd+4rjC86d5W46I"
    },
    "mouredev2":{
        "username": "mouredev2",
        "full_name": "Nicolas Montoya 2",
        "email": "montoyanicolas2.com",
        "disabled": True,
        "password": "$argon2id$v=19$m=65536,t=3,p=4$HfNBQN6yX0tcHRO4DCMnCQ$GmmgEO1okRgh+Kf+2zBrmO9MF34qTKWHpBcrmT4oaKQ"
    }

}


# --- Funciones auxiliares de búsqueda ---
def search_user_db(username: str):
    """Retorna el modelo con contraseña desde la DB simulada."""
    if username in users_db:
        return UserDB(**users_db[username])

def search_user(username: str):
    """Retorna el modelo público (sin contraseña) desde la DB simulada."""
    if username in users_db:
        return User(**users_db[username])


# --- Dependencias de autenticación ---
async def auth_user(token: str = Depends(oauth2)):
    """Valida el token JWT recibido y retorna el usuario correspondiente."""
    exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail="Credenciales de autenticación inválidas",
            headers={"WWW-Authenticate": "Bearer"})

    try:
        # Decodifica el token para obtener el 'sub' (username)
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception
        
    except JWTError:
        raise exception
    
    return search_user(username)

async def current_user(user: User = Depends(auth_user)):
    """Verifica si el usuario autenticado está activo antes de proceder."""
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail="Usuario inactivo")
            
    return user


# --- Rutas (Endpoints) ---
@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """Valida usuario y contraseña, y retorna un token JWT."""
    user_db = users_db.get(form.username )
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="El usuario no es correcto")
    
    user = search_user_db(form.username)

    # Verifica que la contraseña del formulario coincida con el hash
    if not pwd_context.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")
    
    # expire Revisamos cuando expira el token, con la hora del sistema le sumamos el valor de la constante
    acces_token = {"sub":user.username, 
                       "exp":datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(acces_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"} 


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    """Endpoint protegido para obtener los datos del usuario actual."""
    return user