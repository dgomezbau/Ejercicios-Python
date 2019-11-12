import random

class Decision:

    def __init__(self):
        self.movimiento = []

    def primero(self):
        self.movimiento.append[2,2]

    def casillaAleatoria(self, tablero):
        check = True
        while check:
            i = random.randrange(3)
            j = random.randrange(3)
            if tablero.getTablero()[i][j] == '~':
                self.movimiento = [i,j]
                check = False
            elif not tablero.tableroLleno:
                check = False
                
    def getMovimiento(self):
        return self.movimiento


    def primeraRespuesta(self, tablero):
        cont = 0
        pos = []
        for i in range(3):
            for j in range(3):
                if tablero.getTablero()[i][j] == 'O':
                    cont += 1
                    pos.append(i)
                    pos.append(j)
                    break
        if cont == 1:
            try:
                if tablero.getTablero()[pos[0]+1] [pos[1]] == '~':
                    self.movimiento = [pos[0]+1, pos[1]]
            except IndexError:
                try:
                    if tablero.getTablero()[pos[0]-1] [pos[1]] == '~':
                        self.movimiento = [pos[0]-1, pos[1]]
                except IndexError:
                    try:
                        if tablero.getTablero()[pos[0]] [pos[1]+1] == '~':
                            self.movimiento = [pos[0], pos[1]+1]
                    except IndexError:
                        if tablero.getTablero()[pos[0]] [pos[1]-1] == '~':
                            self.movimiento = [pos[0], pos[1]-1]
                
            
            
                    
        
    def checkFilas(self, fila, valor, tablero):
        count = 0
        ocupados = []
        for j in range(3):
            if tablero.getTablero()[fila][j] == valor:
                count+=1
            else:
                hueco = j
        if count == 2 and tablero.getTablero()[fila][hueco] == '~':
            self.movimiento = [fila, hueco]
            return True
        
        else:
            return False

    def checkColumnas(self, columna, valor, tablero):
        count = 0
        hueco = 0
        for i in range(3):
            if tablero.getTablero()[i][columna] == valor:
                count+=1
            else:
                hueco = i
        if count == 2 and tablero.getTablero()[hueco][columna] == '~':
            self.movimiento = [hueco, columna]
            return True

    def checkDiagonalD(self, valor, tablero):
        count = 0
        hueco = 0
        for i in range(0,3,1):
            if tablero.getTablero()[i][i] == valor:
                count+=1
            else:
                hueco = i
        if count == 2 and tablero.getTablero()[hueco][hueco] == '~':
            self.movimiento = [hueco, hueco]
            return True
            
    def checkDiagonalI(self, valor, tablero):
        count = 0
        hueco = 0
        for i in range(2,-1,-1):
            if tablero.getTablero()[i][i] == valor:
                count+=1
            else:
                hueco = i
        if count == 2 and tablero.getTablero()[hueco][hueco] == '~':
            self.movimiento = [hueco, hueco]
            return True

    #Usar los check para que el ordenador tanbién complete una jugada de tres XXX si tiene ocasión    
    def checkJugador(self, valor, tablero):
        check = True
        for x in range(3):
            if self.checkFilas(x, valor, tablero) or self.checkColumnas(x, valor, tablero):
                check = False
                break
        if self.checkDiagonalD(valor, tablero) or self.checkDiagonalI(valor, tablero):
            check = False
        else:
            self.primeraRespuesta(tablero)
        '''if check:
            self.casillaAleatoria(tablero)'''
