from app.BD.Conexion import ConectionBD
from sqlalchemy import text
import pandas as pd

class ProcessQuery:

    def getData(self,id):
        
        try:
            query = f"select * from dbo.TiemposDetalle where id_tiempos = {id} "
            conexion = ConectionBD().getConection()
            dt =  pd.read_sql(query,conexion)
            print(dt)
        except Exception as e:
         print(e)
         return None 







