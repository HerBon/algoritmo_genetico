import copy 

class nodo():
    def __init__(self, estado, padre):
        self.estado = estado
        self.padre = padre

    def generar_hijos(self):
        
        self.hijos = []
        for c in range(len(self.estado)-1):
            hijo = copy.deepcopy(self.estado)
            hijo[c] = self.estado[c+1]
            hijo[c+1]=self.estado[c]
            self.hijos.append(hijo)
        return self.hijos

nodo_inicial = nodo([2,3,5,1,4],None)
#print(nodo_inicial.generar_hijos())

estado_solucion = [1,2,3,4,5]
def busqueda_anchura():
    no_visitados=[]
    visitados = []
    visitados.append(nodo_inicial)

    


    pass


