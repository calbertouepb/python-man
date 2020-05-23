# Modulo que prove funcoes genericas para tratamento de imagens, sons, etc.

import pygame, os

# Carregar imagens
def carrega_imagem(nome):
    """ Carrega imagem e retorna um objeto imagem """
    caminho = os.path.join('imagens', nome)
    try:
        imagem = pygame.image.load(caminho)
        if imagem.get_alpha() is None:
            imagem = imagem.convert()
        else:
            imagem = imagem.convert_alpha()
    except pygame.error, mensagem:
        print "Nao eh possivel carregar imagem:", caminho
        raise SystemExit, mensagem
    return imagem

# Carregar sons
def carrega_som(nome):
    """ Carrega som e retorna um objeto som """
    caminho = os.path.join('sons', nome)
    try:
        sound = pygame.mixer.Sound(caminho)
    except pygame.error, mensagem:
        print "Nao eh possivel carregar som:", caminho
        raise SystemExit, mensagem
    return sound

# Carregar fontes
def carrega_fonte(nome, tamanho):
    """ Carrega fonte e retorna um objeto fonte """
    caminho = os.path.join('fonts', nome)
    try:
        font = pygame.font.Font(caminho, tamanho)
    except pygame.error, mensagem:
        print "Nao eh possivel carregar fonte:", caminho
        raise SystemExit, mensagem
    return font

# Carregar o mapa do labirinto
def carrega_labirinto(nivel):
    """ Carrega arquivo de nivel e retorna um mapa do nivel """
    nome_arquivo = 'nivel%d.txt' % nivel
    caminho = os.path.join('data', nome_arquivo)
    try:
        labirinto = open(caminho)
        mapa = labirinto.readlines()
        labirinto.close()
    except IOError, mensagem:
        print "Nao eh possivel abrir arquivo de nivel:", caminho
        raise SystemExit, mensagem
    return mapa

# Compor o fundo
def compoe_fundo(tela, nome):
    """ Compoe o plano de fundo """
    fundo = carrega_imagem(nome)
    for y in range(0, tela.get_height(), fundo.get_height()):
        for x in range(0, tela.get_width(), fundo.get_width()):
            tela.blit(fundo, (x, y))

