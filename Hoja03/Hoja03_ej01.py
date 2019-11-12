'''I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000'''

def roman_to_arab(num_rom):
    arr_val = []
    numero_arab = 0
    
    try:
        for i in num_rom:
            if i == 'I':
                arr_val.append(1)
            elif i == 'V':
                arr_val.append(5)
            elif i == 'X':
                arr_val.append(10)
            elif i == 'L':
                arr_val.append(50)
            elif i == 'C':
                arr_val.append(100)
            elif i == 'D':
                arr_val.append(500)
            elif i == 'M':
                arr_val.append(1000)
    except:
        print('Alguna letra es incorrecta')

    cont = len(arr_val)-1
    
    for i in reversed(arr_val):
        if cont == len(arr_val)-1:
            numero_arab = numero_arab + i
            cont = cont - 1
        else:
            if arr_val[cont] < arr_val[cont+1]:
                numero_arab = numero_arab - i
            elif arr_val[cont] >= arr_val[cont+1]:
                numero_arab = numero_arab + i
            cont = cont - 1
      
    return numero_arab

def arab_to_roman(num_arab):
    arr_val = []
    cont = 0
    num_rom = ''
    
    if num_arab >= 4000:
        print('El número es demasido grande')
    else:
        for i in reversed(str(num_arab)):
            if i == '1':
                if cont == 0:
                    arr_val.append('I')
                elif cont == 1:
                    arr_val.append('X')
                elif cont == 2:
                    arr_val.append('C')
                elif cont == 3:
                    arr_val.append('M')
            elif i == '2':
                if cont == 0:
                    arr_val.append('II')
                elif cont == 1:
                    arr_val.append('XX')
                elif cont == 2:
                    arr_val.append('CC')
                elif cont == 3:
                    arr_val.append('MM')
            elif i == '3':
                if cont == 0:
                    arr_val.append('III')
                elif cont == 1:
                    arr_val.append('XXX')
                elif cont == 2:
                    arr_val.append('CCC')
                elif cont == 3:
                    arr_val.append('MMM')
            elif i == '4':
                if cont == 0:
                    arr_val.append('IV')
                elif cont == 1:
                    arr_val.append('XL')
                elif cont == 2:
                    arr_val.append('CD')
            elif i == '5':
                if cont == 0:
                    arr_val.append('V')
                elif cont == 1:
                    arr_val.append('L')
                elif cont == 2:
                    arr_val.append('D')
            elif i == '6':
                if cont == 0:
                    arr_val.append('VI')
                elif cont == 1:
                    arr_val.append('LX')
                elif cont == 2:
                    arr_val.append('DC')
            elif i == '7':
                if cont == 0:
                    arr_val.append('VII')
                elif cont == 1:
                    arr_val.append('LXX')
                elif cont == 2:
                    arr_val.append('DCC')
            if i == '8':
                if cont == 0:
                    arr_val.append('VIII')
                elif cont == 1:
                    arr_val.append('LXXX')
                elif cont == 2:
                    arr_val.append('DCCC')
            elif i == '9':
                if cont == 0:
                    arr_val.append('IX')
                elif cont == 1:
                    arr_val.append('XC')
                elif cont == 2:
                    arr_val.append('CM')
                
            cont = cont + 1    

        for i in reversed(arr_val):
            num_rom = num_rom + i

        return num_rom

input_menu = int(input('Introduce:\n 1 - Corvertir numero romano en arábigo\n 2 - Convertir número arábigo en romano\n'))

if input_menu == 1:
    n_romano = input('Introduce un número romano: ')
    print(roman_to_arab(n_romano))
elif input_menu == 2:
    n_arab = int(input('Introduce un número arábigo: '))
    print(arab_to_roman(n_arab))
else:
    print('Opción incorrecta')
