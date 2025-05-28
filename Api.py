from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import random  # Solo usalo si no tenés el modelo todavía
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
    # Simulación del modelo (usá esto si todavía no cargaste uno real)
    
    instancia = model()
    #pirulo es unna instancia de model que corre la funcion innit (no self) por qeu nose puede usar las funciones de unna clase sin intanciarla
    # Si ya tenés un modelo entrenado, usá esto:
    valores = [datos.HeartRate, datos.Temperature, datos.RespirationRate]
    prob = instancia.predict_probability(valores)
    # porcentaje = round(prob * 100, 2)

    # Devolver mensaje como texto
    return {"mensaje": f"La probabilidad de sepsis es del {prob}%."}


uvicorn.run(app)