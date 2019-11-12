def militar_to_habitual(hora_mili):
    cont = 0
    horas = ''
    minutos = ''
    hora_habit = ''
    for i in hora_mili:
        if cont <=1:
            horas = horas + i
        else:
            minutos = minutos + i
        cont = cont + 1

    if int(horas) < 12:
        hora_habit = horas + ':' + minutos + ' AM'
    elif int(horas) == 12:
        hora_habit = horas + ':' + minutos + ' PM'
    else:
        hora_habit = str(int(horas)-12) + ':' + minutos + ' PM'

    return hora_habit

def habitual_to_militar(hora_hab):
    cont = 0
    horas = ''
    minutos = ''
    hora_mili = ''
    for i in hora_hab:
        if cont <=1:
            horas = horas + i
        elif cont >2 and cont<=4:
            minutos = minutos + i
        elif cont == 5:
            if i == 'P':
                horas = str(int(horas)+12)
        cont = cont + 1

    hora_mili = horas + minutos

    return hora_mili
    
input_menu = int(input('Introduce:\n 1 - Corvertir hora militar a habitual\n 2 - Convertir hora habitual a militar\n'))

if input_menu == 1:
    hora_m = input('Introduce hora militar (ej: 1200): ')
    print(militar_to_habitual(hora_m))
elif input_menu == 2:
    hora_h = input('Introduce hora habitual (ej: 10:00PM): ')
    print(habitual_to_militar(hora_h))
else:
    print('Opción incorrecta')

    
            
        
