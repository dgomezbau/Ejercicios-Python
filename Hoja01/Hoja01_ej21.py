numero = int(input('Introduce un número: '))

def calc_divisores(numero):
    divisores = []
    for i in range(1, numero+1):
        if numero%i == 0:
            divisores.append(i)
    return divisores

print('Los divisres de ' + str(numero) + ' son ' + str(calc_divisores(numero)))
