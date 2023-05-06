import pygame
from apoyo import importar_carpeta

class Jugador(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.cargar_personaje()
        self.indice_frame = 0
        self.velocidad_animacion = 0.15
        self.image = self.animaciones["inactivo"][self.indice_frame]
        self.image = pygame.transform.scale(self.image, (32, 65))
        self.rect = self.image.get_rect(topleft = posicion)

        #Movimiento del jugador
        self.direccion = pygame.math.Vector2(0, 0)
        self.velocidad = 7
        self.gravedad = 0.8
        self.velocidad_salto = -16


    def cargar_personaje(self):
        directorio_personaje = "../graficos/personaje/"
        self.animaciones = {"inactivo": [],
                            "correr": [],
                            "saltar": []}
        
        for animacion in self.animaciones.keys():
            directio_lleno = directorio_personaje + animacion
            self.animaciones[animacion] = importar_carpeta(directio_lleno)


    def obtener_teclas(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.direccion.x = 1
        elif teclas[pygame.K_LEFT]:
            self.direccion.x = -1
        else:
            self.direccion.x = 0

        if teclas[pygame.K_SPACE]:
            self.saltar()


    def aplicar_gravedad(self):
        self.direccion.y += self.gravedad
        self.rect.y += self.direccion.y


    def saltar(self):
        self.direccion.y = self.velocidad_salto


    def update(self):
        self.obtener_teclas()
        