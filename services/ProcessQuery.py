from BD.Conexion import ConectionBD
from sqlalchemy import text
import pandas as pd
from services.ResponseQuery import ResponseQuery
from services.Response import Response

class ProcessQuery:
    """
    Clase que gestiona las consultas y operaciones relacionadas con los
    tiempos PERT y el guardado de simulaciones completas en la base de datos.
    """

    def __init__(self):
        """
        Inicializa el objeto con la conexión a la base de datos
        """
        self.responseQ = ResponseQuery()
        self.conexion = ConectionBD().getConection()
       

    def getTiempos(self):
        """
        Obtiene todos los registros de la tabla TiemposSet.

        Returns:
            dict: Lista de sets de tiempos formateados.
        """
        query = "select * from dbo.TiemposSet"
        dt = pd.read_sql(query, self.conexion)
        if(dt is not None):
            result = self.responseQ.dataTiempos(dt)
            return result

    def getDataTiempos(self, id):
        """
        Obtiene los detalles de tiempos (a, m, b) asociados a un set.

        Args:
            id (int): Identificador del TiemposSet.

        Returns:
            dict: Datos formateados de TiemposDetalle.
        """
        try:
            self.id = id
            query = f"select * from dbo.TiemposDetalle where id_tiempos = {id}"
            dt = pd.read_sql(query, self.conexion)
            if (dt is not None):
                data = self.responseQ.dataTables(dt)

        except Exception as e:
            print(e)
            return None
        return data
    

    def saveSimulacion(self, data):
        """
        Guarda en la base de datos una simulación completa.

        Todas las operaciones se realizan dentro de una transacción.

        Args:
            data (dict): Contenido JSON recibido del frontend que incluye
                         tiempos, rutas críticas, actividades y nodos.

        Returns:
            dict: Resultado de la operación con éxito o error.
        """
        try:
            engine = self.conexion

            with engine.begin() as conn:

                query = text("""
                    INSERT INTO dbo.Simulacion(nombre_proyecto, id_tiempos, duracion_A, ruta_critica_A, duracion_B,
                    ruta_critica_B) OUTPUT INSERTED.id_simulacion VALUES(:nombre, :id_tiempos, :da, :rcA, :db, :rcB)
                """)

                id_sim = conn.execute(
                    query,
                    {
                        "nombre": data["nombre"],
                        "id_tiempos": data["id_tiempos"],
                        "da": data["SemanasC1"],
                        "rcA": str(data["rutaCriticaA"]),
                        "db": data["SemanasC2"],
                        "rcB": str(data["rutaCriticaB"])
                    }
                ).scalar_one()

                insert_act = text("""
                    INSERT INTO dbo.Actividad (id_simulacion, id_detalle, te, varianza) 
                    VALUES (:id_sim, :id_detalle, :te, :varianza)
                """)

                actividades_rows = [
                    {
                        "id_sim": id_sim,
                        "id_detalle": act["id_detalle"],
                        "te": act["te"],
                        "varianza": act["varianza"]
                    }
                    for act in data["actividades"]
                ]
                conn.execute(insert_act, actividades_rows)

                nodosA_rows = [
                    {
                        "id_sim": id_sim,
                        "nodo": n["nodo"],
                        "early": n["early"],
                        "late": n["late"],
                        "holgura": n["holgura"],
                        "critical": 1 if n["critical"] else 0,
                        "tipo": "A"
                    }
                    for n in data["nodesA"]
                ]

                nodosB_rows = [
                    {
                        "id_sim": id_sim,
                        "nodo": n["nodo"],
                        "early": n["early"],
                        "late": n["late"],
                        "holgura": n["holgura"],
                        "critical": 1 if n["critical"] else 0,
                        "tipo": "B"
                    }
                    for n in data["nodesB"]
                ]

                insert_nodo = text("""
                    INSERT INTO dbo.NodoSimulacion (id_simulacion, nodo, early, late, holgura, critical, tipo)
                    VALUES(:id_sim, :nodo, :early, :late, :holgura, :critical, :tipo)
                """)

                conn.execute(insert_nodo, nodosA_rows)
                conn.execute(insert_nodo, nodosB_rows)

                insert_result = text("""INSERT INTO dbo.Resultado (id_simulacion, varianza_total, probabilidad_30_sem)
                VALUES (:id_sim, :var_total, :prob)
                """)

                conn.execute(
                    insert_result,
                    {
                        "id_sim": id_sim,
                        "var_total": data["varianza_total"],
                        "prob": data["probabilidad"]
                    }
                )

            return {"ok": True, "id_simulacion": id_sim}

        except Exception as e:
            print("Error al guardar simulación:", e)
            return {"Éxito": False, "error": str(e)}
