# Modulos
import support
import pygame, sys
from pygame.locals import *

# Funcao principal
def main(tela):
    fundo = support.carrega_imagem('tela_jogo.jpg')
    font1 = support.carrega_fonte('tallpaul.ttf', 80)
    font1.set_bold(True)
    font2 = support.carrega_fonte('tallpaul.ttf', 60)
    # Loop
    while True:
        # Eventos
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return
                if event.key == K_RETURN:
                    return
        # Texto
        tela.blit(fundo, (0, 0))
        text1 = font1.render("Ajuda?", 1, (10, 10, 10))
        text1_rect = text1.get_rect()
        text1_rect.topright = (924, 200)
        text2 = font2.render("Pegue todos os objetos", 1, (10, 10, 10))
        text2_rect = text2.get_rect()
        text2_rect.topright = (924, 280)
        text3 = font2.render("sem esbarrar no impata!", 1, (10, 10, 10))
        text3_rect = text3.get_rect()
        text3_rect.topright = (924, 340)
        text4 = font1.render("Have Fun!!!", 1, (10, 10, 10))
        text4_rect = text4.get_rect()
        text4_rect.topright = (724, 520)
        text5 = font2.render("Enter para voltar", 1, (10, 10, 10))
        text5_rect = text5.get_rect()
        text5_rect.topright = (924, 650)
        
        tela.blit(text1, text1_rect)
        tela.blit(text2, text2_rect)
        tela.blit(text3, text3_rect)
        tela.blit(text4, text4_rect)
        tela.blit(text5, text5_rect)
        pygame.display.update()
