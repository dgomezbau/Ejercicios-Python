import random

matrix = [[0,0,0],[0,0,0,],[0,0,0]]

def rellena_alea (matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            matriz [i][j] = random.randrange(0,9)
            print(str(matriz [i][j]) + ' ', end = '')
        print('')

def borra_casilla (matriz, fila, columna):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i == fila-1 and j == columna-1:
                matriz [i][j] = 0
            print(str(matriz [i][j]) + ' ', end = '')
        print('')

rellena_alea(matrix)

selec_fila = int(input('Selecciona fila: '))
selec_columna = int(input('Selecciona columna: '))

borra_casilla(matrix, selec_fila, selec_columna)

