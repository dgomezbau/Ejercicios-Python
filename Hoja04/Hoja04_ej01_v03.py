import random
import time


def tablero_vacio(tamano):
    num_barcos = 0
    matriz = []
    for i in range(tamano):
        matriz.append([])
        for j in range(tamano):
            matriz[i].append('WW')
            
    return matriz

def posicion_barco(matriz, i, j, orientacion, len_barco_consigno):
    cont = 0
    try:
        if len_barco_consigno>0:
            if orientacion == 0:
                for j in range(j, j+len_barco_consigno):
                    if matriz[i][j] == 'WW':
                        cont = cont + 1
            elif orientacion == 1:
                for i in range(i, i+len_barco_consigno):
                    if matriz[i][j] == 'WW':
                        cont = cont + 1
                        
        elif len_barco_consigno<0:
            if orientacion == 0:
                for j in range(j+len_barco_consigno, j):
                    if matriz[i][j] == 'WW' and j >= 0:
                        cont = cont + 1
            elif orientacion == 1:
                for i in range(i+len_barco_consigno, i):
                    if matriz[i][j] == 'WW' and i >= 0:
                        cont = cont + 1
    except IndexError:
        return False

    if cont == abs(len_barco_consigno):
        return True
    else:
        return False    

def coloca_barco(matriz, tamano, barco):
    check = True
    while check:
        orientacion = random.randrange(2)
        i = random.randrange(tamano)
        j = random.randrange(tamano)

        if orientacion == 0:
            if posicion_barco(matriz, i, j, orientacion, len(barco)):
                check = False
                for j in range(j, j+len(barco)):
                    matriz[i][j] = barco[0]
                return matriz        
            elif posicion_barco(matriz, i, j, orientacion, ((-1)*len(barco))):
                check = False
                for j in range(j-len(barco), j):
                    matriz[i][j] = barco[0]
                return matriz    
            
        elif orientacion == 1:
            if posicion_barco(matriz, i, j, orientacion, len(barco)):
                check = False
                for i in range(i, i+len(barco)):
                    matriz[i][j] = barco[0]
                return matriz    
            elif posicion_barco(matriz, i, j, orientacion, ((-1)*len(barco))):
                check = False
                for i in range(i-len(barco), i):
                    matriz[i][j] = barco[0]
                return matriz    

def radar_crear(tamano):
    matriz = [['-' for x in range(tamano)] for y in range(tamano)]
    
    return matriz

def titulo_tablero(tipo):
    if tipo == 'flota':
        print('Estado de tu flota')
    elif tipo == 'radar':
        print('Estado de la flota enemiga')

def print_matriz(matriz):
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            print(matriz[i][j] + ' ', end ='')
        print('')

def tablero_completo(matriz, tamano):
    matriz = coloca_barco(matriz, tamano, barco_5)
    matriz = coloca_barco(matriz, tamano, barco_4)
    matriz = coloca_barco(matriz, tamano, barco_3A)
    matriz = coloca_barco(matriz, tamano, barco_3B)
    matriz = coloca_barco(matriz, tamano, barco_2A)
    matriz = coloca_barco(matriz, tamano, barco_2B)
    return matriz
         

def comparar_posicion_valor(matriz, fila, columna, valor):
    fila = fila - 1
    columna = columna - 1
    try:
        if matriz[fila][columna] == valor and fila>=0 and columna >=0:
            return True
        else:
            return False
    except IndexError:
        return False


#NO funciona correctamente
def comprobar_hundido(matriz, i, j):
    cont = 0
    i=i-1
    j=j-1
    try:
        if (matriz[i+1][j] == 'WW' or matriz[i-1][j] == 'TT' and i>=0):
            cont = cont + 1
    except IndexError:
        cont = cont + 1
    try:
        if (matriz[i][j-1] == 'WW' or matriz[i][j-1] == 'TT' and j>=0):
            cont = cont + 1
    except IndexError:
        cont = cont + 1
    try:
        if (matriz[i][j+1] == 'WW' or matriz[i][j+1] == 'TT'):
            cont = cont + 1
    except IndexError:
        cont = cont + 1
    try:
        if (matriz[i+1][j] == 'WW' or matriz[i+1][j] == 'TT'):
            cont = cont + 1
    except IndexError:
        cont = cont + 1

    if cont == 4:
        return True
#Revisar
def comprueba_valor_cardinal (matriz, fila, columna, valor):
    if (comparar_posicion_valor(matriz, fila-1, columna, valor)
        or comparar_posicion_valor(matriz, fila, columna-1, valor)
        or comparar_posicion_valor(matriz, fila, columna+1, valor)
        or comparar_posicion_valor(matriz, fila+1, columna, valor)):
        return True
    else:
        return False
        
     
    
#revisar
def info_disparo(matriz_objetivo, fila, columna):
    if comparar_posicion_valor(matriz_objetivo, fila, columna, 'WW'):
        print('Agua')
    elif comparar_posicion_valor(matriz_objetivo, fila, columna, 'TT'):
        print('Ya has disparado a ese barco en esa posición')
    else:
        if comprueba_valor_cardinal(matriz_objetivo, fila, columna, matriz_objetivo[fila-1][columna-1]):
            print('Tocado')        
        else:
            print('Hundido')

def input_jugador (in_jug, tamano):
    cont = 0
    fila = 0
    columna = 0
    for i in in_jug:
        if cont == 0:
            fila = int(i)
        if cont == 2:
            columna = int(i)
        cont = cont + 1
        
    return (fila, columna)

def comprueba_user_input(coordenada, tamano):
    if coordenada[0]>tamano and coordenada[1]>tamano:
        return True
    else:
        return False

