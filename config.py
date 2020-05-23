# Modulos
import support
import pygame, sys
from pygame.locals import *

# Funcao principal
def main(tela, som, tempo):
    option = 1
    sound = som
    time = tempo
    fundo = support.carrega_imagem('tela_jogo.jpg')
    font1 = support.carrega_fonte('tallpaul.ttf', 50)
    font1.set_bold(True)
    font2 = support.carrega_fonte('tallpaul.ttf', 40)
    font2.set_bold(True)
    font3 = support.carrega_fonte('tallpaul.ttf', 40)
    font4 = support.carrega_fonte('tallpaul.ttf', 50)
    # Loop
    while True:
        # Eventos
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    return sound, time
                if event.key == K_RETURN:
                    return sound, time
                
                if event.key == K_UP:
                    option -= 1
                    if option < 1:
                        option = 1
                if event.key == K_DOWN:
                    option += 1
                    if option > 2:
                        option = 2
                if event.key == K_SPACE and option == 1:
                    if sound == 1:
                        print sound
                        sound = 0
                    else:
                        sound = 1
                        print sound
                if event.key == K_SPACE and option == 2:
                    if time == 1:
                        print time
                        time = 0
                    else:
                        print time
                        time = 1
                    
        # Texto
        tela.blit(fundo, (0, 0))
        text1 = font1.render("Configurar:", 1, (10, 10, 10))
        text1_rect = text1.get_rect()
        text1_rect.topright = (924, 200)
        if option == 1:
            text2 = font2.render("Som:", 1, (255, 10, 10))
        else:
            text2 = font2.render("Som:", 1, (10, 10, 10))
        text2_rect = text2.get_rect()
        text2_rect.topright = (924, 260)
        if sound == 1:
            text3 = font3.render("On", 1, (10, 10, 10))
            text3_rect = text3.get_rect()
            text3_rect.topright = (924, 290)
        else:
            text3 = font3.render("Off", 1, (10, 10, 10))
            text3_rect = text3.get_rect()
            text3_rect.topright = (924, 290)
        
        if option == 2:
            text5 = font2.render("Tempo:", 1, (255, 10, 10))
        else:
            text5 = font2.render("Tempo:", 1, (10, 10, 10))
        text5_rect = text5.get_rect()
        text5_rect.topright = (924, 390)
        if time == 1:
            text6 = font3.render("On", 1, (10, 10, 10))
            text6_rect = text6.get_rect()
            text6_rect.topright = (924, 430)
        else:
            text6 = font3.render("Off", 1, (10, 10, 10))
            text6_rect = text6.get_rect()
            text6_rect.topright = (924, 430)
                
        text9 = font2.render("Enter para voltar", 1, (10, 10, 10))
        text9_rect = text9.get_rect()
        text9_rect.topright = (924, 668)
        tela.blit(text1, text1_rect)
        tela.blit(text2, text2_rect)
        tela.blit(text3, text3_rect)
        tela.blit(text5, text5_rect)
        tela.blit(text6, text6_rect)
        tela.blit(text9, text9_rect)
        
        pygame.display.update()
