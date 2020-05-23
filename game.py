# Engine principal
#
# Modulos usados no jogo
import impata, lab, play, support, vector2d
import pygame, random, sys
from pygame.locals import *
from pygame.sprite import *

# Inicializacao
pygame.init()
tela = pygame.display.set_mode((1024, 768), 0, 32)
pygame.display.set_caption("py Fun k")

#
##############################################
#

# Loop principal
def main (nivel, som_ativado):
    
    # Instanciacao dos objetos e grupos
    grupo = RenderUpdates()
    labirinto = lab.Labirinto(nivel)
    jogador = play.Jogador()
    saida = lab.Porta(840, 320)
    impatas = Group()
    paredes = Group()
    objetos = Group()
    for impt in range(nivel):
        impatas.add(impata.Impata(512, 404, nivel))
    som = support.carrega_som("ambient%d.ogg" % nivel)
    if som_ativado == 1:
        som.play(-1)
    pegar = support.carrega_som("catch%d.ogg" % nivel)
    colide = support.carrega_som("crash%d.ogg" % nivel)
    fim = support.carrega_som('finish.ogg')
    
    # Composicao do background
    support.compoe_fundo(tela, "background%d.jpg" % nivel)
    labirinto.constroi(tela, nivel)
    labirinto.cria_objetos(paredes, objetos, nivel)
    objetos.draw(tela)
        
    while True:

        # Sair
        for evento in pygame.event.get():
            if evento.type == QUIT:
                som.stop()
                return "saiu"
            if evento.type == KEYDOWN and evento.key == K_ESCAPE:
                som.stop()
                return "saiu"

        teclas = pygame.key.get_pressed()
        direcao = vector2d.Vector2(0, 0)

        if teclas[K_LEFT]:
            direcao.x = -1  # --> (-1, 0)
        if teclas[K_RIGHT]:
            direcao.x = +1  # --> (+1, 0)
        if teclas [K_UP]:
            direcao.y = -1  # --> (0, -1)
        if teclas[K_DOWN]:
            direcao.y = +1  # --> (0, +1)

        support.compoe_fundo(tela, "background%d.jpg" % nivel)
        labirinto.constroi(tela, nivel)
        objetos.draw(tela)
        
        for impt in impatas:
            impt.move()
        jogador.move(direcao)
        
        # Movimentos do impata
        direcoes = [-1, 1]
        for impt in impatas:
            if spritecollideany(impt, paredes):
                impt.volta()
                eixo = random.choice(direcoes)
                if eixo == -1:
                    impt.direcao.y = 0
                    impt.direcao.x = random.choice(direcoes)
                else:
                    impt.direcao.x = 0
                    impt.direcao.y = random.choice(direcoes)
            tela.blit(impt.image, impt.rect.center)
        
        # Movimentos do jogador
        if spritecollideany(jogador, paredes):
            jogador.volta()
        tela.blit(jogador.image, jogador.rect.center)
        
        if spritecollideany(jogador, objetos):
            pegar.play()
            spritecollide(jogador, objetos, True)
            jogador.pontuacao += 10
        
        if spritecollideany(jogador, impatas) and jogador.vidas > 0:
            colide.play()
            jogador.vidas -= 1
            jogador.posicao = vector2d.Vector2(152, 564)
            impatas.add(impata.Impata(512, 404, nivel))
            if jogador.vidas == 0:
                pygame.time.delay(500)
                som.stop()
                return "perdeu"
        
        if jogador.rect.colliderect(saida.rect) and jogador.pontuacao == 150:
            fim.play()
            som.stop()
            return "ganhou"
        
        font = support.carrega_fonte('tallpaul.ttf', 60)
        text = font.render("Nivel: "+str(nivel)+"  Score: "+str(jogador.pontuacao)+"  Vidas: "+str(jogador.vidas), 1, (10, 10, 10))
        textpos = text.get_rect()
        textpos.centerx = tela.get_rect().centerx
        tela.blit(text, textpos)
        
        pygame.display.update()

