from pydantic import BaseModel

# Modelo de entrada de datos
class SepsisInput(BaseModel):
    frecuencia_cardiaca: float
    presion_arterial: float
    frecuencia_respiratoria: float
    temperatura_corporal: float
    saturacion_oxigeno: float
    procalcitonina: float
    lactato: float
    proteina_creactiva: float
    leucocitos: float

class model:
    def update(self, dt: SepsisInput):
        self.dt = dt


    def predict_probability(self):
        # Aquí va la lógica real cuando tengas el modelo entrenado
        # Por ahora simulamos con un porcentaje aleatorio
        # Convertimos el objeto a diccionario para acceder fácilmente a los valores
        valores = self.dt.dict().values()
        promedio = sum(valores) / len(valores)

        
        return round(promedio, 2)  # Devolvemos el promedio redondeado
        
    




