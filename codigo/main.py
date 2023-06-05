#Importar de librerias
import pygame
import math
from configuraciones import *
from nivel import Nivel
from data_niveles import nivel1


#Configuracion incial del juego
pygame.init()
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
reloj = pygame.time.Clock()
nivel = Nivel(nivel1, ventana)


#Cargar fondo del juego
bg = pygame.image.load("../graficos/fondo/fondo.png")
bg_ancho = bg.get_width()
patrones = math.ceil(ventana_ancho / bg_ancho)


#Loop del juego
ejecutar = True
while ejecutar:
    

    #Cargar fondo
    for i in range(0, patrones):
        ventana.blit(bg, (i * bg_ancho, 0))


    #Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False


    nivel.ejecutar()


    pygame.display.update()
    reloj.tick(60)

pygame.quit()