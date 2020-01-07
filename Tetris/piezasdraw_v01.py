import pygame as pg

class Pieza(pg.sprite.Sprite):
    def __init__(self, path):
        super().__init__()
        self.image = pg.image.load(path)
        self.rect = self.image.get_rect()

    def move(self, dx, dy, wall_list):
        
        # Move each axis separately. Note that this checks for collisions both times.
        if dx != 0:
            self.move_single_axis(dx, 0, wall_list)
        if dy != 0:
            self.move_single_axis(0, dy, wall_list)
    
    def move_single_axis(self, dx, dy, wall_list):
        
        # Move the rect
        self.rect.x += dx
        self.rect.y += dy

        # If you collide with a wall, move out based on velocity
        for wall in wall_list:
            if self.rect.colliderect(wall.rect):
                if dx > 0: # Moving right; Hit the left side of the wall
                    self.rect.right = wall.rect.left
                if dx < 0: # Moving left; Hit the right side of the wall
                    self.rect.left = wall.rect.right
                if dy > 0: # Moving down; Hit the top side of the wall
                    self.rect.bottom = wall.rect.top
                if dy < 0: # Moving up; Hit the bottom side of the wall
                    self.rect.top = wall.rect.bottom