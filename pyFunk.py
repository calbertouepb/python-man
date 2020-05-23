#!/usr/bin/env python

###############################################
#   ----------      pyFunk       ----------   #
###############################################

# Modulos
import menu
import pygame, sys
from pygame.locals import *

# Inicializacao
pygame.init()
tela = pygame.display.set_mode((1024, 768), 0, 32)
pygame.display.set_caption("py Fun k")

# Corpo do programa
menu = menu.Menu(tela)
menu.main()

