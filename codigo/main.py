#Importar de librerias
import pygame
from configuraciones import *
from nivel import Nivel

#Configuracion incial del juego
pygame.init()
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
reloj = pygame.time.Clock()
mapa_beta = Nivel(mapa, ventana)

#Loop del juego
ejecutar = True
while ejecutar:
    
    #Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False

    ventana.fill((0, 0, 0))
    mapa_beta.ejecutar()

    pygame.display.update()
    reloj.tick(60)

pygame.quit()