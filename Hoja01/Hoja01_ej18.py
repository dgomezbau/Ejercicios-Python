numero = int(input('Introduce un número: '))

n_tri = 1
check = False
cont = 2
while (n_tri <= numero):
    if numero == n_tri:
        check = True
    n_tri = n_tri + cont
    cont = cont + 1
       
if check == True:
    print(str(numero) + ' es un número triangular')
else:
    print(str(numero) + ' no es un número triangular')
