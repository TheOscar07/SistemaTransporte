import networkx as nx
from experta import *

class MejorRuta(KnowledgeEngine):
    """Motor de inferencia basado en reglas lógicas para encontrar la mejor ruta."""
    
    @DefFacts()
    def _init_facts(self):
        yield Fact(mejor_ruta=None)
    
    @Rule(Fact(origen=MATCH.origen), Fact(destino=MATCH.destino))
    def calcular_ruta(self, origen, destino):
        ruta = nx.shortest_path(self.grafo, origen, destino, weight='peso')
        print(f"La mejor ruta de {origen} a {destino} es: {ruta}")
        self.declare(Fact(mejor_ruta=ruta))

class SistemaTransporte:
    """Clase principal para gestionar el sistema de transporte."""
    
    def __init__(self):
        self.grafo = nx.Graph()
        self.agregar_estaciones()
        self.motor = MejorRuta()
        self.motor.grafo = self.grafo
    
    def agregar_estaciones(self):
        """Define las estaciones y conexiones con sus respectivos pesos."""
        conexiones = [
            ("A", "B", 10),
            ("B", "C", 15),
            ("A", "C", 30),
            ("C", "D", 10),
            ("B", "D", 25)
        ]
        for origen, destino, peso in conexiones:
            self.grafo.add_edge(origen, destino, peso=peso)
    
    def encontrar_mejor_ruta(self, origen, destino):
        self.motor.reset()
        self.motor.declare(Fact(origen=origen, destino=destino))
        self.motor.run()

if __name__ == "__main__":
    sistema = SistemaTransporte()
    sistema.encontrar_mejor_ruta("A", "D")
