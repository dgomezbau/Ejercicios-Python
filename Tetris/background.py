import pygame as pg

class Back():

    def __init__(self):
        pass

    def create_back_panel(self):
        panel = []
        for j in range (14):
            line =[]
            for i in range(1,11):
                rect = pg.Rect(50*i,50*j,50,50)
                line.append(rect)
            panel.append(line)

        return panel
