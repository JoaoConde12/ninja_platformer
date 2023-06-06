#Importación de librerías y módulos
import pygame
from data_niveles import nivel1
from configuraciones import tamaño_bloque, ventana_ancho
from importador import importar_csv_layout, importar_graficos_terreno
from bloques import Bloque, Bloque_estatico
from jugador import Jugador
from enemigo import Enemigo
from vegetacion import Arbol1, Arbol2, Tronco, Arbusto1, Arbusto2, Arbusto3, Arbusto4
from agua import Agua, Olas


class Nivel:
    def __init__(self, nivel, surface):

        #Configuración general
        self.ventana_surface = surface
        self.cambio_mundo = 0

        #Jugador
        personaje_layout = importar_csv_layout(nivel1["personaje"])
        self.jugador = pygame.sprite.GroupSingle()
        self.goal = pygame.sprite.GroupSingle()
        self.configuracion_personaje(personaje_layout)


        #Enemigo
        #enemigo_layout = importar_csv_layout(nivel1["enemigo"])
        #self.enemigo_sprites = self.crear_grupos_bloques(enemigo_layout, "enemigo")


        #Configuración de terreno
        terreno_layout = importar_csv_layout(nivel1["terreno"])
        self.terreno_sprites = self.crear_grupos_bloques(terreno_layout, "terreno")


        #Arboles y troncos
        arbol1_layout = importar_csv_layout(nivel1["arbol1"])
        self.arbol1_sprites = self.crear_grupos_bloques(arbol1_layout, "arbol1")

        arbol2_layout = importar_csv_layout(nivel1["arbol2"])
        self.arbol2_sprites = self.crear_grupos_bloques(arbol2_layout, "arbol2")

        tronco_layout = importar_csv_layout(nivel1["troncos"])
        self.tronco_sprites = self.crear_grupos_bloques(tronco_layout, "troncos")

        arbusto1_layout = importar_csv_layout(nivel1["arbusto1"])
        self.arbusto1_sprites = self.crear_grupos_bloques(arbusto1_layout, "arbusto1")

        arbusto2_layout = importar_csv_layout(nivel1["arbusto2"])
        self.arbusto2_sprites = self.crear_grupos_bloques(arbusto2_layout, "arbusto2")

        arbusto3_layout = importar_csv_layout(nivel1["arbusto3"])
        self.arbusto3_sprites = self.crear_grupos_bloques(arbusto3_layout, "arbusto3")

        arbusto4_layout = importar_csv_layout(nivel1["arbusto4"])
        self.arbusto4_sprites = self.crear_grupos_bloques(arbusto4_layout, "arbusto4")


        #Agua y olas
        agua_layout = importar_csv_layout(nivel1["agua"])
        self.agua_sprites = self.crear_grupos_bloques(agua_layout, "agua")

        olas_layout = importar_csv_layout(nivel1["olas"])
        self.olas_sprites = self.crear_grupos_bloques(olas_layout, "olas")


    def crear_grupos_bloques(self, layout, tipo):
        sprite_grupo = pygame.sprite.Group()

        for fila_indice, fila in enumerate(layout):
            for columna_indice, valor in enumerate(fila):
                if valor != "-1":
                    x = columna_indice * tamaño_bloque
                    y = fila_indice * tamaño_bloque

                    if tipo == "terreno":
                        lista_terreno_bloque = importar_graficos_terreno("../graficos/terreno/terreno.png")
                        bloque_superficie = lista_terreno_bloque[int(valor)]
                        sprite = Bloque_estatico(tamaño_bloque, x, y, bloque_superficie)
                        
                    if tipo == "arbol1":
                        sprite = Arbol1(tamaño_bloque, x, y)

                    if tipo == "arbol2":
                        sprite = Arbol2(tamaño_bloque, x, y)
                    
                    if tipo == "troncos":
                        sprite = Tronco(tamaño_bloque, x, y)
                    
                    if tipo == "arbusto1":
                        sprite = Arbusto1(tamaño_bloque, x, y)

                    if tipo == "arbusto2":
                        sprite = Arbusto2(tamaño_bloque, x, y)

                    if tipo == "arbusto3":
                        sprite = Arbusto3(tamaño_bloque, x, y)

                    if tipo == "arbusto4":
                        sprite = Arbusto4(tamaño_bloque, x, y)

                    if tipo == "enemigo":
                        sprite = Enemigo(tamaño_bloque, x, y)

                    if tipo == "choque":
                        sprite = Bloque(tamaño_bloque, x, y)

                    if tipo == "agua":
                        sprite = Agua(tamaño_bloque, x, y)

                    if tipo == "olas":
                        sprite = Olas(tamaño_bloque, x, y, "../graficos/olas")

                    sprite_grupo.add(sprite)

        return sprite_grupo

    
    def configuracion_personaje(self, layout):
        for fila_indice, fila in enumerate(layout):
            for columna_indice, valor in enumerate(fila):
                x = columna_indice * tamaño_bloque
                y = fila_indice * tamaño_bloque
                if valor == "0":
                    sprite = Jugador((x, y), self.ventana_surface)
                    self.jugador.add(sprite)


    def mover_camara_x(self):
        jugador = self.jugador.sprite
        jugador_x = jugador.rect.centerx
        direcion_x = jugador.direccion.x

        if jugador_x < ventana_ancho / 4 and direcion_x < 0:
            self.cambio_mundo = 8
            jugador.velocidad = 0
        elif jugador_x > ventana_ancho - (ventana_ancho / 4) and direcion_x > 0:
            self.cambio_mundo = -8
            jugador.velocidad = 0
        else:
            self.cambio_mundo = 0
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

        
    def ejecutar(self):

        #Orden
        """
        1. Personaje
        2. Enemigos
        3. Terreno
        4. Agua
        5. Olas
        6. Monedas
        7. Mush salto
        8. Mush dec
        9. Cajas
        10. Cartel 1
        11. Cartel 2
        12. Arbusto 1
        13. Arbusto 3
        14. Rocas
        15. Arbol 1
        16. Arbol 2
        17. Troncos
        18. Arbusto 2
        19. Arbusto 4
        """
        #Ejecución de todo el juego
        
        #Arboles y troncos
        self.arbusto4_sprites.update(self.cambio_mundo)
        self.arbusto4_sprites.draw(self.ventana_surface)

        self.arbusto2_sprites.update(self.cambio_mundo)
        self.arbusto2_sprites.draw(self.ventana_surface)
        
        self.tronco_sprites.update(self.cambio_mundo)
        self.tronco_sprites.draw(self.ventana_surface)

        self.arbol2_sprites.update(self.cambio_mundo)
        self.arbol2_sprites.draw(self.ventana_surface)

        self.arbol1_sprites.update(self.cambio_mundo)
        self.arbol1_sprites.draw(self.ventana_surface)

        self.arbusto3_sprites.update(self.cambio_mundo)
        self.arbusto3_sprites.draw(self.ventana_surface)

        self.arbusto1_sprites.update(self.cambio_mundo)
        self.arbusto1_sprites.draw(self.ventana_surface)


        #Agua y olas
        self.olas_sprites.update(self.cambio_mundo)
        self.olas_sprites.draw(self.ventana_surface)

        self.agua_sprites.update(self.cambio_mundo)
        self.agua_sprites.draw(self.ventana_surface)


        #Terreno
        self.terreno_sprites.update(self.cambio_mundo)
        self.terreno_sprites.draw(self.ventana_surface)
        

        #Jugador sprites
        self.jugador.update()
        self.colision_horizontal()
        self.colision_vertical()
        self.mover_camara_x()
        self.jugador.draw(self.ventana_surface)
        self.goal.update(self.cambio_mundo)
        self.goal.draw(self.ventana_surface)