import pygame as pg
import sys
import piezas
import walls
import random
import background


def fixation(complete_estructure, rect_list, colision_down):
    if colision_down:
        for rect in rect_list:
            complete_estructure.append(rect)
    return complete_estructure
    
def draw_complete(complete_estructure, screen):
    for rect in complete_estructure:
        pg.draw.rect(screen, (0,0,0), rect, 0)

def check_for_line(back_panel, complete_estructure):
    line_index = []
    for line in back_panel:
        colision_count = 0
        for virtual_rect in line:
            for rect in complete_estructure:
                if rect.contains(virtual_rect):
                    colision_count +=1
            if colision_count == len(line):
                line_index.append(back_panel.index(line))
    return line_index

def rebuild(complete_estructure, lines, back_panel):
    for line in lines:
        for virtual_rect in back_panel[line]:
            for rect in complete_estructure:
                if rect.contains(virtual_rect):
                    complete_estructure.remove(rect)
        for rect in complete_estructure:
            if rect.y <= 50*(line-1):
                rect.y += 50

def main():
    screen = pg.display.set_mode((600, 750))
    clock = pg.time.Clock()

    walls_game = walls.Wall()
    #walls_to_colide = walls_game.create_walls()
    wall_left = walls_game.create_walls_left()
    wall_rigth = walls_game.create_walls_right()
    wall_down = walls_game.create_walls_down()

    complete_estructure = []

    back_panel = background.Back().create_back_panel()

    score = 0


    done = False
    
    while not done:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True


        lines = check_for_line(back_panel, complete_estructure)
        score += len(lines)*1000
        rebuild(complete_estructure, lines, back_panel)


        colision_wall_down = False
        colision_fixed = False
        screen.fill((100, 100, 20))


        pz = piezas.Pieza(random.randrange(1,15))
        pz_list = pz.figure_to_rect()
        pz.draw_rects(pz_list, screen)



        while not colision_wall_down and not colision_fixed:
            last_key = None
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_LEFT:
                        pz.move_left(pz_list, screen)
                        last_key = "L"
                    if event.key == pg.K_RIGHT:
                        pz.move_right(pz_list, screen)
                        last_key = "R"
            
            for pz_rect in pz_list:
                for wall_rect in wall_left:
                    if wall_rect.colliderect(pz_rect):
                        pz.move_right(pz_list, screen)

                for fixed in complete_estructure:
                    if fixed.colliderect(pz_rect):
                        if last_key == "L":
                            pz.move_right(pz_list, screen)

                for wall_rect in wall_rigth:
                    if wall_rect.colliderect(pz_rect):
                        pz.move_left(pz_list, screen)

                for fixed in complete_estructure:
                    if fixed.colliderect(pz_rect):
                        if last_key == "R":
                            pz.move_left(pz_list, screen)
                
                for fixed in complete_estructure:
                    if fixed.colliderect(pz_rect):
                        colision_fixed = True
                        pz.move_up(pz_list, screen)
                                     
                for wall_rect in wall_down:
                    if wall_rect.colliderect(pz_rect):
                        colision_wall_down = True
                        pz.move_up(pz_list, screen)
                        

            screen.fill((100, 100, 20))

            complete_estructure = fixation(complete_estructure, pz_list, colision_wall_down)
            complete_estructure = fixation(complete_estructure, pz_list, colision_fixed) 
            draw_complete(complete_estructure, screen)

            walls_game.draw_walls(wall_left, screen)
            walls_game.draw_walls(wall_rigth, screen)
            walls_game.draw_walls(wall_down, screen)

            font = pg.font.Font('freesansbold.ttf', 12)
            text = font.render("Score: " + str(score), True, (25,220,68), (255,255,255))
            textRect = text.get_rect() 
            textRect.center = (300, 20)
            screen.blit(text, textRect)

            pz.move_down(pz_list, colision_wall_down, colision_fixed, screen)

            pg.display.flip()
            clock.tick(15)
            #print(colision)

if __name__ == '__main__':
    pg.init()
    main()
    pg.quit()
    sys.exit()