def generar_coord_aleatoria(tamano):
    coord_al = [random.randrange(tamano)+1, random.randrange(tamano)+1]

    return coord_al

def status(matriz):
    check = False
    for i in range(len(matriz)):
        if check == False:
            for j in range(len(matriz[i])):
                if  (matriz[i][j] == 'B1'
                    or matriz[i][j] == 'B2'
                    or matriz[i][j] == 'B3'
                    or matriz[i][j] == 'B4'
                    or matriz[i][j] == 'B5'
                    or matriz[i][j] == 'B6'):
                    check = True
                    break
            
    return check

def disparo(matriz_objetivo, matriz_radar, fila, columna):
    fila_co = fila - 1
    columna_co = columna - 1
    if matriz_objetivo[fila_co][columna_co] == 'WW':
        matriz_radar[fila_co][columna_co] = 'X'
    elif (matriz_objetivo[fila_co][columna_co] == 'B1'
        or matriz_objetivo[fila_co][columna_co] == 'B2'
        or matriz_objetivo[fila_co][columna_co] == 'B3'
        or matriz_objetivo[fila_co][columna_co] == 'B4'
        or matriz_objetivo[fila_co][columna_co] == 'B5'
        or matriz_objetivo[fila_co][columna_co] == 'B6'):
        matriz_objetivo[fila_co][columna_co] = 'TT'
        matriz_radar[fila_co][columna_co] = 'V'


def disparo_ordenador_norep(radar, tamano):
    check = True
    while(check):
        coord = generar_coord_aleatoria(tamano)
        if radar [coord[0]-1][coord[1]-1] == '-':
            check = False
            return coord


        
#Variables globales:
barco_5 = ['B1', 'B1', 'B1', 'B1', 'B1']
barco_4 = ['B2', 'B2', 'B2', 'B2']
barco_3A = ['B3', 'B3', 'B3']
barco_3B = ['B4', 'B4', 'B4']
barco_2A = ['B5', 'B5']
barco_2B = ['B6', 'B6']

tamano_tablero = 8

acierto_j = True
acierto_o = True

tablero_j = tablero_completo(tablero_vacio(tamano_tablero), tamano_tablero)
tablero_o = tablero_completo(tablero_vacio(tamano_tablero), tamano_tablero)
radar_j = radar_crear(tamano_tablero)
radar_o = radar_crear(tamano_tablero)


print('Comienzo del juego. Ésta es tu flota:')
print_matriz(tablero_j)
print('-----------------')
print_matriz(tablero_o)

while status(tablero_j) and status(tablero_o):

    #---------------------------------------------------------------

    while(acierto_j and status(tablero_o)):
        
        coord_jugador = input_jugador(input('Introduce fila y columna para disparar (Ejemplo: 3,2): '), tamano_tablero)
        while comprueba_user_input(coord_jugador, tamano_tablero):
            print('El panel no es tan grande')
            coord_jugador = input_jugador(input('Introduce fila y columna (Ejemplo: 3,2): '))

        if (comparar_posicion_valor(tablero_o, coord_jugador[0], coord_jugador[1], 'B1')
            or comparar_posicion_valor(tablero_o, coord_jugador[0], coord_jugador[1], 'B2')
            or comparar_posicion_valor(tablero_o, coord_jugador[0], coord_jugador[1], 'B3')
            or comparar_posicion_valor(tablero_o, coord_jugador[0], coord_jugador[1], 'B4')
            or comparar_posicion_valor(tablero_o, coord_jugador[0], coord_jugador[1], 'B5')
            or comparar_posicion_valor(tablero_o, coord_jugador[0], coord_jugador[1], 'B6')):
            
            acierto_j = True
        else:
            acierto_j = False
        
        print('------------------------------------------------------')
        info_disparo(tablero_o, coord_jugador[0], coord_jugador[1])
        print('------------------------------------------------------')
        disparo(tablero_o, radar_j, coord_jugador[0], coord_jugador[1])

        titulo_tablero('flota')
        print_matriz(tablero_j)
        titulo_tablero('radar')
        print_matriz(radar_j)

        acierto_o = True
        
    #---------------------------------------------------------------
        
    while(acierto_o and status(tablero_j)):
        print('Turno del oponente' + ' ', end ='')
        time.sleep(0.5)
        print('... ', end ='')
        time.sleep(0.5)
        print('... ', end ='')
        time.sleep(0.5)
        print('... ')
        time.sleep(0.5)

        coord_o = disparo_ordenador_norep(radar_o, tamano_tablero)

        if (comparar_posicion_valor(tablero_j, coord_o[0], coord_o[1], 'B1')
            or comparar_posicion_valor(tablero_j, coord_o[0], coord_o[1], 'B2')
            or comparar_posicion_valor(tablero_j, coord_o[0], coord_o[1], 'B3')
            or comparar_posicion_valor(tablero_j, coord_o[0], coord_o[1], 'B4')
            or comparar_posicion_valor(tablero_j, coord_o[0], coord_o[1], 'B5')
            or comparar_posicion_valor(tablero_j, coord_o[0], coord_o[1], 'B6')):
            
            acierto_o = True
        else:
            acierto_o = False
       
        print(coord_o)
        print('------------------------------------------------------')
        info_disparo(tablero_j, coord_o[0], coord_o[1])
        print('------------------------------------------------------')
        disparo(tablero_j, radar_o, coord_o[0], coord_o[1])

        titulo_tablero('flota')
        print_matriz(tablero_j)

        acierto_j = True

if status(tablero_j) == False and status(tablero_o) == False:
    print('Empate')
elif status(tablero_j) == False:
    print('Has perdido')
else:
    print('Has ganado')


