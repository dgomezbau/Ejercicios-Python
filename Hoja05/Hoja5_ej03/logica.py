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


#Función para pasar los discos de una pila a otra    
def pasoDisco(torre1, torre2):
    disco_obj = torre1.peek()
    if torre2.push(disco_obj):
        torre1.pop()
    else:
        print('No puedes mover ahí')
    

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


printJuego(numero_discos)
movimientos = 0
#Lógica del juego

while (tor_d.getPointer()<numero_discos-1):
    print(movimientos)

    user_o = input('Introduce pila de la que tomar el último disco (o, a, d): ')
    user_d = input('Introduce pila en la que depositar el disco (o, a, d): ')

    if user_o == user_d:
        print('No has movido el disco')
    elif user_o == 'o' and user_d == 'a':
        pasoDisco(tor_o, tor_a)

    elif user_o == 'o' and user_d == 'd':
        pasoDisco(tor_o, tor_d)

    elif user_o == 'a' and user_d == 'o':
        pasoDisco(tor_a, tor_o)

    elif user_o == 'a' and user_d == 'd':
        pasoDisco(tor_a, tor_d)

    elif user_o == 'd' and user_d == 'o':
        pasoDisco(tor_d, tor_o)

    elif user_o == 'd' and user_d == 'a':
        pasoDisco(tor_d, tor_a)

    else:
        print('Input incorreco')

    printJuego(numero_discos)

    movimientos += 1

print('PUZZLE COMPLETADO') 
    
