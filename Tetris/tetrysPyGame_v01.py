import pygame as pg
import sys
import piezasdraw
import walls



def wall_list():

    wall_list = []
    level = [
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W            W",
    "W    E       W",
    "WWWWWWWWWWWWWW",
    ]
    x = y = 0   
    for row in level:
        for col in row:
            if col == "W":
                wall_list.append(walls.Wall((x, y)))
            x += 20
        y += 20
        x = 0
    return wall_list

def draw_walls(screen):
    for wall in wall_list():
        pg.draw.rect(screen, (255, 255, 255), wall.rect)
       
    

def main():
    screen = pg.display.set_mode((640, 480))
    clock = pg.time.Clock()
    pieza = piezasdraw.Pieza("ptest01.png")
    pieza.get_rect().move(35,35)
    all_sprites = pg.sprite.Group(pieza)


    done = False

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
                running = False
                
        key = pg.key.get_pressed()
        if key[pg.K_LEFT]:
            pieza.move(-2, 0, wall_list())
        if key[pg.K_RIGHT]:
            pieza.move(2, 0, wall_list())
        if key[pg.K_UP]:
            pieza.move(0, -2, wall_list())
        if key[pg.K_DOWN]:
            pieza.move(0, 2, wall_list())

        screen.fill((100, 100, 20))
        draw_walls(screen)
        #screen.blit(pieza.rect, (35,35))
        
        all_sprites.draw(screen)
        pg.display.flip()
        clock.tick(15)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()