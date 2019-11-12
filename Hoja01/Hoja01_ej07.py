segundos_input = int(input('¿Segundos? '))

'''horas = int(segundos_input/3600)
horas_decimal = segundos_input/3600 - horas
minutos = int(horas_decimal*60)
minutos_decimal = horas_decimal*60 - minutos
segundos = int(minutos_decimal*60)'''

horas = int(segundos_input/3600)
minutos_dec = (segundos_input%3600)/60
minutos = int(minutos_dec)
segundos = int((segundos_input%3600)%60)

print('%s:%s:%s' % (horas, minutos, segundos))
