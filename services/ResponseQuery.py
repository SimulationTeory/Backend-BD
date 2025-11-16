import pandas as pd

class ResponseQuery:

    def dataTiempos(self, data):
     result = []

     ids = list(data["id_tiempos"])
     nombres = list(data["nombre"])

     for i in range(len(ids)):
        result.append({
            "id": ids[i],
            "nombre": nombres[i]
        })

     return result



    def dataTables(self, data):
        table = {}
        nodos = []
        nodesA = list(data['nodo_inicio'])
        nodesB =list( data['nodo_fin'])
        for i in range(0,len(nodesA)) :
            nodos.append( f"{nodesA[i]}-{nodesB[i]}")
        table["Nodos"] = nodos
        table["Tiempo_optimitsa"]  = list(data["a"])
        table["Tiempo_probable"]   = list(data["m"])
        table["Tiempo_pesimista"]  = list(data["b"])
        table["id"] = list(data["id_detalle"])

        
        return table

    def dataSimulaciones(self, data):
     result = []

     ids = list(data["id_simulacion"])
     nombres = list(data["nombre_proyecto"])

     for i in range(len(ids)):
        result.append({
            "id": ids[i],
            "nombre": nombres[i]
        })


     return result

    
    
    
   
       
       

    


