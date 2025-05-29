

class model:
    def predict_probability(self,lista):
        # Aquí va la lógica real cuando tengas el modelo entrenado
        # Por ahora simulamos con un porcentaje aleatorio
        porcentaje = 0
        for i in range(len(lista)):
            porcentaje= porcentaje + lista[i]
            porcentaje = porcentaje/ len(lista)
        return porcentaje
        # porcentaje = round(random.uniform(10, 90), 2)
       
    




