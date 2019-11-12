edad = int(input('¿Cuántos años tienes? '))

mes_cumple = int(input('¿En qué mes es tu cumpleaños? '))
dia_cumple = int(input('¿Qué día es tu cumpleaños? '))

mes_actual = int(input('¿En qué mes estamos? '))
dia_actual = int(input('¿En qué día estamos? '))
ano_actual = int(input('¿En qué año estamos? '))

if mes_actual > mes_cumple:
    print('Naciste en el año ' + str(ano_actual - edad))
elif mes_actual < mes_cumple:
    print('Naciste en el año ' + str(ano_actual - edad -1))
else:
    if dia_actual > dia_cumple:
        print('Naciste en el año ' + str(ano_actual - edad))
    elif dia_actual < dia_cumple:
        print('Naciste en el año ' + str(ano_actual - edad -1))
    else:
         print('¡Felicidades, naciste en el año ' + str(ano_actual - edad) + ' tal día como hoy')

