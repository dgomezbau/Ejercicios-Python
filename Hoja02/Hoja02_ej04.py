dni =  int(input('Introduce el DNI: '))

def calc_dni_letra(numero_dni):
    alfa=dni%23
    letras = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B', 'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    return letras[alfa]

print(calc_dni_letra(dni))
