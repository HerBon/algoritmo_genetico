import random


class personas:
    def __init__(self, estado, proba_vida):
        self.estado = estado
        self.proba_vida = proba_vida

    
def generar_poblacion():


person1= personas([1,1,0,0,0,1],0.1)

print(person1.estado)