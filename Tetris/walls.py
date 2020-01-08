import pygame as pg

class Wall(object):
    
    def __init__(self):
        pass

    def create_walls(self):
        walls = []
        for j in range(15):
            rect = pg.Rect(0,50*j,50,50)
            walls.append(rect)
        for j in range(15):
            rect = pg.Rect(550,50*j,50,50)
            walls.append(rect)
        for i in range(1,11):
            rect = pg.Rect(50*i,700,50,50)
            walls.append(rect)
        return walls

    def create_walls_left(self):
        walls = []
        for j in range(15):
            rect = pg.Rect(0,50*j,50,50)
            walls.append(rect)
        return walls

    def create_walls_right(self):
        walls = []
        for j in range(15):
            rect = pg.Rect(550,50*j,50,50)
            walls.append(rect)
        return walls
    
    def create_walls_down(self):
        walls = []
        for i in range(1,11):
            rect = pg.Rect(50*i,700,50,50)
            walls.append(rect)
        return walls
    
    def draw_walls(self, walls, screen):
        for wall in walls:
            pg.draw.rect(screen, (200,25,0), wall, 2)
