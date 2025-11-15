# Backend-BD
Backend en Python, FastAPI, para una lógica del proyecto
---
# Requerimientos
- python 3.13.3

- Librerías necesarias:
- nextworkx -> pip install networkx
- pandas -> pip install pandas 
- fastapi -> pip install fastapi 
- matplotlib -> pip install matplotlib
- servidor uvicorn -> pip install uvicorn 

- Ejecutar el servidor : uvicorn main:app --reload
  http://localhost:8000/docs


# Datos de prueba 
{
   "nodes": [
"0−20","20−40","40−60","20−50","50−70","70−90","0−10","10−30","30−80","0−30","20−60","60−80",
"80−90"

  ],
  "timepo_op": [
  4,2,3,1,1,4,1,4,4,9,5,4,3

  ],
  "tiempo_es": [
  5.5,4,6,2,4,10,2,10.5,6,13,9,5.5,5.5
  ],
  "tiempo_pe": [
   10,6,15,3,7,16,3,14,8,17,13,10,11

  ]
}
 # para guardar en la BD
{
  "id_tiempos": 1,
  "nombre": "Simulación Proyecto X",

  "SemanasC1": 29,
  "SemanasC2": 27,

  "rutaCriticaA": ["0-20", "20-40", "40-60", "60-80", "80-90"],
  "rutaCriticaB": ["0-20", "20-60", "60-80", "80-90"],

  "varianza_total": 2.36,
  "probabilidad": 0.898,

  "actividades": [
    { "id_detalle": 1, "te": 6, "varianza": 1.0 },
    { "id_detalle": 2, "te": 4, "varianza": 0.5 },
    { "id_detalle": 3, "te": 6, "varianza": 1.2 },
    { "id_detalle": 4, "te": 2, "varianza": 0.22 },
    { "id_detalle": 5, "te": 4, "varianza": 0.44 },
    { "id_detalle": 6, "te": 10, "varianza": 2.0 },
    { "id_detalle": 7, "te": 2, "varianza": 0.11 },
    { "id_detalle": 8, "te": 10, "varianza": 2.0 },
    { "id_detalle": 9, "te": 6, "varianza": 1.0 },
    { "id_detalle": 10, "te": 13, "varianza": 3.0 },
    { "id_detalle": 11, "te": 9, "varianza": 1.2 },
    { "id_detalle": 12, "te": 6, "varianza": 0.9 },
    { "id_detalle": 13, "te": 10, "varianza": 2.0 }
  ],

  "nodesA": [
    { "nodo": 0,  "early": 0,  "late": 0,  "holgura": 0,  "critical": true },
    { "nodo": 10, "early": 2,  "late": 7,  "holgura": 5,  "critical": false },
    { "nodo": 20, "early": 6,  "late": 6,  "holgura": 0,  "critical": true },
    { "nodo": 30, "early": 13, "late": 17, "holgura": 4, "critical": false },
    { "nodo": 40, "early": 10, "late": 10, "holgura": 0, "critical": true },
    { "nodo": 50, "early": 8,  "late": 15, "holgura": 7, "critical": false },
    { "nodo": 60, "early": 17, "late": 17, "holgura": 0, "critical": true },
    { "nodo": 70, "early": 12, "late": 19, "holgura": 7, "critical": false },
    { "nodo": 80, "early": 23, "late": 23, "holgura": 0, "critical": true },
    { "nodo": 90, "early": 29, "late": 29, "holgura": 0, "critical": true }
  ],

  "nodesB": [
    { "nodo": 0,  "early": 0,  "late": 0,  "holgura": 0,  "critical": true },
    { "nodo": 10, "early": 2,  "late": 5,  "holgura": 3,  "critical": false },
    { "nodo": 20, "early": 6,  "late": 6,  "holgura": 0,  "critical": true },
    { "nodo": 30, "early": 13, "late": 15, "holgura": 2,  "critical": false },
    { "nodo": 40, "early": 6,  "late": 8,  "holgura": 2,  "critical": false },
    { "nodo": 50, "early": 8,  "late": 13, "holgura": 5,  "critical": false },
    { "nodo": 60, "early": 15, "late": 15, "holgura": 0,  "critical": true },
    { "nodo": 70, "early": 12, "late": 17, "holgura": 5,  "critical": false },
    { "nodo": 80, "early": 21, "late": 21, "holgura": 0,  "critical": true },
    { "nodo": 90, "early": 27, "late": 27, "holgura": 0,  "critical": true }
  ]
}


