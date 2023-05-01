#Importar de librerias
import pygame

#Configuracion incial del juego
pygame.init()
ventana_ancho = 1200
ventana_alto = 650
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
reloj = pygame.time.Clock()

#Loop del juego
ejecutar = True
while ejecutar:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False

    reloj.tick(60)

pygame.quit()