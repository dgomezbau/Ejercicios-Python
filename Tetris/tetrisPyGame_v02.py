import pygame as pg
import sys
import piezas

def main():
    screen = pg.display.set_mode((550, 750))
    clock = pg.time.Clock()


    done = False
    screen.fill((100, 100, 20))
    pz = piezas.Pieza(10)
    r_list = pz.figure_to_rect()
    pz.draw_rects(r_list, screen)

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
        
        
        pz.move_down(r_list)
        pg.display.flip()
        clock.tick(15)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()