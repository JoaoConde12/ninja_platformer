import pygame
from data_niveles import niveles


class Nodo(pygame.sprite.Sprite):
    def __init__(self, posicion, estado, velociad_icono, directorio):
        super().__init__()
        self.image = pygame.image.load(directorio)

        if estado == "disponible":
            self.estado = "disponible"
        else:
            self.estado = "bloqueado"
            pintar_negro = self.image.copy()
            pintar_negro.fill("black", None, pygame.BLEND_RGBA_MULT)
            self.image.blit(pintar_negro, (0, 0))
        
        self.rect = self.image.get_rect(center = posicion)
        self.detectar_colision = pygame.Rect(self.rect.centerx - (velociad_icono / 2),
                                             self.rect.centery - (velociad_icono / 2),
                                             velociad_icono,
                                             velociad_icono)
        

class Icono(pygame.sprite.Sprite):
    def __init__(self, posicion):
        super().__init__()
        self.posicion = posicion
        self.image = pygame.image.load("../graficos/menu/ninja.png")
        self.rect = self.image.get_rect(center = posicion)

    def update(self):
        self.rect.center = self.posicion


class Menu():
    def __init__(self, nivel_inicio, nivel_final, surface, crear_nivel):
        
        #Configuraciones
        self.ventana_surface = surface
        self.nivel_actual = nivel_inicio
        self.nivel_final = nivel_final
        self.crear_nivel = crear_nivel

        #Movimiento
        self.direccion_movimiento = pygame.math.Vector2(0, 0)
        self.velocidad = 8
        self.moviendo = False

        #sprites
        self.configuracion_nodos()
        self.configuracion_icono()


    def configuracion_nodos(self):
        self.nodos = pygame.sprite.Group()
        for indice, posicion in enumerate(niveles.values()):
            if indice <= self.nivel_final:
                nodo_sprite = Nodo(posicion["posicion"], "disponible", self.velocidad, posicion["grafico"])
            else:
                nodo_sprite = Nodo(posicion["posicion"], "bloqueado", self.velocidad, posicion["grafico"])
            self.nodos.add(nodo_sprite)


    def configuracion_icono(self):
        self.icono = pygame.sprite.GroupSingle()
        icono_sprite = Icono(self.nodos.sprites()[self.nivel_actual].rect.center)
        self.icono.add(icono_sprite)
        

    def dibujar_lineas(self):
        if self.nivel_final > 0:
            puntos = [posicion["posicion"] for indice, posicion in enumerate(niveles.values())
                  if indice <= self.nivel_final]
            pygame.draw.lines(self.ventana_surface, "#01153E", False, puntos, 6)


    def mover_icono(self):
        teclas = pygame.key.get_pressed()

        if not self.moviendo:
            if teclas[pygame.K_RIGHT] and self.nivel_actual < self.nivel_final:
                self.direccion_movimiento = self.obtener_direccion_movimiento("siguiente")
                self.nivel_actual += 1
                self.moviendo = True
            elif teclas[pygame.K_LEFT] and self.nivel_actual > 0:
                self.direccion_movimiento = self.obtener_direccion_movimiento("anterior")
                self.nivel_actual -=1
                self.moviendo = True
            elif teclas[pygame.K_SPACE]:
                self.crear_nivel(self.nivel_actual)
    

    def obtener_direccion_movimiento(self, destino):
        inicio = pygame.math.Vector2(self.nodos.sprites()[self.nivel_actual].rect.center)

        if destino == "siguiente":
            final = pygame.math.Vector2(self.nodos.sprites()[self.nivel_actual + 1].rect.center)
        else:
            final = pygame.math.Vector2(self.nodos.sprites()[self.nivel_actual - 1].rect.center)

        return (final - inicio).normalize()


    def actualizar_posicion_icono(self):
        if self.moviendo and self.direccion_movimiento:
            self.icono.sprite.posicion += self.direccion_movimiento * self.velocidad
            destino_nodo = self.nodos.sprites()[self.nivel_actual]
            if destino_nodo.detectar_colision.collidepoint(self.icono.sprite.posicion):
                self.moviendo = False
                self.direccion_movimiento = pygame.math.Vector2(0, 0)


    def ejecutar(self):
        self.mover_icono()
        self.actualizar_posicion_icono()
        self.icono.update()
        self.dibujar_lineas()
        self.nodos.draw(self.ventana_surface)
        self.icono.draw(self.ventana_surface)