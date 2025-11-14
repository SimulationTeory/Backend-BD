from pydantic import BaseModel

class DataSimulacion(BaseModel):
    """
    Modelo de datos utilizado para recibir la información JSON enviada desde el frontend
    hacia el backend de FastAPI.

    Atributos:
        nodes (list[str]): Lista de identificadores de nodos o actividades del grafo.
        tiempo_op (list[float]): Lista de tiempos optimistas (a) para cada actividad.
        tiempo_es (list[float]): Lista de tiempos más probables (m) para cada actividad.
        tiempo_pe (list[float]): Lista de tiempos pesimistas (b) para cada actividad.
    """
    
    nodes: list[str]
    tiempo_op: list[float]
    tiempo_es: list[float]
    tiempo_pe: list[float]
