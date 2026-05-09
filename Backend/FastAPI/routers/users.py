from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Entidad User
class User(BaseModel):
    id: int
    name: str
    surname: str  
    url: str
    age: int


users_list = [User(id=1, name = "Nicolas", surname = "Montoya", url ="https://nicolas.com", age = 29),
              User(id= 2, name = "Melissa", surname = "Montoya", url = "https://melissa.com", age = 27),
              User(id= 3, name = "Jairo", surname = "Dahlberg", url = "https://jairo.com", age = 50)]

@router.get("/usersjson")
async def usersjson():
    return [{"name": "Nicolas","surname": "montoya", "url": "https://mouredev.com/", "age": 29},
            {"name": "Melissa","surname": "montoya", "url": "https://melissa.com/", "age": 29},
            {"name": "Jairo","surname": "montoya", "url": "https://jairo.com/", "age": 29}]



@router.get("/users")
async def users():
    return users_list

# Path - Primera forma 
'''
@router.get("/user/{id}")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "no se ha encontrado el usuario"}
    
# Query

@router.get("/userquery/")
async def user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "no se ha encontrado el usuario"}
'''

# Segunda forma - Con función 

@router.get("/user/{id}")
async def user(id: int):
    return search_user(id)

@router.get("/user/") 
async def user(id: int):
    return search_user(id)


@router.post("/user/", response_model=User,status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
        
    else:
        users_list.append(user)
        return user


@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"Error": "No se ha actualizado el usuario"}
    else:
        return user


@router.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True

    if not found:
        return {"Error": "No se ha eliminado el usuario"}





def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "No se ha encontrado el usuario"}
    
