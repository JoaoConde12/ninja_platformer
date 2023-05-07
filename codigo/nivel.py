#Importación de librerías y módulos
import pygame
from bloques import Bloque
from configuraciones import tamaño_bloque, ventana_ancho
from jugador import Jugador

class Nivel:
    def __init__(self, mapa_beta, surface):
        self.mostrar_surface = surface
        self.configurar_nivel(mapa_beta)
        self.avanzar_mapa = 0
        self.x_actual = 0


    def configurar_nivel(self, layout):
        self.bloques = pygame.sprite.Group()
        self.jugador = pygame.sprite.GroupSingle()

        for fila_indice, fila in enumerate(layout):
            for columna_indice, columna in enumerate(fila):
                x = columna_indice * tamaño_bloque
                y = fila_indice * tamaño_bloque
                if columna == 'X':    
                    bloque = Bloque((x, y), tamaño_bloque)
                    self.bloques.add(bloque)
                if columna == 'P':
                    jugador = Jugador((x, y))
                    self.jugador.add(jugador)


    def mover_camara_x(self):
        jugador = self.jugador.sprite
        jugador_x = jugador.rect.centerx
        direcion_x = jugador.direccion.x

        if jugador_x < ventana_ancho / 4 and direcion_x < 0:
            self.avanzar_mapa = 8
            jugador.velocidad = 0
        elif jugador_x > ventana_ancho - (ventana_ancho / 4) and direcion_x > 0:
            self.avanzar_mapa = -8
            jugador.velocidad = 0
        else:
            self.avanzar_mapa = 0
            jugador.velocidad = 8


    def colision_horizontal(self):
        jugador = self.jugador.sprite
        jugador.rect.x += jugador.direccion.x * jugador.velocidad

        for sprite in self.bloques.sprites():
            if sprite.rect.colliderect(jugador.rect):
                if jugador.direccion.x < 0:
                    jugador.izquierda = True
                    jugador.rect.left = sprite.rect.right
                    self.x_actual = jugador.rect.left
                elif jugador.direccion.x > 0:
                    jugador.rect.right = sprite.rect.left
                    jugador.derecha = True
                    self.x_actual = jugador.rect.right

        if jugador.izquierda and (jugador.rect.left < self.x_actual or jugador.direccion.x >= 0):
            jugador.izquierda = False
        if jugador.derecha and (jugador.rect.right > self.x_actual or jugador.direccion.x <= 0):
            jugador.derecha = False
        
        

    def colision_vertical(self):
        jugador = self.jugador.sprite
        jugador.aplicar_gravedad()

        for sprite in self.bloques.sprites():
            if sprite.rect.colliderect(jugador.rect):
                if jugador.direccion.y > 0:
                    jugador.rect.bottom = sprite.rect.top
                    jugador.direccion.y = 0
                    jugador.en_suelo = True
                elif jugador.direccion.y < 0:
                    jugador.rect.top = sprite.rect.bottom
                    jugador.direccion.y = 0
                    jugador.en_techo = True
            
            if jugador.en_suelo and jugador.direccion.y < 0 or jugador.direccion.y > 1:
                jugador.en_suelo = False
            if jugador.en_techo and jugador.direccion.y > 0:
                jugador.en_techo = False


    def ejecutar(self):
        self.bloques.update(self.avanzar_mapa)
        self.bloques.draw(self.mostrar_surface)
        self.mover_camara_x()

        self.jugador.update()        
        self.colision_horizontal()
        self.colision_vertical()
        self.jugador.draw(self.mostrar_surface)

        
