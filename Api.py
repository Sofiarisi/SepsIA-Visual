from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
from modelito import model  # Esto va si ya tenés el modelo cargado
import uvicorn

    
app = FastAPI()

# Modelo de entrada de datos
class SepsisInput(BaseModel):
    HeartRate: float
    Temperature: float
    RespirationRate: float

@app.post("/analizar")
def predict_probability(datos: SepsisInput):
    instancia = model()
    #pirulo es unna instancia de model que corre la funcion innit (no self) por qeu nose puede usar las funciones de unna clase sin intanciarla
   
    valores = [datos.HeartRate, datos.Temperature, datos.RespirationRate]
    prob = instancia.predict_probability(valores)
    return {"mensaje": f"La probabilidad de sepsis es del {prob}%."}


uvicorn.run(app, host="0.0.0.0")