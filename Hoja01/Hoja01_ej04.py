edad = int(input('¿Cuántos años tienes? '))
cumplido = input('¿Has cumplido ya este año? (y/n) ')
ano_actual = int(input('¿En qué año estamos? '))

if cumplido == 'y':
    print('Naciste en: ' + str(ano_actual - edad))
elif cumplido == 'n':
    print('Naciste en: ' + str(ano_actual - edad -1))
