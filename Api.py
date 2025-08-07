# from fastapi import FastAPI
# import numpy as np
# from modelito import model, SepsisInput  # Esto va si ya tenés el modelo cargado
# import uvicorn

    
# app = FastAPI()




# @app.post("/analizar")
# def predict_probability(datos: SepsisInput):
#     print("Se corre en el modelo correcto")
#     instancia = model()
#     #intancia es unna instancia de model que corre la funcion innit (no self) por qeu nose puede usar las funciones de unna clase sin intanciarla
 

#     instancia.update(datos)
#     prob = instancia.predict_probability()
#     #return {"mensaje": f"{prob}"}
#     print(prob)
#     return {"a": prob}



# uvicorn.run(app, host="0.0.0.0")

from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import uvicorn

# Crear app
app = FastAPI()

# Cargar modelo entrenado
modelo = joblib.load("modelo_xgboost.pkl")
print("Modelo cargado correctamente")

# Definir el esquema de datos que vas a recibir (ejemplo con 4 signos vitales)
class DatosEntrada(BaseModel):
    frecuencia_cardiaca: float
    presion_arterial: float
    frecuencia_respiratoria: float
    temperatura_corporal: float
    saturacion_oxigeno: float
    #procalcitonina: float
    lactato: float
    #proteina_creactiva: float
    leucocitos: float

# Endpoint de predicción
@app.post("/analizar")

def analizar(datos: DatosEntrada):
    entrada = np.array([[  # Convertimos a un array 2D para el modelo
    datos.frecuencia_cardiaca,
    datos.presion_arterial,
    datos.frecuencia_respiratoria,
    datos.temperatura_corporal,
    datos.saturacion_oxigeno,
    #datos.procalcitonina,
    datos.lactato,
    #datos.proteina_creactiva,
    datos.leucocitos
    ]])
    print("Los datos entraron")
    try:
        prediccion = modelo.predict(entrada)
        print("el resultado es ", prediccion[0])
        return {"resultado": prediccion[0]}
    except Exception as e:
        print("Error en la predicción:", e)
        return {"error": str(e)}

    # prediccion = modelo.predict(entrada)
    # print("el resultad es ", prediccion[0])
    # return {"resultado": prediccion[0]}
uvicorn.run(app, host="0.0.0.0")