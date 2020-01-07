import time


def screen(rows, columns):
    matriz = []
    for i in range(rows):
        matriz.append([])
        for j in range(columns):
            if i==rows-1:
                matriz[i].append('=')
            elif j == 0 or j == columns-1:
                matriz[i].append('|')
            else:
                matriz[i].append(0)
            
    return matriz

def print_matriz(matriz):
    for i in range (len(matriz)):
        for j in range(len(matriz[i])):
            print(str(matriz[i][j]) + ' ', end ='')
        print('')
    
tablero = screen(15, 12)
print_matriz(tablero)