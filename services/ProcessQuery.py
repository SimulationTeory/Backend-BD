from BD.Conexion import ConectionBD
from sqlalchemy import text
import pandas as pd
from services.ResponseQuery import ResponseQuery
from services.Response import Response

class ProcessQuery:

    def __init__(self):
       self.responseQ = ResponseQuery()
       

    def getTiempos(self):
        query = "select * from dbo.TiemposSet"
        conexion = ConectionBD().getConection()
        dt = pd.read_sql(query,conexion)
        if(dt is not None):
            result = self.responseQ.dataTiempos(dt)
            return result

    def getDataTiempos(self,id):
        try:
            self.id = id
            query = f"select * from dbo.TiemposDetalle  where id_tiempos = {id} "
            conexion = ConectionBD().getConection()
            dt =  pd.read_sql(query,conexion)
            if (dt is not None):
               data = self.responseQ.dataTables(dt)
               
              

        except Exception as e:
            print(e)
            return None
        return data
    
    def saveData(self, name):
   
        return True





       






