#Importación de librerías y módulos
import pygame
from data_niveles import nivel1
from configuraciones import tamaño_bloque, ventana_ancho
from importador import importar_csv_layout, importar_graficos_terreno
from bloques import Bloque
from vegetacion import Arbol1, Arbol2, Tronco
from agua import Agua, Olas


class Nivel:
    def __init__(self, nivel, surface):

        #Configuración general
        self.ventana_surface = surface
        self.cambio_mundo = 0

        #Jugador


        #Configuración de terreno
        terreno_layout = importar_csv_layout(nivel1["terreno"])
        self.terreno_sprites = self.crear_grupos_bloques(terreno_layout, "terreno")


        #Arboles y troncos
        arbol1_layout = importar_csv_layout(nivel1["arbol1"])
        self.arbol1_sprites = self.crear_grupos_bloques(arbol1_layout, "arbol1")

        arbol2_layout = importar_csv_layout(nivel1["arbol2"])
        self.arbol2_sprites = self.crear_grupos_bloques(arbol2_layout, "arbol2")

        tronco_layout = importar_csv_layout(nivel1["tronco"])
        self.tronco_sprites = self.crear_grupos_bloques(tronco_layout, "tronco")


        #Enemigo
        enemigo_layout = importar_csv_layout(nivel1["enemigo"])
        self.enemigo_sprites = self.crear_grupos_bloques(enemigo_layout, "enemigo")

        #Choque de enemigo
        choque_layout = importar_csv_layout(nivel1["choque"])
        self.choque_sprites = self.crear_grupos_bloques(choque_layout, "choque")


        #Agua y olas
        agua_layout = importar_csv_layout(nivel1["agua"])
        self.agua_sprites = self.crear_grupos_bloques(agua_layout, "agua")

        olas_layout = importar_csv_layout(nivel1["ola"])
        self.olas_sprites = self.crear_grupos_bloques(olas_layout, "ola")



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

        for sprite in self.terreno_sprites.sprites():
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
    
        for sprite in self.terreno_sprites.sprites():
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

        
