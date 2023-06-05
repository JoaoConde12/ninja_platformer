import pygame
from csv import reader
from configuraciones import tamaño_bloque
from os import walk


def importar_carpeta(directorio):

    lista = []

    for _ ,__ , archivos_imagen in walk(directorio):
        for imagen in archivos_imagen:
            directorio_lleno = directorio + "/" + imagen
            imagen_surf = pygame.image.load(directorio_lleno).convert_alpha()
            lista.append(imagen_surf)

    return lista


def importar_graficos_terreno(direccion):
    superfice = pygame.image.load(direccion).convert_alpha()
    bloque_num_x = int(superfice.get_size()[0] / tamaño_bloque)
    bloque_num_y = int(superfice.get_size()[1] / tamaño_bloque)

    bloques_cortados = []

    for fila in range(bloque_num_y):
        for columna in range(bloque_num_x):
            x = columna * tamaño_bloque
            y = fila * tamaño_bloque

            nueva_superficie = pygame.Surface((tamaño_bloque, tamaño_bloque), flags = pygame.SRCALPHA)
            nueva_superficie.blit(superfice, (0, 0), pygame.Rect(x, y, tamaño_bloque, tamaño_bloque))
            bloques_cortados.append(nueva_superficie)

    return bloques_cortados


def importar_csv_layout(direccion):
    mapa_terreno = []
    with open(direccion) as map:
        nivel = reader(map, delimiter = ",")
        for linea in nivel:
            mapa_terreno.append(list(linea))
        return mapa_terreno