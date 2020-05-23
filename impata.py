# Modulo que prove o impata

import pygame, random, support, vector2d
from pygame.locals import *
from pygame.sprite import *

clock = pygame.time.Clock()

class Impata(Sprite):
    
    # Inicializacao dos atributos
    def __init__(self, x, y, nivel, *grupos):
        Sprite.__init__(self, *grupos)
        self.image = support.carrega_imagem('impata%d.png' % nivel)
        self.rect = Rect(x, y, 30, 30)
        #self.rect.inflate(-10, -10)
        self.velocidade = 200.
        self.posicao = vector2d.Vector2(x, y)
        self.pos_temp = vector2d.Vector2()
        self.direcao = vector2d.Vector2(-1, 0)

    # Metodo que movimenta o impata
    def move(self):
        self.pos_temp.x, self.pos_temp.y = self.posicao.x, self.posicao.y
        tempo = clock.tick(60)
        tempo_segundos = tempo / 1000.0
        self.posicao += self.direcao * self.velocidade * tempo_segundos
        self.rect.center = (self.posicao.x , self.posicao.y)

    # Metodo que retorna o impata a posicao anterior
    def volta(self):
        self.posicao.x, self.posicao.y = (self.pos_temp.x, self.pos_temp.y)
        self.rect.center = (self.pos_temp.x, self.pos_temp.y)

