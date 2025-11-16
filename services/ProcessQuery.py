from BD.Conexion import ConectionBD
from sqlalchemy import text
import pandas as pd
from services.ResponseQuery import ResponseQuery
from services.Response import Response


class ProcessQuery:

    def __init__(self):
        self.responseQ = ResponseQuery()
        self.conexion = ConectionBD().getConection()

    def fetch_non_empty(self, cursor):
        while True:
            rows = cursor.fetchall()
            if rows:  
                return rows
            if not cursor.nextset(): 
                return []

    def getTiempos(self):
        query = "SELECT * FROM dbo.TiemposSet"
        dt = pd.read_sql(query, self.conexion)
        if dt is not None:
            return self.responseQ.dataTiempos(dt)

    def getSimulaciones(self):
        query = "SELECT id_simulacion, nombre_proyecto FROM dbo.Simulacion"
        dt = pd.read_sql(query, self.conexion)
        if dt is not None:
            return self.responseQ.dataSimulaciones(dt)

    def getDataTiempos(self, id):
        try:
            query = f"SELECT * FROM dbo.TiemposDetalle WHERE id_tiempos = {id}"
            dt = pd.read_sql(query, self.conexion)
            if dt is not None:
                return self.responseQ.dataTables(dt)
        except Exception as e:
            print(e)
            return None

    def saveSimulacion(self, data):
        try:
            engine = self.conexion

            with engine.begin() as conn:

                # Insert simulación
                query = text("""
                    INSERT INTO dbo.Simulacion(
                        nombre_proyecto, id_tiempos, duracion_A, ruta_critica_A,
                        duracion_B, ruta_critica_B
                    )
                    OUTPUT INSERTED.id_simulacion 
                    VALUES(:nombre, :id_tiempos, :da, :rcA, :db, :rcB)
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

                # Insert actividades
                insert_act = text("""
                    INSERT INTO dbo.Actividad (id_simulacion, id_detalle, te, tipo) 
                    VALUES (:id_sim, :id_detalle, :te, :tipo)
                """)

                actividadesA = [
                    {"id_sim": id_sim, "id_detalle": a["id_detalle"], "te": a["te"], "tipo": "A"}
                    for a in data["actividadesA"]
                ]

                actividadesB = [
                    {"id_sim": id_sim, "id_detalle": b["id_detalle"], "te": b["te"], "tipo": "B"}
                    for b in data["actividadesB"]
                ]

                conn.execute(insert_act, actividadesA)
                conn.execute(insert_act, actividadesB)

                # Insert nodos
                insert_nodo = text("""
                    INSERT INTO dbo.NodoSimulacion 
                    (id_simulacion, nodo, early, late, holgura, critical, tipo)
                    VALUES(:id_sim, :nodo, :early, :late, :holgura, :critical, :tipo)
                """)

                nodosA = [
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

                nodosB = [
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

                conn.execute(insert_nodo, nodosA)
                conn.execute(insert_nodo, nodosB)

                # Insert resultado
                insert_result = text("""
                    INSERT INTO dbo.Resultado (id_simulacion, varianza_total, probabilidad_30_sem)
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

    # ----------------------------------------------------------------------
    def getDataSimulacion(self, id_sim):
        try:
            conn = self.conexion.raw_connection()
            cursor = conn.cursor()

            cursor.execute("EXEC SP_ObtenerSimulacion ?", id_sim)

            row = cursor.fetchone()
            if not row:
                return None

            response = {
                "SemanasC1": row.SemanasC1,
                "pathA": eval(row.pathA),
                "SemanasC2": row.SemanasC2,
                "pathB": eval(row.pathB),
                "varianza": float(row.varianza),
                "probabilidad": float(row.probabilidad),
            }

            # Nodos A
            cursor.nextset()
            nodosA = self.fetch_non_empty(cursor)
            response["nodesA"] = [
                {
                    "id": r.id,
                    "early": r.early,
                    "latest": r.latest,
                    "holgura": r.holgura,
                    "critical": bool(r.critical)
                }
                for r in nodosA
            ]

            # Nodos B
            cursor.nextset()
            nodosB = self.fetch_non_empty(cursor)
            response["nodesB"] = [
                {
                    "id": r.id,
                    "early": r.early,
                    "latest": r.latest,
                    "holgura": r.holgura,
                    "critical": bool(r.critical)
                }
                for r in nodosB
            ]

            # Tiempos A
            cursor.nextset()
            tiemposA = self.fetch_non_empty(cursor)
            response["tiemposPert_A"] = {
                r.edge: r.tiempo_pert
                for r in tiemposA
            }

            
            cursor.nextset()
            tiemposB = self.fetch_non_empty(cursor)
            response["tiemposPert_B"] = {
                r.edge: r.tiempo_pert
                for r in tiemposB
            }

            cursor.close()
            conn.close()

            return response

        except Exception as e:
            print("Error :", e)
            return None
