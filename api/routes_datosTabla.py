from fastapi import APIRouter
from services.ProcessQuery import ProcessQuery

router = APIRouter()

@router.post("/Tiempos")
def getTiempos():
    p = ProcessQuery()
    data = p.getTiempos()
    return data

@router.post("/dataTiempos")
def  getdataTiempos(id : int):
    process = ProcessQuery()
    result = process.getDataTiempos(id)
    print(result)    
    return result




