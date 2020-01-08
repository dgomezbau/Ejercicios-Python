import pygame as pg
import sys
import piezas
import walls

def main():
    screen = pg.display.set_mode((600, 750))
    clock = pg.time.Clock()

    walls_game = walls.Wall()
    #walls_to_colide = walls_game.create_walls()
    wall_left = walls_game.create_walls_left()
    wall_rigth = walls_game.create_walls_right()
    wall_down = walls_game.create_walls_down()


    done = False
    colision_wall_left = False
    colision_wall_rigth = False
    colision_wall_down = False
    screen.fill((100, 100, 20))
    pz = piezas.Pieza(2)
    pz_list = pz.figure_to_rect()
    pz.draw_rects(pz_list, screen)

    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    pz.move_left(pz_list, colision_wall_left, screen)
                    colision_wall_rigth = False
                if event.key == pg.K_RIGHT:
                    pz.move_right(pz_list, colision_wall_rigth, screen)
                    colision_wall_left = False
        
        for pz_rect in pz_list:
            for wall_rect in wall_left:
                if wall_rect.colliderect(pz_rect):
                    colision_wall_left = True   
            for wall_rect in wall_rigth:
                if wall_rect.colliderect(pz_rect):
                    colision_wall_rigth = True              
            for wall_rect in wall_down:
                if wall_rect.colliderect(pz_rect):
                    colision_wall_down = True

        screen.fill((100, 100, 20))
        walls_game.draw_walls(wall_left, screen)
        walls_game.draw_walls(wall_rigth, screen)
        walls_game.draw_walls(wall_down, screen)
        pz.move_down(pz_list, colision_wall_down, screen)
        pg.display.flip()
        clock.tick(15)
        #print(colision)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()