def calc_divisores(numero):
    divisores = []
    for i in range(1, numero+1):
        if numero%i == 0:
            divisores.append(i)
    return divisores

def check_num_perf(numero):
    suma_divisores = 0
    lista_div = calc_divisores(numero)
    for i in range(len(lista_div)-1):
        suma_divisores = suma_divisores + lista_div[i]
    if suma_divisores == numero:
        return True
    else:
        return False

#itera = int(input('¿Cuántos números perfectos? '))

'''lista_num_perf = []
count = 0
num = 1
while count < 4:
    if check_num_perf(num) == True:
        lista_num_perf.append(num)
        num = num + 1
        count = count + 1
    else:
        num = num + 1'''

lista_num_perf = []
num = 1
while len(lista_num_perf) < 4:
    if check_num_perf(num) == True:
        lista_num_perf.append(num)
        num = num + 1
    else:
        num = num + 1
        
print('Lista de números perfectos: %s' % (lista_num_perf))
