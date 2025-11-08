from pydantic import BaseModel
class DataJson(BaseModel) :

    nodes : list[str]
    timepo_op : list[float]
    tiempo_es : list[float]
    tiempo_pe : list[float]

  

   
    