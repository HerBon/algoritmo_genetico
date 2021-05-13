import random


class poblacion:
    def __init__(self, estado, proba_vida):
        self.estado = estado
        self.proba_vida = proba_vida

    def seleccionar_mejor(self, problacion1):
        
        
        pass




    
def generar_poblacion():
    poblacion1 = []
    for f in range(8):
        poblacion1.append([])
        for c in range(8):
            poblacion1[f].append(random.randint(0, 1))
    return poblacion1

poblacion_inicio = generar_poblacion()
def escoger_mejores():
    
    pass

#print(generar_poblacion())
'''
person1= personas([1,1,0,0,0,1],0.1)

print(person1.estado)
'''