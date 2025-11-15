from pydantic import BaseModel
from typing import List


class ActividadItem(BaseModel):
    id_detalle: int
    te: float
    varianza: float


class NodoItem(BaseModel):
    nodo: int
    early: float
    late: float
    holgura: float
    critical: bool


class SaveData(BaseModel):
    id_tiempos: int
    nombre: str

    SemanasC1: float
    SemanasC2: float

    rutaCriticaA: List[str]
    rutaCriticaB: List[str]

    varianza_total: float
    probabilidad: float

    actividades: List[ActividadItem]

    nodesA: List[NodoItem]
    nodesB: List[NodoItem]
