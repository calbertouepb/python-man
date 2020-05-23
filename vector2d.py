# Modulo que prove movimentos vetoriais

import math

class Vector2(object):
    # Inicializacao dos atributos
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y
    
    # String representativa
    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)
    
    # Calcula o vetor diretor
    def from_points(self, P1, P2):
        return Vector2(P2[0] - P1[0], P2[1] - P1[1])
    
    # Calcula a distancia entre dois pontos
    def get_magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    # Normaliza o vetor
    def normalize(self):
        magnitude = self.get_magnitude()
        self.x /= magnitude
        self.y /= magnitude
    
    # rhs stands for Right Hand Side
    
    # Adicao de dois vetores
    def __add__(self, rhs):
        return Vector2(self.x + rhs.x, self.y + rhs.y)
    
    # Subtracao de dois vetores
    def __sub__(self, rhs):
        return Vector2(self.x - rhs.x, self.y - rhs.y)
    
    # Inversao de vetor
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    # Multiplicacao de um vetor por um escalar
    def __mul__(self, scalar):
        return Vector2(self.x * scalar, self.y * scalar)
    
    # Divisao de um vetor por um escalar
    def __div__(self, scalar):
        return Vector2(self.x / scalar, self.y / scalar)

