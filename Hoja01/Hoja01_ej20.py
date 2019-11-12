numero = int(input('Introduce un número: '))

def calc_factorial(numero):
    fact = 1
    for i in range(1, numero+1):
        fact = fact*i
    return fact

print('El factorial de ' + str(numero) + ' es ' + str(calc_factorial(numero)))
