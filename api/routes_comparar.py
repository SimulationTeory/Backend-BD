from fastapi import APIRouter
from services.ProcessQuery import ProcessQuery

router = APIRouter()

@router.post("/getSimulaciones")

def getSimulaciones():
    p = ProcessQuery()
    result = p.getSimulaciones()
    return result 

@router.post("/dataSimulaciones")
def dataSimulaciones(id_s1 : int,id_s2 : int):
    p = ProcessQuery()
    result = []
    result.append(p.getDataSimulacion(id_s1))
    result.append(p.getDataSimulacion(id_s2))

    return result

