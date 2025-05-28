from modelito import model
instancia = model()
#pirulo es unna instancia de model que corre la funcion in1,2,nit (no self) por qeu nose puede usar las funciones de unna clase sin intanciarla
# Si ya tenés un modelo entrenado, usá esto:

class SepsisInput:
    def __init__(self, HeartRate, Temperature, RespirationRate):
        self.HeartRate = HeartRate
        self.Temperature = Temperature
        self.RespirationRate = RespirationRate
    
datos = SepsisInput(1,2,3)



valores = [datos.HeartRate, datos.Temperature, datos.RespirationRate]
prob = instancia.predict_probability(valores)

print (f"La probabilidad de sepsis es del {prob}%.")