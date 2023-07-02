import pygame
from importador import importar_carpeta
from math import sin 


class Jugador(pygame.sprite.Sprite):
    def __init__(self, posicion, surface, recibir_daño, saltos_mushroom):
        super().__init__()
        self.cargar_personaje()
        self.indice_frame = 0
        self.velocidad_animacion = 0.15
        self.image = self.animaciones["inactivo"][self.indice_frame]
        self.rect = self.image.get_rect(topleft = posicion)

        #Movimiento del jugador
        self.direccion = pygame.math.Vector2(0, 0)
        self.velocidad = 7
        self.gravedad = 0.8
        self.velocidad_salto = -16

        #Estados del jugador
        self.estado = "inactivo"
        self.mirar_derecha = True
        self.en_suelo = False
        self.en_techo = False
        self.izquierda = False
        self.derecha = False
        self.saltos_realizados = 0
        self.saltos_mushroom = saltos_mushroom

        #Cambio de vida
        self.recibir_daño = recibir_daño
        self.invencible = False
        self.duracion_invencibilidad = 650
        self.herir_tiempo = 0


    def cargar_personaje(self):
        directorio_personaje = "../graficos/personaje/"
        self.animaciones = {"inactivo": [],
                            "correr": [],
                            "saltar": [],
                            "caer": []}
        
        for animacion in self.animaciones.keys():
            directio_lleno = directorio_personaje + animacion
            self.animaciones[animacion] = importar_carpeta(directio_lleno)


    def animar(self):
        animacion = self.animaciones[self.estado]

        #Loop por cada indice del frame
        self.indice_frame += self.velocidad_animacion  
        if self.indice_frame >= len(animacion):
            self.indice_frame = 0

        imagen = animacion[int(self.indice_frame)]

        if self.mirar_derecha:
            self.image = imagen
            #self.image = pygame.transform.scale(self.image, (32, 65))
        else:
            virar_imaginen = pygame.transform.flip(imagen, True, False)
            self.image = virar_imaginen
            #self.image = pygame.transform.scale(self.image, (32, 65))

        if self.invencible:
            alfa = self.valor_ola()
            self.image.set_alpha(alfa)
        else:
            self.image.set_alpha(255)

        #Comprobar si está en el rectangulo
        if self.en_suelo and self.derecha:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.en_suelo and self.izquierda:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.en_suelo:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.en_techo and self.derecha:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.en_techo and self.izquierda:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.en_techo:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)


    def obtener_teclas(self):
        teclas = pygame.key.get_pressed()

        if teclas[pygame.K_RIGHT]:
            self.direccion.x = 1
            self.mirar_derecha = True
        elif teclas[pygame.K_LEFT]:
            self.direccion.x = -1
            self.mirar_derecha = False
        else:
            self.direccion.x = 0

        if teclas[pygame.K_SPACE]:
            if self.en_suelo:
                self.saltar()
                self.saltos_realizados = 1
            elif self.saltos_realizados < 2 and self.direccion.y >= 0 and self.saltos_mushroom >= 1:
                self.saltar()
                self.saltos_realizados += 1
                self.saltos_mushroom -= 1

            
    def obtener_estados(self):
        if self.direccion.y < 0:
            self.estado = "saltar"
        elif self.direccion.y > 1:
            self.estado = "caer"
        else:
            if self.direccion.x != 0:
                self.estado = "correr"
            else:
                self.estado = "inactivo"


    def aplicar_gravedad(self):
        self.direccion.y += self.gravedad
        self.rect.y += self.direccion.y

        if self.en_suelo:
            self.saltos_disponibles = 2


    def saltar(self):
        self.direccion.y = self.velocidad_salto


    def obtener_daño(self):
        if not self.invencible:
            self.recibir_daño(-10)
            self.invencible = True
            self.herir_tiempo = pygame.time.get_ticks()


    def caer_vacio(self):
        self.recibir_daño(-40)


    def invencibilidad_tiempo(self):
        if self.invencible:
            tiempo_actual = pygame.time.get_ticks()
            if tiempo_actual - self.herir_tiempo >= self.duracion_invencibilidad:
                self.invencible = False


    def valor_ola(self):
        valor = sin(pygame.time.get_ticks())
        if valor >= 0:
            return 255
        else:
            return 0


    def update(self):
        self.obtener_teclas()
        self.obtener_estados()
        self.animar()
        self.invencibilidad_tiempo()
        self.valor_ola()
        