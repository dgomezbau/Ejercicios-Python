class InputU:
    def __init__(self):
        self.casilla = [None, None]
    

    def inputJugador (self, rawinput):
        cont = 0
        fila = 0
        columna = 0
        for i in rawinput:
            if cont == 0:
                self.casilla[0] = int(i)
            if cont == 2:
                self.casilla[1] = int(i)
            cont += 1

    def getCasilla(self):
        return self.casilla

    def rawInput(self, tablero):
        introduce = input('Introduce casilla (Ejemplo: 3,2): ')
        self.inputJugador(introduce)
        while not tablero.checkCasilla(self.casilla[0]-1, self.casilla[1]-1, '~'):
            introduce = input('Introduce casilla (Ejemplo: 3,2): ')
            rawin = self.inputJugador(introduce)
        
