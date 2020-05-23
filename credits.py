# Modulos
import support
import pygame, sys
from pygame.locals import *

# Funcao principal
def main(tela):
    fundo = support.carrega_imagem('tela_jogo.jpg')
    font1 = support.carrega_fonte('tallpaul.ttf', 50)
    font1.set_bold(True)
    font2 = support.carrega_fonte('tallpaul.ttf', 40)
    font2.set_bold(True)
    font3 = support.carrega_fonte('tallpaul.ttf', 40)
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
        text1 = font1.render("Creditos:", 1, (10, 10, 10))
        text1_rect = text1.get_rect()
        text1_rect.topright = (924, 200)
        text2 = font2.render("Programadores:", 1, (10, 10, 10))
        text2_rect = text2.get_rect()
        text2_rect.topright = (924, 260)
        text3 = font3.render("Carlos Alberto de Amorim Porto", 1, (10, 10, 10))
        text3_rect = text3.get_rect()
        text3_rect.topright = (924, 290)
        text4 = font3.render("Zeus Cunha Barros", 1, (10, 10, 10))
        text4_rect = text4.get_rect()
        text4_rect.topright = (924, 330)
        text5 = font2.render("Tutor:", 1, (10, 10, 10))
        text5_rect = text5.get_rect()
        text5_rect.topright = (724, 390)
        text6 = font3.render("Jemerson Figueiredo Damasio", 1, (10, 10, 10))
        text6_rect = text6.get_rect()
        text6_rect.topright = (724, 430)
        text7 = font2.render("Professor:", 1, (10, 10, 10))
        text7_rect = text7.get_rect()
        text7_rect.topright = (624, 480)
        text8 = font3.render("Dalton Serey", 1, (10, 10, 10))
        text8_rect = text8.get_rect()
        text8_rect.topright = (624, 520)
        
        text9 = font2.render("Enter para voltar", 1, (10, 10, 10))
        text9_rect = text9.get_rect()
        text9_rect.topright = (924, 668)
        tela.blit(text1, text1_rect)
        tela.blit(text2, text2_rect)
        tela.blit(text3, text3_rect)
        tela.blit(text4, text4_rect)
        tela.blit(text5, text5_rect)
        tela.blit(text6, text6_rect)
        tela.blit(text7, text7_rect)
        tela.blit(text8, text8_rect)
        tela.blit(text9, text9_rect)
        pygame.display.update()
