import random
import time

def tablero_vacio(tamano):
    matriz = []
    for i in range(tamano):
        matriz.append([])
        for j in range(tamano):
            matriz[i].append(0)
            
    return matriz

def relleno_aleat(matriz):
    celulas = 0
    while celulas <= len(matriz)**2/2.5:
        i = random.randrange(len(matriz))
        j = random.randrange(len(matriz))
        if matriz[i][j] != "■":
            matriz[i][j] = "■"
            celulas += 1
        
    return matriz        

def print_matriz(matriz):
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            print(str(matriz[i][j]) + ' ', end ='')
        print('')


def calcula_nuvecinas(matriz, i, j):
    nuvecinas = 0
    for x in range(i-1, i+2):
        for y in range(j-1, j+2):
            try:
                if matriz[x][y] == "■" and (x!=i or y!=j) and x>=0 and y>=0:
                    nuvecinas += 1
            except IndexError:
                nuvecinas = nuvecinas
                
    return nuvecinas

def nueva_celula(tablero, fila, columna):
    fila -= 1
    columna -= 1
    if tablero[fila][columna] != "■":
        tablero[fila][columna] = "■"
    else:
        print('La casilla ya está ocupada')
    
    return tablero

def elimina_celula(tablero, fila, columna):
    fila -= 1
    columna -= 1
    if tablero[fila][columna] != 0:
        tablero[fila][columna] = 0
    else:
        print('La casilla ya está vacía')
    
    return tablero

def next_gen(tablero):
    tablero_nuevo=tablero_vacio(len(tablero))
    for i in range (len(tablero)):
        for j in range(len(tablero[i])):
            if tablero[i][j] == "■":
                if calcula_nuvecinas(tablero, i, j) < 1:
                    tablero_nuevo[i][j] = 0
                elif calcula_nuvecinas(tablero, i, j) == 3:
                    tablero_nuevo[i][j] = tablero[i][j]
                    check = True
                    while check:
                        f = random.randrange(len(tablero))
                        c = random.randrange(len(tablero))
                        if tablero[f][c] != "■" and tablero_nuevo[f][c] != "■":
                            tablero_nuevo[f][c] = "■"
                            check = False
                        else:
                            check = True
                elif calcula_nuvecinas(tablero, i, j) > 3:
                    tablero_nuevo[i][j] = 0
                else:
                    tablero_nuevo[i][j] = tablero[i][j]
                    
    return tablero_nuevo

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

def menu_tx():
    print('--------------------------------------------\n'
          +'1 - Genera tablero aleatorio\n'
          + '2 - Genera tablero vacio\n'
          + '3 - Introduce un nuevo bicho en la coordenada (i,j)\n'
          + '4 - Eliminar un bicho de la coordenada (i,j)\n'
          + '5 - Simular n generaciones\n'
          + '--------------------------------------------\n'
          + '0 - Salir')

#Variables
tamano_tablero=5
generacion = 1
menu = -1
tablero_actual = []
tablero_futuro = []

#----------------------


while menu !=0:
    
    menu_tx()
    menu = int(input('Selecciona un opción: '))
    if menu == 1:
        tamano_tablero = int(input('Introduce tamaño del tablero (max 20)'))
        if tamano_tablero<=20:
            tablero_actual = relleno_aleat(tablero_vacio(tamano_tablero))
            print_matriz(tablero_actual)
        else:
            print('El tablero es demasiado grande')
        
    elif menu == 2:
        if tamano_tablero<=20:
            tamano_tablero = int(input('Introduce tamaño del tablero (max 20)'))
            tablero_actual = tablero_vacio(tamano_tablero)
            print_matriz(tablero_actual)
        else:
            print('El tablero es demasiado grande')
        
    elif menu == 3:
        if len(tablero_actual) == 0:
            print('Debes crear un tablero primero')
        else:
            coord = input_jugador(input('Introduce coordenada (ej. 2,4)'))
            tablero_actual = nueva_celula(tablero_actual, coord[0], coord[1])
            print_matriz(tablero_actual)

    elif menu == 4:
        if len(tablero_actual) == 0:
            print('Debes crear un tablero primero')
        else:
            coord = input_jugador(input('Introduce coordenada (ej. 2,4)'))
            tablero_actual = elimina_celula(tablero_actual, coord[0], coord[1])
            print_matriz(tablero_actual)

    elif menu == 5:
        n_generaciones = int(input('¿Cuántas generaciones quieres simular?'))
        print_matriz(tablero_actual)
        
        while generacion <= n_generaciones:
            
            
            print('Calculando la próxima generación ' + ' ', end ='')
            time.sleep(0.5)
            print('... ', end ='')
            time.sleep(0.5)
            print('... ', end ='')
            time.sleep(0.5)
            print('... ', end ='')
            time.sleep(0.5)
            print('... ')

            tablero_futuro = next_gen(tablero_actual)
            print('---------- Generación:' + str(generacion) + ' ----------')
            print_matriz(tablero_futuro)

            generacion += 1
            tablero_actual = tablero_futuro
