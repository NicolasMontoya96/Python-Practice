from fastapi import APIRouter

router = APIRouter(prefix="/products", 
                   tags=["products"],
                   responses={404: {"message": "No encontrado"}})


products_list = ["Producto 1", "Producto 2", "Producto 3"]

@router.get("/")
async def products():
    return ["Producto 1", "Producto 2", "Producto 3"]


@router.get("/{id}")
async def products(id: int):
    return products_list[id]