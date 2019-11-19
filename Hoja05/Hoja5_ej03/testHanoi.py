'''def doTowers (n, origen, aux, destino):
        if n==1:
            print('Disk 1 from ' + origen + 'to'+ destino) 
        else:
            doTowers(n-1, origen, aux, destino)
            print('Disk ' + str(n) + ' desde ' + origen + ' to '+ destino)
    

doTowers(5, 'O', 'A', 'D')'''


def moverTorre(altura,origen, destino, intermedio):
    if altura >= 1:
        moverTorre(altura-1,origen,intermedio,destino)
        moverDisco(origen,destino)
        moverTorre(altura-1,intermedio,destino,origen)

def moverDisco(desde,hacia):
    print("mover disco de",desde,"a",hacia)

moverTorre(5,"A","B","C")
