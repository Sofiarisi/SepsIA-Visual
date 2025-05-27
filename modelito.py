import random 

class model:
    def predict_probability(self, heart_rate, temperature, respiration_rate):
        # Aquí va la lógica real cuando tengas el modelo entrenado
        # Por ahora simulamos con un porcentaje aleatorio
        porcentaje = (heart_rate + temperature + respiration_rate)/3
        # porcentaje = round(random.uniform(10, 90), 2)
        return porcentaje
    




