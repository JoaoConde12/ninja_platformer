#Importar de librerias
import pygame
import math
from configuraciones import *
from nivel import Nivel
from menu import Menu
from interfaz import Interfaz


class Juego():
    def __init__(self):
        #Atributos del juego
        self.nivel_maximo = 0
        self.vida_maxima = 40
        self.vida_actual = 40
        self.contador_monedas = 0
        self.contador_mushrooms = 0
        self.saltos = 0
        self.restar_mushroom = False

        #Audio (soundtrack)
        self.sonido_soundtrack_nivel =pygame.mixer.Sound("../audio/musica_nivel.wav")
        self.sonido_soundtrack_nivel.set_volume(0.2)
        self.sonido_menu = pygame.mixer.Sound("../audio/musica_menu.wav")
        self.sonido_menu.set_volume(0.1)

        #Audio efectos
        self.sonido_aumentar_vida = pygame.mixer.Sound("../audio/efectos/up_life.wav")
        self.sonido_aumentar_vida.set_volume(0.4)

        #Creacion menú
        self.menu = Menu(0, self.nivel_maximo, ventana, self.crear_nivel)
        self.estado = "menu"
        self.sonido_menu.play(loops = -1)

        #Interfaz
        self.interfaz = Interfaz(ventana)


    def crear_nivel(self, nivel_actual):
        self.nivel = Nivel(nivel_actual, ventana, self.crear_menu, self.aumentar_monedas, self.recibir_daño, self.aumentar_mushroom, self.aumentar_vida)
        self.estado = "nivel"
        self.sonido_menu.stop()
        self.sonido_soundtrack_nivel.play(loops = -1)


    def crear_menu(self, nivel_actual, siguiente_nivel):
        if siguiente_nivel > self.nivel_maximo:
            self.nivel_maximo = siguiente_nivel
        self.menu = Menu(nivel_actual, self.nivel_maximo, ventana, self.crear_nivel)
        self.contador_mushrooms = 0
        self.estado = "menu"
        self.sonido_menu.play(loops = -1)
        self.sonido_soundtrack_nivel.stop()


    def aumentar_monedas(self, cantidad):
        self.contador_monedas += cantidad


    def aumentar_mushroom(self, cantidad):
        if cantidad < 0 and not self.restar_mushroom:
            self.contador_mushrooms -= 1
            self.restar_mushroom = True
        elif cantidad > 0:
            self.contador_mushrooms += cantidad
            self.restar_mushroom = False        


    def recibir_daño(self, cantidad):
        self.vida_actual += cantidad


    def aumentar_vida(self, cantidad):
        if self.vida_actual < 40:
            self.sonido_aumentar_vida.play()
            self.vida_actual += cantidad
        else:
            pass


    def game_over(self):
        if self.vida_actual <= 0:
            #time.sleep(3)
            self.vida_actual = 40
            self.contador_monedas = 0
            self.contador_mushrooms = 0
            self.nivel_maximo = 0
            self.menu = Menu(0, self.nivel_maximo, ventana, self.crear_nivel)
            self.estado = "menu"
            self.sonido_soundtrack_nivel.stop()
            self.sonido_menu.play(loops = -1)


    def ejecutar(self):
        if self.estado == "menu":
            ventana.blit(bg_menu, (0,0))
            self.menu.ejecutar()
            
        else:
            for i in range(0, patrones):
                ventana.blit(bg, (i * bg_ancho, 0))
            self.nivel.ejecutar()
            self.interfaz.mostrar_vida(self.vida_actual, self.vida_maxima)
            self.interfaz.mostrar_monedas(self.contador_monedas)
            self.interfaz.mostrar_mushroom(self.contador_mushrooms)
            self.game_over()


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

    #Eventos del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutar = False

    juego.ejecutar()

    pygame.display.update()
    reloj.tick(60)

pygame.quit()