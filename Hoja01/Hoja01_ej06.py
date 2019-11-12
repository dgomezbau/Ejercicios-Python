horas = int(input('¿Horas? '))
minutos = int(input('¿Minutos? '))
segundos = int(input('¿Segundos? '))

segundos_totales = (horas*60*60) + (minutos*60) + segundos
print('Nº total de segundos = ' + str(segundos_totales))
