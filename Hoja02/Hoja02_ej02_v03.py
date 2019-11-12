import time
import random

n_sets_part = int(input('Selecciona numero de sets: ' ))

juegos_a = 0
juegos_b = 0

sets_a = 0
sets_b = 0

cont_set = 1

print('Comienza el partido entre A y B')    
while juegos_a < 7 and juegos_b < 7 and sets_a < int(n_sets_part/2)+1 and sets_b < int(n_sets_part/2)+1:
    time.sleep(2)    
    randomnum = random.randint(0,1)
    if randomnum == 0:
        juegos_a = juegos_a+1
        print('Juego ganado por el jugador A')
    elif randomnum == 1:
        juegos_b = juegos_b+1
        print('Juego ganado por el jugador B')

    print('----------------------\nSet actual: %s\nJugador A(%s) %s // %s Jugador B(%s)\n----------------------' % (cont_set, sets_a, juegos_a, juegos_b, sets_b))
    

    if juegos_a >=6 and juegos_a-juegos_b >= 2 or juegos_a >=7:
        print('El jugador A gana el set')
        sets_a = sets_a + 1
        cont_set = cont_set + 1
        juegos_a = 0
        juegos_b = 0

    elif juegos_b >=6 and juegos_b-juegos_a >= 2 or juegos_b >=7:
        print('El jugador B gana el set')
        sets_b = sets_b + 1
        cont_set = cont_set + 1
        juegos_a = 0
        juegos_b = 0
else:
    if sets_a > sets_b:
        print('El jugador A ha ganado el partido')
    elif sets_b > sets_a:
        print('El jugador B ha ganado el partido')
print('----------------------\nResultado final: \nJugador A %s sets // Jugador B %s sets\n----------------------' % (sets_a, sets_b))
