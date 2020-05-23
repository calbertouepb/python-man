# Modulos utilizados
import config, credits, game, help, records, support
import os, pygame, sys
from pygame.locals import *

# Classe principal
class Menu:

    def __init__(self, tela):
        # Inicializacao
        self.tela = tela
        self.som = support.carrega_som('intro.ogg').play(-1)
        self.fundo = support.carrega_imagem('tela_jogo.jpg')
        self.jogar = support.carrega_imagem('jogar1.png')
        self.rect_jogar = self.jogar.get_rect(topleft=(300, 600))
        self.configurar = support.carrega_imagem('configurar1.png')
        self.rect_configurar = self.configurar.get_rect(topleft=(410, 600))
        self.recordes = support.carrega_imagem('recordes1.png')
        self.rect_recordes = self.recordes.get_rect(topleft=(550, 600))
        self.creditos = support.carrega_imagem('creditos1.png')
        self.rect_creditos = self.creditos.get_rect(topleft=(710, 600))
        self.ajuda = support.carrega_imagem('ajuda1.png')
        self.rect_ajuda = self.ajuda.get_rect(topleft=(830, 600))
        self.sair = support.carrega_imagem('sair1.png')
        self.rect_sair = self.sair.get_rect(topleft=(890, 600))
        self.font = support.carrega_fonte('tallpaul.ttf', 40)
        self.option = 1
        self.som_ativado = 1
        self.nivel = 1
        self.modo_tempo = 1
        self.tempo = 0
        self.text = self.font.render("", 1, (10, 10, 10))
        self.textpos = Rect(0, 0, 0, 0)
        
    def main(self):
        # Loop principal
        while True:
            # Tratamento de eventos
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        sys.exit()
                    if event.key == K_LEFT:
                        self.option -= 1
                        if self.option < 1:
                            self.option = 1
                    if event.key == K_RIGHT:
                        self.option += 1
                        if self.option > 6:
                            self.option = 6
                    if event.key == K_RETURN:
                        if self.option == 1:
                            self.go = support.carrega_som('go.ogg').play()
                            pygame.time.delay(800)
                            self.som.pause()
                            if self.modo_tempo == 1:
                                self.tempo = pygame.time.get_ticks()
                                
                            status = game.main(self.nivel, self.som_ativado)
                            while self.nivel < 3 and status == "ganhou":
                                self.nivel += 1
                                status = game.main(self.nivel, self.som_ativado)
                            if self.modo_tempo == 1:
                                tempo_final = pygame.time.get_ticks()
                                tempo_total = tempo_final - self.tempo
                                self.tempo = tempo_total
                                
                            if status == "ganhou":
                                self.fundo = support.carrega_imagem('ganhou.jpg')
                                caminho = os.path.join('data', 'ranking.dat')
                                dados = open(caminho, 'a')
                                dados.write(str(self.tempo)+"\n")
                                dados.close()
                                self.nivel = 1
                            if status == "perdeu":
                                self.fundo = support.carrega_imagem('perdeu.jpg')
                                self.nivel = 1
                            self.som.unpause()
                        if self.option == 2:
                            self.som_ativado, self.modo_tempo = config.main(self.tela, self.som_ativado, self.modo_tempo)
                        if self.option == 3:
                            records.main(self.tela)
                        if self.option == 4:
                            credits.main(self.tela)
                        if self.option == 5:
                            help.main(self.tela)
                        if self.option == 6:
                            sys.exit()
            # Composicao da tela
            self.tela.blit(self.fundo, (0, 0))
            self.tela.blit(self.jogar, self.rect_jogar)
            self.text_jogar = self.font.render("Jogar", 1, (10, 10, 10))
            self.textpos_jogar = (300, 700)
            self.tela.blit(self.configurar, self.rect_configurar)
            self.text_configurar = self.font.render("Configurar", 1, (10, 10, 10))
            self.textpos_configurar = (400, 700)
            self.tela.blit(self.recordes, self.rect_recordes)
            self.text_recordes = self.font.render("Recordes", 1, (10, 10, 10))
            self.textpos_recordes = (545, 700)
            self.tela.blit(self.creditos, self.rect_creditos)
            self.text_creditos = self.font.render("Creditos", 1, (10, 10, 10))
            self.textpos_creditos = (690, 700)
            self.tela.blit(self.ajuda, self.rect_ajuda)
            self.text_ajuda = self.font.render("Ajuda", 1, (10, 10, 10))
            self.textpos_ajuda = (820, 700)
            self.tela.blit(self.sair, self.rect_sair)
            self.text_sair = self.font.render("Sair", 1, (10, 10, 10))
            self.textpos_sair = (910, 700)
            self.tela.blit(self.text, self.textpos)
            self.tela.blit(self.text_jogar, self.textpos_jogar)
            self.tela.blit(self.text_configurar, self.textpos_configurar)
            self.tela.blit(self.text_recordes, self.textpos_recordes)
            self.tela.blit(self.text_creditos, self.textpos_creditos)
            self.tela.blit(self.text_ajuda, self.textpos_ajuda)
            self.tela.blit(self.text_sair, self.textpos_sair)
            if self.option == 1:
                self.jogar = support.carrega_imagem('jogar1.png')
                self.tela.blit(self.jogar, self.rect_jogar)
            if self.option == 2:
                self.configurar = support.carrega_imagem('configurar1.png')
                self.tela.blit(self.configurar, self.rect_configurar)
            if self.option == 3:
                self.recordes = support.carrega_imagem('recordes1.png')
                self.tela.blit(self.recordes, self.rect_recordes)
            if self.option == 4:
                self.creditos = support.carrega_imagem('creditos1.png')
                self.tela.blit(self.creditos, self.rect_creditos)
            if self.option == 5:
                self.ajuda = support.carrega_imagem('ajuda1.png')
                self.tela.blit(self.ajuda, self.rect_ajuda)
            if self.option == 6:
                self.sair = support.carrega_imagem('sair1.png')
                self.tela.blit(self.sair, self.rect_sair)
            pygame.display.update()
