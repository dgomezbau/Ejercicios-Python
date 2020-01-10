import pygame as pg

class Pieza():

    def __init__(self, number):
        self.number = number-1
        
        self.cuadrado_01 = [[True,True,False,False],[True,True,False,False],[False,False,False,False],[False,False,False,False]]

        self.linea4_v_02 = [[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False]]
        self.linea4_h_03 = [[True,True,True,True],[False,False,False,False],[False,False,False,False],[False,False,False,False]]

        self.linea2_v_04 = [[True,False,False,False],[True,False,False,False],[False,False,False,False],[False,False,False,False]]
        self.linea2_h_05 = [[True,True,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]

        self.punto_06 = [[True,False,False,False],[True,False,False,False],[True,False,False,False],[True,False,False,False]]

        self.ese_v_07 = [[True,False,False,False],[True,True,False,False],[False,True,False,False],[False,False,False,False]]
        self.ese_h_08 = [[False,True,True,False],[True,True,False,False],[False,False,False,False],[False,False,False,False]]

        self.cuatro_v_09 = [[False,True,False,False],[True,True,False,False],[True,False,False,False],[False,False,False,False]]
        self.cuatro_h_10 = [[True,True,False,False],[False,True,True,False],[False,False,False,False],[False,False,False,False]]

        self.piramide_v_d_11 = [[True,False,False,False],[True,True,False,False],[True,False,False,False],[False,False,False,False]]
        self.piramide_v_i_12 = [[False,True,False,False],[True,True,False,False],[False,True,False,False],[False,False,False,False]]
        self.piramide_h_up_13 = [[False,True,False,False],[True,True,True,False],[False,False,False,False],[False,False,False,False]]
        self.piramide_h_down_14 = [[True,True,True,False],[False,True,False,False],[False,False,False,False],[False,False,False,False]]

        self.ele_derecha_v_down_15 = [[True,False,False,False],[True,False,False,False],[True,True,False,False],[False,False,False,False]]
        self.ele_derecha_h_up_16 = [[False,False,True,False],[True,True,True,False],[False,False,False,False],[False,False,False,False]]
        self.ele_derecha_v_up_17 = [[True,True,False,False],[False,True,False,False],[False,True,False,False],[False,False,False,False]]
        self.ele_derecha_h_down_18 = [[True,True,True,False],[True,False,False,False],[False,False,False,False],[False,False,False,False]]

        self.ele_izquierda_v_down_19 = [[False,True,False,False],[False,True,False,False],[True,True,False,False],[False,False,False,False]]
        self.ele_izquierda_h_up_20 = [[False,False,True,False],[True,True,True,False],[False,False,False,False],[False,False,False,False]]
        self.ele_izquierda_v_up_21 = [[True,True,False,False],[False,True,False,False],[False,True,False,False],[False,False,False,False]]
        self.ele_izquierda_h_down_22 = [[True,True,True,False],[False,False,True,False],[True,True,False,False],[False,False,False,False]]

        self.figure_list = [self.cuadrado_01, self.linea4_v_02, self.linea4_h_03, self.linea2_v_04, self.linea2_h_05, self.punto_06, self.ese_v_07, self.ese_h_08, self.cuatro_v_09, self.cuatro_h_10, self.piramide_v_d_11, self.piramide_v_i_12, self.piramide_h_up_13, self.piramide_h_down_14]
        
        self.x = 250
        self.y = 0
        self.x_move = 50
        self.y_move = 10

    def figure_to_rect(self):
        rect_list = []
        for i in range(4):
            for j in range(4):
                if self.figure_list[self.number][i][j]:
                    rect_list.append(pg.Rect((50*i)+self.x,50*j,50,50))
        return rect_list

    def draw_rects(self, rect_list, screen):
        for rect in rect_list:
            pg.draw.rect(screen, (150,150,0), rect, 0)

    def move_down(self, rect_list, colision_wall, colision_fixed, screen):
        if not colision_wall and not colision_fixed:
            for rect in rect_list:
                rect.y += self.y_move
                pg.draw.rect(screen, (150,150,0), rect, 0)

    def move_up(self, rect_list, screen):
        for rect in rect_list:
            rect.y -= self.y_move
            pg.draw.rect(screen, (150,150,0), rect, 0)
        

    def move_left(self, rect_list, screen):
        for rect in rect_list:
            rect.x -= self.x_move
            pg.draw.rect(screen, (150,150,0), rect, 0)

    def move_right(self, rect_list, screen):
        for rect in rect_list:
            rect.x += self.x_move
            pg.draw.rect(screen, (150,150,0), rect, 0)

    def getX_move(self):
        return self.x_move

    def setX_move(self, xm):
        self.x_move = xm

    def getY_move(self):
        return self.y_move

    def setY_move(self, ym):
        self.y_move = ym