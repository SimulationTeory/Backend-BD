from fastapi import APIRouter, HTTPException
from model.model import DataSimulacion
from services.process import Process

router = APIRouter()

@router.post("/")
def simulacion(data: DataSimulacion):
    
    n_nodes = len(data.nodes)
    if not (len(data.tiempo_op) == len(data.tiempo_es) == len(data.tiempo_pe) == n_nodes):
        raise HTTPException(
            status_code=422,
            detail="Las listas nodes, tiempo_op, tiempo_es y tiempo_pe deben tener la misma longitud"
        )

    process = Process()
    result = process.processData(data)
    return result
