# Backend-BD
Backend en Python, FastAPI, para una lógica del proyecto
---
#Requerimientos
- python 3.13.3

- Librerías necesarias:
- nextworkx -> pip install networkx
- pandas -> pip install pandas 
- fastapi -> pip install fastapi 
- matplotlib -> pip install matplotlib
- servidor uvicorn -> pip install uvicorn 

- Ejecutar el servidor: uvicorn main:app --reload
  http://localhost:8000/docs

---
---
#Datos de prueba 
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
---
