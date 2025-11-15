from fastapi import APIRouter
from services.ProcessQuery import ProcessQuery
from model.SaveData import SaveData

router = APIRouter()

@router.post("/")
def saveData(data : SaveData ):

    process = ProcessQuery()
    result = process.saveSimulacion(data.model_dump())
    print(result)
    return result


    