import pygame as pg
import piezas

class Pieza():
    def __init__(self):
        self.pieza = piezas.Pieza()
    
    def draw(self, screen):
        rect_list = []
        for i in range(4):
            for j in range(4):
                if self.pieza.cuadrado[i][j]:
                    pg.rect(50*i,50*j,50,50)
                    pg.draw.rect(screen, (50,0,100), (50*i,50*j,50,50), 2)

        return rect_list
