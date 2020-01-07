import pygame as pg

class Wall(object):
    
    def __init__(self, pos):
        self.rect = pg.Rect(pos[0], pos[1], 20, 20)