from fastapi import FastAPI
from app.api import routes_simulacion,routes_datos

app = FastAPI()

app.include_router(routes_simulacion.router,prefix="/api/simulacion")
app.include_router(routes_datos.router,prefix="/api/datos")
