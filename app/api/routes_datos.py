from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def get_data():

    return {"mes":"Hola mundo"}