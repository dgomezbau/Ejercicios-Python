class Tablero:
    def __init__(self):
        self.tablero = []
        for i in range(3):
            self.tablero.append([])
            for j in range(3):
                self.tablero[i].append('~')

    def printTablero(self):
        for i in range (len(self.tablero)):
            for j in range(len(self.tablero[i])):
                print(str(self.tablero[i][j]) + ' ', end ='')
            print('')

    def setCasilla(self, fila, columna, val):
        try:
            if self.tablero[fila][columna] == '~' and fila >=0 and columna >=0 and self.tableroLleno():
                self.tablero[fila][columna] = val
            else:
                print('No puedes mover allí')
        except IndexError:
            print('La casilla no existe')

    def tableroLleno(self):
        cont = False
        for i in range(3):
            for j in range(3):
                if self.tablero[i][j] == '~':
                    cont = True
        return cont
    
    def getTablero(self):
        return self.tablero

    def checkCasilla(self, fila, columna, valor):
        try:
            if self.tablero[fila][columna] == valor and fila>=0 and columna >=0:
                return True
            else:
                return False
        except IndexError:
            return False
        
    def checkFilas(self, fila, valor):
        count = 0
        for j in range(3):
            if self.tablero[fila][j] == valor:
                count+=1
        if count == 3:
            return True
        else:
            False

    def checkColumnas(self, columna, valor):
        count = 0
        for i in range(3):
            if self.tablero[i][columna] == valor:
                count+=1
        if count == 3:
            return True
        else:
            False

    def checkDiagonalD(self, valor):
        count = 0
        for i in range(0,3,1):
            if self.tablero[i][i] == valor:
                count+=1
        if count == 3:
            return True
        else:
            False
            
    def checkDiagonalI(self, valor):
        count = 0
        for i in range(2,-1,-1):
            if self.tablero[i][i] == valor:
                count+=1
        if count == 3:
            return True
        else:
            False

    def checkGlobal(self, valor):
        lineas = 0
        for x in range(3):
            if self.checkFilas(x, valor):
                lineas += 1
        for x in range(3):
            if self.checkColumnas(x, valor):
                lineas += 1
        if self.checkDiagonalD(valor):
            lineas += 1
        if self.checkDiagonalI(valor):
            lineas += 1
            
        return lineas


            
