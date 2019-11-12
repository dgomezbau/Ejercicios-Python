import random

preguntas = [0,0,0,0,0,0,0,0,0,0]
aciertos_primera = 0
cont=0

for i in preguntas:
    n1 = random.randint(1,10)
    n2 = random.randint(1,10)
    print('¿Cuánto es: %s x %s?' % (n1, n2))
    resp = int(input('Respuesta: '))
    while resp != n1*n2:
        preguntas[cont]=1
        print('Respuesta incorrecta')
        print('¿Cuánto es: %s x %s?' % (n1, n2))
        resp = int(input('Otro intento: '))
    cont = cont + 1       
for i in preguntas:
    if preguntas[i] == 0:
        aciertos_primera = aciertos_primera + 1

print('Has acertado %s respuestas a la primera' % aciertos_primera)
                   
    
    
    
