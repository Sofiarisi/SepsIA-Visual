from pydantic import BaseModel

# Modelo de entrada de datos
class SepsisInput(BaseModel):
    edad: int
    sexo: str
    frecuenciacardiaca: float
    presionarterial: float
    frecuenciarespiratoria: float
    temperatura: float
    saturacion: float
    procalcitonina: float
    lactato: float
    proteinacreactiva: float
    leucocitos: float

class model:
    def update(self, dt: SepsisInput):
        self.dt = dt


    def predict_probability(self):
        # Aquí va la lógica real cuando tengas el modelo entrenado
        # Por ahora simulamos con un porcentaje aleatorio
        # porcentaje = 0
        # for i in range(len(lista)):
        #     porcentaje= porcentaje + lista[i]
        #     porcentaje = porcentaje/ len(lista)
        # return porcentaje
        # # porcentaje = round(random.uniform(10, 90), 2)
        return self.dt
    




