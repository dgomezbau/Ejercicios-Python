import sorteosim
import boletouser

'''time = 0
juegos_por_semana = 2
juegos_por_año = 52*juegos_por_semana
juegos_tot = time*juegos_por_año'''

saldo = 0
tactual = 0
num_sorteos = 0
num_semanas = 0

bol = boletouser.Boleto()
resultado = sorteosim.SorteoSim()

input_años = int(input('Introduce los años que quieres simular: '))
input_frecuencia = int(input('Introduce la frecuencia (sorteos) de comprobación de saldo: '))

while tactual<=input_años:

    saldo -= 1
    bol.genBoleto()
    resultado.sorteo()
    saldo += resultado.comprobacion(bol)

    if num_sorteos%input_frecuencia == 0:
        print(saldo)

    if num_sorteos%2==0:
        num_semanas+=1

    if num_semanas%52==0:
        tactual+=1

    num_sorteos += 1
    
    
    
