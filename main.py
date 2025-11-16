from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api import routes_simulacion, routes_datosTabla,routes_save,routes_comparar

app = FastAPI()

# Routers
app.include_router(routes_simulacion.router, prefix="/api/simulacion")
app.include_router(routes_datosTabla.router, prefix="/api/datosTabla")
app.include_router(routes_save.router, prefix="/api/save")
app.include_router(routes_comparar.router,prefix=("/api/comparar"))



origins = [
    "http://localhost:5173",  
    "http://127.0.0.1:5173",  
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,      
    allow_credentials=True,
    allow_methods=["*"],       
    allow_headers=["*"],       
)
