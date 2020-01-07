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
        self.figure_list = [self.cuadrado_01, self.linea4_v_02, self.linea4_h_03, self.linea2_v_04, self.linea2_h_05, self.punto_06, self.ese_v_07, self.ese_h_08, self.cuatro_v_09, self.cuatro_h_10, self.piramide_v_d_11, self.piramide_v_i_12, self.piramide_h_up_13, self.piramide_h_down_14]
        self.x = 0
        self.y = 0
        self.x_move = 1
        self.y_move = 1

    def figure_to_rect(self):
        rect_list = []
        for i in range(4):
            for j in range(4):
                if self.figure_list[self.number][i][j]:
                    rect_list.append(pg.Rect(50*i*self.x,50*j*self.y,50,50))
        return rect_list

    def draw_rects(self, rect_list, screen):
        for rect in rect_list:
            pg.draw.rect(screen, (150,150,0), rect, 2)

    def move_down(self, rect_list):
        rect_list = []
        for i in range(4):
            for j in range(4):
                if self.figure_list[self.number][i][j]:
                    rect_list.append(pg.Rect(50*i*(self.x+self.x_move),50*j*(self.y+self.y_move),50,50))
        return rect_list
