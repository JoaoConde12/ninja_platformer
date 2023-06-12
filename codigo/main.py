#Importar de librerias
import pygame
import math
from configuraciones import *
from nivel import Nivel
from data_niveles import nivel1
from menu import Menu


class Juego():
    def __init__(self):
        self.nivel_maximo = 1
        self.menu = Menu(0, self.nivel_maximo, ventana, self.crear_nivel)
        self.estado = "menu" 

    def crear_nivel(self, nivel_actual):
        self.nivel = Nivel(nivel_actual, ventana, self.crear_menu)
        self.estado = "nivel"
    
    def crear_menu(self, nivel_actual, siguiente_nivel):
        if siguiente_nivel > self.nivel_maximo:
            self.nivel_maximo = siguiente_nivel
        self.menu = Menu(nivel_actual, self.nivel_maximo, ventana, self.crear_nivel)
        self.estado = "menu"


    def ejecutar(self):
        if self.estado == "menu":
            ventana.blit(bg_menu, (0,0))
            self.menu.ejecutar()
            
        else:
            for i in range(0, patrones):
                ventana.blit(bg, (i * bg_ancho, 0))
            self.nivel.ejecutar()
            


#Configuracion incial del juego
pygame.init()
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ninja Platformer")
reloj = pygame.time.Clock()
juego = Juego()


#Cargar fondo del juego
bg = pygame.image.load("../graficos/fondo/fondo.png")
bg_menu = pygame.image.load("../graficos/fondo/menu_fondo.png")
bg_ancho = bg.get_width()
patrones = math.ceil(ventana_ancho / bg_ancho)


#Loop del juego
ejecutar = True
while ejecutar:
    

    #Cargar fondo

    #Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False


    juego.ejecutar()


    pygame.display.update()
    reloj.tick(60)

pygame.quit()