from fastapi import APIRouter
from BD.ProcessQuery import ProcessQuery

router = APIRouter()

@router.post("/")
def get_data(id : int):

    process = ProcessQuery()
    process.getData(id)

    