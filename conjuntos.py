# conjunto.py

class Conjuntos:
    def __init__(self, elementos):
        self.elementos = set(elementos)  # Usamos set para evitar duplicados

    def complemento(self, universo):
        return Conjuntos(universo.elementos - self.elementos)

    def union(self, otro_conjunto):
        return Conjuntos(self.elementos | otro_conjunto.elementos)

    def interseccion(self, otro_conjunto):
        return Conjuntos(self.elementos & otro_conjunto.elementos)

    def diferencia(self, otro_conjunto):
        return Conjuntos(self.elementos - otro_conjunto.elementos)

    def diferencia_simetrica(self, otro_conjunto):
        return Conjuntos(self.elementos ^ otro_conjunto.elementos)

    def __str__(self):
        return f"{sorted(self.elementos)}"
