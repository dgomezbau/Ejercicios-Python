iteraciones = int(input('¿Cuántos números triangulares? '))

lista_tri = []
n_tri = 1
cont = 2
for i in range(iteraciones):
    lista_tri.append(n_tri)
    n_tri = n_tri + cont
    cont = cont + 1

print(lista_tri)
