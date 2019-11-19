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
ult_jugada = ''
while (tor_d.getPointer()<numero_discos-1):
    paso += 1
    print(paso)

    #Esquema básico:
    '''try:
        pasoDiscoAuto(tor_o, tor_d)
    except:
        try:
            pasoDiscoAuto(tor_o, tor_a)
        except:
            try:
                pasoDiscoAuto(tor_a, tor_d)
            except:
                try:
                    pasoDiscoAuto(tor_d, tor_a)
                except:
                    try:
                        pasoDiscoAuto(tor_a, tor_o)
                    except:
                        try:
                            pasoDiscoAuto(tor_d, tor_o)
                        except:
                            pass'''

    
    #Esquema que funciona en impares pero con movimientos extra:
    '''try:
        if ult_jugada != 'do':
            pasoDiscoAuto(tor_o, tor_d)
            ult_jugada = 'od'
        else:
            raise Exception
    except:
        try:
            if ult_jugada != 'ao':
                pasoDiscoAuto(tor_o, tor_a)
                ult_jugada = 'oa'
            else:
                raise Exception      
        except:
            try:
                if ult_jugada != 'da':
                    pasoDiscoAuto(tor_a, tor_d)
                    ult_jugada = 'ad'
                else:
                    raise Exception
            except:
                try:
                    if ult_jugada != 'ad':
                        pasoDiscoAuto(tor_d, tor_a)
                        ult_jugada = 'da'
                    else:
                        raise Exception
                except:
                    try:
                        if ult_jugada != 'oa' and ult_jugada !='da':
                            pasoDiscoAuto(tor_a, tor_o)
                            ult_jugada = 'ao'
                        else:
                            raise Exception
                    except:
                        try:
                            if ult_jugada != 'od':
                                pasoDiscoAuto(tor_d, tor_o)
                                ult_jugada = 'do'
                            else:
                                raise Exception
                        except:
                            print('Punto muerto')'''

    '''pasoDiscoAuto(tor_o, tor_d) #1D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_a) #2A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_d, tor_a) #1A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #3D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_a, tor_o) #1O
    printJuego(numero_discos)
    pasoDiscoAuto(tor_a, tor_d) #2D
    printJuego(numero_discos)
    
    pasoDiscoAuto(tor_o, tor_d) #1D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_a) #4A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_d, tor_a) #1A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_d, tor_o) #2O
    printJuego(numero_discos)
    pasoDiscoAuto(tor_a, tor_o) #1O
    printJuego(numero_discos)
    pasoDiscoAuto(tor_d, tor_a) #3A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #1D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_a) #2A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_d, tor_a) #1A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #5D
    printJuego(numero_discos)

    pasoDiscoAuto(tor_d, tor_o) #1O
    printJuego(numero_discos)
    pasoDiscoAuto(tor_a, tor_d) #2D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #1D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_a, tor_o) #3O
    printJuego(numero_discos)
    pasoDiscoAuto(tor_d, tor_a) #1A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #5D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_d, tor_o) #2O
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #5D
    printJuego(numero_discos)

    pasoDiscoAuto(tor_a, tor_o) #1O
    printJuego(numero_discos)
    pasoDiscoAuto(tor_a, tor_d) #4D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #1D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_a) #2A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_d, tor_a) #1A
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #3D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_a, tor_o) #1O
    printJuego(numero_discos)
    pasoDiscoAuto(tor_a, tor_d) #2D
    printJuego(numero_discos)
    pasoDiscoAuto(tor_o, tor_d) #1D'''
    
    
    printJuego(numero_discos)

def doTowers (n, origen, aux, destino):
        if n==1:
            print('Disk 1 from ' + origen + 'to'+ destino) 
        else:
            doTwers(n-1, origen, aux, destino)
            print('Disk ' + str(n) + ' desde ' + origen + ' to '+ destino)
    
    doTowers(5, 'O', 'A', 'D')

print('¡¡¡Conseguido!!!')      
