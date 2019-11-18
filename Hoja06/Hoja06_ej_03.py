file = open('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\palabraoculta.txt', 'r')


palabra = 'elefante'


arr_lineas = []

pointer = 0
cont_pos = 0

def storeLines(file):
    for line in file:
        arr_lineas.append(line)
        
storeLines(file)

for i in arr_lineas:
    for j in i:
        cont_pos+=1
        if j.lower() == palabra[pointer]:
            pointer+= 1
            if pointer == len(palabra)-1:
                print('La palabra está contenida')
                break
    

print('Se han necesitado %s caractreres' % cont_pos)
