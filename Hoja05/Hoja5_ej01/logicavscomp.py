import tablero as tab
import inteligencia as inte
import inputU

# ------------------------------

def input_jugador (in_jug):
    cont = 0
    fila = 0
    columna = 0
    for i in in_jug:
        if cont == 0:
            fila = int(i)
        if cont == 2:
            columna = int(i)
        cont += 1
        
    return (fila, columna)

tablero = tab.Tablero()
ia = inte.Decision()
in_u = inputU.InputU()

tablero.printTablero()

while tablero.tableroLleno():
    in_u.rawInput(tablero)
    tablero.setCasilla(in_u.getCasilla()[0]-1, in_u.getCasilla()[1]-1, 'O')
    
    tablero.printTablero()
    
    if tablero.tableroLleno():
        print('Turno del oponente')
        #ia.casillaAleatoria(tablero)
        ia.checkJugador('O', tablero)
        casilla_o = ia.getMovimiento()
        tablero.setCasilla(casilla_o[0], casilla_o[1], 'X')
        tablero.printTablero()
        
    else:
        print('Fin del Juego')
        

if tablero.checkGlobal('O') > tablero.checkGlobal('X'):
    print ('Has ganado')
elif tablero.checkGlobal('O') < tablero.checkGlobal('X'):
    print ('Has perdido')
else:
    print('Empate')
    
