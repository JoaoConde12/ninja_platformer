#Importación de librerías y módulos
import pygame
from bloques import Bloque
from configuraciones import tamaño_bloque
from jugador import Jugador

class Nivel:
    def __init__(self, mapa_beta, surface):
        self.mostrar_surface = surface
        self.configurar_nivel(mapa_beta)
        self.avanzar_mapa = 0

    def configurar_nivel(self, layout):
        self.bloques = pygame.sprite.Group()
        self.jugadores = pygame.sprite.GroupSingle()

        for fila_indice, fila in enumerate(layout):
            for columna_indice, columna in enumerate(fila):
                x = columna_indice * tamaño_bloque
                y = fila_indice * tamaño_bloque
                if columna == 'X':    
                    bloque = Bloque((x, y), tamaño_bloque)
                    self.bloques.add(bloque)
                if columna == 'P':
                    jugador = Jugador((x, y))
                    self.jugadores.add(jugador)

    def mover_camara_x(self):
        jugadores = self.jugadores.sprite
        jugadores_x = jugadores.rect.centerx
        direcion_x = jugadores.direccion.x

        if jugadores_x < 300 and direcion_x < 0:
            self.avanzar_mapa = 8
            jugadores.velocidad = 0
        elif jugadores_x > 900 and direcion_x > 0:
            self.avanzar_mapa = -8
            jugadores.velocidad = 0
        else:
            self.avanzar_mapa = 0
            jugadores.velocidad = 8
        

    def ejecutar(self):
        self.bloques.update(self.avanzar_mapa)
        self.bloques.draw(self.mostrar_surface)

        self.jugadores.update()        
        self.jugadores.draw(self.mostrar_surface)

        self.mover_camara_x()
