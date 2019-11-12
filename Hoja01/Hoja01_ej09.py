def hour_to_sec(horas, minutos, segundos):
    segundos_totales = (horas*60*60) + (minutos*60) + segundos
    print('Nº total de segundos = ' + str(segundos_totales))

def sec_to_hour(segundos_in):
    horas = int(segundos_in/3600)
    horas_decimal = segundos_in/3600 - horas
    minutos = int(horas_decimal*60)
    minutos_decimal = horas_decimal*60 - minutos
    segundos = int(minutos_decimal*60)
    print(str(horas) + ':' + str(minutos) + ':' + str(segundos))

tipo_conversion = int(input('Elige:\n1 - Horas --> Segundos\n2 - Segundos --> Horas\n0 - Salir '))

if tipo_conversion == 1:
    horas_in = int(input('¿Horas? '))
    minutos_in = int(input('¿Minutos? '))
    segundos_in = int(input('¿Segundos? '))
    hour_to_sec(horas_in, minutos_in, segundos_in)
    
elif tipo_conversion == 2:
    segundos_in = int(input('¿Segundos? '))
    sec_to_hour(segundos_in)

elif tipo_conversion == 0:
    print('Exit')
