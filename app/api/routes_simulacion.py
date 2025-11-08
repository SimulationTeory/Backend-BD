from fastapi import APIRouter
from app.model.model import DataJson
from app.services.process import Process

router = APIRouter()

@router.post("/")
def  simulacion(data :DataJson):
    process = Process()
    e = process.processData(data)


    return e