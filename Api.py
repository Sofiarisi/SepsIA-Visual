from fastapi import FastAPI
import numpy as np
from modelito import model, SepsisInput  # Esto va si ya tenés el modelo cargado
import uvicorn

    
app = FastAPI()




@app.post("/analizar")
def predict_probability(datos: SepsisInput):
    instancia = model()
    #intancia es unna instancia de model que corre la funcion innit (no self) por qeu nose puede usar las funciones de unna clase sin intanciarla
    if datos.sexo == "femenino" :
        datos.sexo= 1
    else:
        datos.sexo=0

    instancia.update(datos)
    prob = instancia.predict_probability()
    #return {"mensaje": f"{prob}"}
    print(prob)
    return {"a": prob}



uvicorn.run(app, host="0.0.0.0")