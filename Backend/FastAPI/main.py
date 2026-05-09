from fastapi import FastAPI
from routers import products, users, jwt_auth_users, basic_auth_user, users_db
from fastapi.staticfiles import StaticFiles
import os
from dotenv import load_dotenv

load_dotenv()
app = FastAPI()

# Routers
# Al añadir un prefijo, FastAPI sabrá diferenciar dónde está cada ruta
app.include_router(products.router, prefix="/products")
app.include_router(users.router, prefix="/users")
app.include_router(basic_auth_user.router, prefix="/basic")
app.include_router(users_db.router)
app.include_router(jwt_auth_users.router, prefix="/jwt")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return "Hola FastAPI!"

@app.get("/url")
async def url():
    return {"url":"https://mouredev.com/python"}

