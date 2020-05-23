# Modulo que prove o labirinto

import pygame, support
from pygame.locals import *
from pygame.sprite import *

# Objetos presentes no labirinto
class Porta:
    def __init__(self, x, y):
        self.image = support.carrega_imagem('porta1.png')
        self.rect = Rect(x, y, 40, 40)
        
class Saida:
    def __init__(self, x, y):
        Sprite.__init__(self)
        self.image = support.carrega_imagem('porta2.png')
        self.rect = self.image.get_rect(center=(x, y))

class Parede(Sprite):
    def __init__(self, x, y, nivel):
        Sprite.__init__(self)
        self.image = support.carrega_imagem('parede%d.png' % nivel)
        self.rect = self.image.get_rect(center=(x, y))

class Objeto(Sprite):
    def __init__(self, x, y, nivel):
        Sprite.__init__(self)
        self.image = support.carrega_imagem('objeto%d.png' % nivel)
        self.rect = Rect(x, y, 20, 20)
        
class Labirinto(Sprite):
    
    # Inicializar componentes
    def __init__(self, nivel):
        self.porta = support.carrega_imagem('porta1.png')
        self.saida = support.carrega_imagem('porta2.png')
        self.parede = support.carrega_imagem('parede%d.png' % nivel)
        self.objeto = support.carrega_imagem('objeto%d.png' % nivel)
        
    # Desenhar labirinto
    def constroi(self, tela, nivel):
        labirinto = support.carrega_labirinto(nivel)
        y = 84
        # Cada linha
        for linha in labirinto:
            x = 112
            # Cada coluna
            for letra in linha:
                if letra == "#":
                    tela.blit(self.parede, (x, y))
                elif letra == "s":
                    tela.blit(self.porta, (x, y))
                elif letra == "f":
                    tela.blit(self.saida, (x, y))
                x += 40
            y += 40
    
    # Cria a lista de objetos contidos no labirinto
    def cria_objetos(self, paredes, objetos, nivel):
        labirinto = support.carrega_labirinto(nivel)
        y = 84
        for linha in labirinto:
            x = 112
            for letra in linha:
                if letra == '#':
                    paredes.add(Parede(x, y, nivel))
                elif letra == 'o':
                    objetos.add(Objeto(x, y, nivel))
                x += 40
            y += 40

