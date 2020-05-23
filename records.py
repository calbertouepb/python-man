# Modulos
import support
import os, pygame, sys
from pygame.locals import *

# Funcao principal
def main(tela):
    caminho = os.path.join('data', 'ranking.dat')
    dados = open(caminho, 'r')
    dados2 = dados.readlines()
    fundo = support.carrega_imagem('tela_jogo.jpg')
    font1 = support.carrega_fonte('tallpaul.ttf', 50)
    font1.set_bold(True)
    font2 = support.carrega_fonte('tallpaul.ttf', 40)
    
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
        text1 = font1.render("Ranking:", 1, (10, 10, 10))
        text1_rect = text1.get_rect()
        text1_rect.topright = (924, 200)
        cont = 0
        pos_x = 260
        dados3 = [i.strip("\n") for i in dados2]
        for i in dados3:
            tempo = int(i)/60000.0
            time = (str(tempo).split('.'))
            temp = "%s min(s) e %2s seg(s)" % (time[0], time[1][0:2])
            text2 = font2.render(str(cont+1)+" : "+temp, 1, (10, 10, 10))
            text2_rect = text2.get_rect()
            text2_rect.topright = (924, pos_x)
            tela.blit(text2, text2_rect)
            cont += 1
            pos_x += 50
        
        
        text9 = font2.render("Enter para voltar", 1, (10, 10, 10))
        text9_rect = text9.get_rect()
        text9_rect.topright = (924, 668)
        tela.blit(text1, text1_rect)
        
        tela.blit(text9, text9_rect)
        pygame.display.update()
