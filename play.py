# Modulo que prove o jogador

import pygame, support, vector2d
from pygame.locals import *
from pygame.sprite import *

clock = pygame.time.Clock()

class Jogador(Sprite):
    
    # Inicializacao dos atributos
    def __init__(self, *grupos):
        Sprite.__init__(self, *grupos)
        self.image = support.carrega_imagem('climber44.png')
        self.rect = Rect(152, 564, 30, 30)
        #self.rect.inflate(-10, -10)
        self.velocidade = 200.
        self.posicao = vector2d.Vector2(152, 564)
        self.pos_temp = vector2d.Vector2()
        self.pontuacao = 0
        self.vidas = 3

    # Metodo que realiza a movimentacao do jogador
    def move(self, direcao):
        self.pos_temp.x, self.pos_temp.y = self.posicao.x, self.posicao.y
        tempo = clock.tick(60)
        tempo_segundos = tempo / 1000.0
        self.posicao += direcao * self.velocidade * tempo_segundos
        self.rect.center = (self.posicao.x , self.posicao.y)

    # Metodo que retorna o jogador para a posicao anterior
    def volta(self):
        self.posicao.x, self.posicao.y = (self.pos_temp.x, self.pos_temp.y)
        self.rect.center = (self.pos_temp.x, self.pos_temp.y)

