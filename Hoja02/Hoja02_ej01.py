y = 0 # Longitud de la rampa (max. 15)
x = 0 # Punto central de la rampa que mide 5. +2.5, -2.5 de margen
sleep = False

while x in range (-2, 3) and y<=15 and sleep == False :
    opcion = int(input('Introduce un entero: '))
                 
    if opcion<0:
        sleep = True
    elif opcion%2 == 0:
        y = y+1
    elif opcion%2 != 0 and (opcion-1)%4 == 0:
        x = x+1
    else:
        x = x-1

if not x in range (-2, 3):
    print('El pirata cae por un costado y se ahoga')
if y > 15:
    print('El pirata logra abordar el barco')
if sleep == True:
    print('El pirata se duerme sobre sobre la rampa')
