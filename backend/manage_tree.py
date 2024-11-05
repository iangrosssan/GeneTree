import networkx as nx
from class_miembro import Miembro

class ArbolGenealogico():
    def __init__(self):
        self.grafo = nx.MultiDiGraph()
    
    def agregar_miembro(self, miembro):
        self.grafo.add_node(miembro)
    
    def conectar_progenitor_descendencia(self, padre, madre, hijo):
        self.grafo.add_edge(padre, hijo)
        self.grafo.add_edge(madre, hijo)
        self.conectar_conyuges(padre, madre)
        hijo.agregar_progenitores(padre, madre)
    
    def conectar_conyuges(self, miembro1, miembro2):
        self.grafo.add_edge(miembro1, miembro2)
        self.grafo.add_edge(miembro2, miembro1)
        miembro1.agregar_conyuge(miembro2)
    
    def obtener_parientes(self, miembro):
        predecesores = list(self.grafo.predecessors(miembro))
        sucesores = list(self.grafo.successors(miembro))
        conyuges = list(set(predecesores).intersection(sucesores))
        predecesores = [item for item in predecesores if item not in conyuges]
        sucesores = [item for item in sucesores if item not in conyuges]
        
        padre = next((p for p in predecesores if p.sexo == "M"), None)
        madre = next((m for m in predecesores if m.sexo == "F"), None)
        if predecesores:
            miembro.agregar_progenitores(padre, madre)

        return miembro.obtener_parientes()


arbol = ArbolGenealogico()

alejandro = Miembro("Alejandro", "M")
paulina = Miembro("Paulina", "F")
marcos = Miembro("Marcos", "M")
marissa = Miembro("Marissa", "F")

alan = Miembro("Alan", "M")
ian = Miembro("Ian", "M")
daniela = Miembro("Daniela", "F")
valeria = Miembro("Valeria", "F")

arbol.agregar_miembro(alejandro)
arbol.agregar_miembro(paulina)
arbol.agregar_miembro(marcos)
arbol.agregar_miembro(alan)
arbol.agregar_miembro(ian)
arbol.agregar_miembro(daniela)
arbol.agregar_miembro(valeria)


arbol.conectar_progenitor_descendencia(alejandro, paulina, ian)
arbol.conectar_progenitor_descendencia(alejandro, paulina, alan)
arbol.conectar_progenitor_descendencia(marcos, marissa, daniela)
arbol.conectar_progenitor_descendencia(marcos, paulina, valeria)

print(arbol.obtener_parientes(alejandro))
print(arbol.obtener_parientes(paulina))
print(arbol.obtener_parientes(marcos))
print(arbol.obtener_parientes(marissa))
print(arbol.obtener_parientes(ian))
print(arbol.obtener_parientes(alan))
print(arbol.obtener_parientes(daniela))
print(arbol.obtener_parientes(valeria))
