from fastapi import APIRouter
from services.ProcessQuery import ProcessQuery
from model.SaveData import SaveData

router = APIRouter()

@router.post("/")
def saveData(data : SaveData ):

    process = ProcessQuery()
    print(data)


    