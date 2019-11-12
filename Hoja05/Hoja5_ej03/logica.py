import disco
import pila

def prEspa(n):
    for i in range(n):
        print(' ', end = '')

def prGuion(n):
    for i in range(n):
        print('=', end = '')

def printJuego(numero_discos):
    punt_o = tor_o.getPointer()
    punt_a = tor_a.getPointer()
    punt_d = tor_d.getPointer()
    
    for i in range(numero_discos-1, -1, -1):
        if punt_o == i:
            prEspa(numero_discos - tor_o.getPila()[i].getLongitud())
            print(tor_o.getPila()[i].printDisco(tor_o.getPila()[i].getLongitud()))
            prEspa(numero_discos - tor_o.getPila()[i].getLongitud())
            print(' ', end = '')
            punt_o -= 1
        else:
            prEspa(numero_discos*2)
            print(' ', end = '')

        if punt_a == i:
            prEspa(numero_discos - punt_a.getPila()[i].getLongitud())
            print(tor_a.getPila()[i].printDisco(tor_a.getPila()[i].getLongitud()))
            prEspa(numero_discos - punt_a.getPila()[i].getLongitud())
            print(' ', end = '')
            punt_a -= 1
        else:
            prEspa(numero_discos*2)
            print(' ', end = '')

        if punt_d == i:
            prEspa(numero_discos - punt_d.getPila()[i].getLongitud())
            print(tor_d.getPila()[i].printDisco(tor_d.getPila()[i].getLongitud()))
            prEspa(numero_discos - punt_d.getPila()[i].getLongitud())
            print(' ', end = '')
            punt_d -= 1
        else:
            prEspa(numero_discos*2)
            print(' ', end = '')

        print('')

    prGuion(disco.Disco.printDiscoAux(array_discos[0].getLongitud()))
    print(' ', end = '')
    prGuion(disco.Disco.printDiscoAux(array_discos[0].getLongitud()))
    print(' ', end = '')
    prGuion(disco.Disco.printDiscoAux(array_discos[0].getLongitud()))
                  
    print('')
    print(tor_o.getNombre(), end = '')
    prEspa(numero_discos)
    print(tor_a.getNombre(), end = '')
    prEspa(numero_discos)
    print(tor_d.getNombre(), end = '')
    


numero_discos = int(input('Introduce número de discos: '))
array_discos = []

for i in range(numero_discos, 0, -1):
    array_discos.append(disco.Disco(i))


tor_o = pila.Pila(numero_discos, 'ORIGEN')
tor_a = pila.Pila(numero_discos, 'AUXILIAR')
tor_d = pila.Pila(numero_discos, 'DESTINO')

#Inicialización. Añadir discos a la torre Origen y las demás vacías

for i in range(numero_discos):
    tor_o.push(array_discos[i])

printJuego(numero_discos)
