ano = int(input('Introduce un año '))

if ano%4 == 0 and ano%100 != 0:
    print('El año ' + str(ano) + ' es bisiesto')
elif ano%4 == 0 and ano%100 == 0 and ano%400 == 0:
    print('El año ' + str(ano) + ' es bisiesto')
else:
    print('El año ' + str(ano) + ' no es bisiesto')
