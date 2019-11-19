import time
#Fichero pensado para hacer que el programa mueva los discos automáticamente. SIN COMPLETAR


import disco
import pila

def prEspa(n):
    for i in range(n):
        print(' ', end = '')

def prGuion(n):
    for i in range(n):
        print('=', end = '')

#Imprimir estado del juego

def printJuego(numero_discos):
    punt_o = tor_o.getPointer()
    punt_a = tor_a.getPointer()
    punt_d = tor_d.getPointer()
    
    for i in range(numero_discos-1, -1, -1):
        if punt_o == i:
            prEspa(numero_discos - tor_o.getPila()[i].getLongitud())
            print(tor_o.getPila()[i].printDisco(tor_o.getPila()[i].getLongitud()), end = '')
            prEspa(numero_discos - tor_o.getPila()[i].getLongitud())
            print(' ', end = '')
            punt_o -= 1
        else:
            prEspa(numero_discos*2-1)
            print(' ', end = '')

        if punt_a == i:
            prEspa(numero_discos - tor_a.getPila()[i].getLongitud())
            print(tor_a.getPila()[i].printDisco(tor_a.getPila()[i].getLongitud()), end = '')
            prEspa(numero_discos - tor_a.getPila()[i].getLongitud())
            print(' ', end = '')
            punt_a -= 1
        else:
            prEspa(numero_discos*2-1)
            print(' ', end = '')

        if punt_d == i:
            prEspa(numero_discos - tor_d.getPila()[i].getLongitud())
            print(tor_d.getPila()[i].printDisco(tor_d.getPila()[i].getLongitud()), end = '')
            prEspa(numero_discos - tor_d.getPila()[i].getLongitud())
            print(' ', end = '')
            punt_d -= 1
        else:
            prEspa(numero_discos*2-1)
            print(' ', end = '')

        print('')

    prGuion(disco.Disco.printDiscoAux(array_discos[0].getLongitud()))
    print(' ', end = '')
    prGuion(disco.Disco.printDiscoAux(array_discos[0].getLongitud()))
    print(' ', end = '')
    prGuion(disco.Disco.printDiscoAux(array_discos[0].getLongitud()))
                  
    print('')
    prEspa(int(numero_discos/2))
    print(tor_o.getNombre(), end = '')
    prEspa(int(numero_discos/2))
    print(tor_a.getNombre(), end = '')
    prEspa(int(numero_discos/2))
    print(tor_d.getNombre(), end = '')

    print('')

#Crear una lógica para que sea el propio programa el que resuelva el problema paso a paso

def pasoDiscoAuto(torre1, torre2):
    disco_obj = torre1.peek()
    if torre1.isEmpty()!=True:
        if torre2.push(disco_obj):
            torre1.pop()
        else:
            raise Exception
    else:
        raise Exception

#Crear discos

numero_discos = int(input('Introduce número de discos: '))
array_discos = []

for i in range(numero_discos, 0, -1):
    array_discos.append(disco.Disco(i))

#Crear torres

tor_o = pila.Pila(numero_discos, 'ORIGEN')
tor_a = pila.Pila(numero_discos, 'AUXILIAR')
tor_d = pila.Pila(numero_discos, 'DESTINO')

#Inicialización. Añadir discos a la torre Origen y las demás vacías

for i in range(numero_discos):
    tor_o.push(array_discos[i])


#Lógica del juego
printJuego(numero_discos)

paso = 0

arr_decisiones = []

def moverTorre(numero_discos,origen, destino, intermedio):
    if numero_discos >= 1:
        moverTorre(numero_discos-1,origen,intermedio,destino)
        
        arr_decisiones.append(origen)
        arr_decisiones.append(destino)

        moverTorre(numero_discos-1,intermedio,destino,origen)

 
moverTorre(numero_discos,"o","d","a")

print(arr_decisiones)

for i in range(0, len(arr_decisiones), 2):
    if arr_decisiones[i] == 'o' and  arr_decisiones[i+1] == 'd':
        pasoDiscoAuto(tor_o, tor_d)
    if arr_decisiones[i] == 'o' and  arr_decisiones[i+1] == 'a':
        pasoDiscoAuto(tor_o, tor_a)
    if arr_decisiones[i] == 'a' and  arr_decisiones[i+1] == 'd':
        pasoDiscoAuto(tor_a, tor_d)
    if arr_decisiones[i] == 'a' and  arr_decisiones[i+1] == 'o':
        pasoDiscoAuto(tor_a, tor_o)
    if arr_decisiones[i] == 'd' and  arr_decisiones[i+1] == 'a':
        pasoDiscoAuto(tor_d, tor_a)
    if arr_decisiones[i] == 'd' and  arr_decisiones[i+1] == 'o':
        pasoDiscoAuto(tor_d, tor_o)

    printJuego(numero_discos)
    time.sleep(1)

print('¡¡¡Conseguido!!!')      
