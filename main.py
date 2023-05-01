#Importar de librerias
import pygame
from configuraciones import *
from bloques import Bloque
from nivel import Nivel

#Configuracion incial del juego
pygame.init()
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
reloj = pygame.time.Clock()
nivel_beta = Nivel(mapa, ventana)

#Loop del juego
ejecutar = True
while ejecutar:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False

    nivel_beta.ejecutar()

    pygame.display.update()
    reloj.tick(60)

pygame.quit()