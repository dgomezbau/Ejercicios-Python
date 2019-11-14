file = open('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\passwords.txt', 'r')

def getNumPalabras(linea):
    palabras = 1
    for i in linea:
        if i == ' ':
            palabras+=1
    return palabras

def getNumCaracteres(linea):
    caracteres = 0
    for i in linea:
        if i != '\n':
            caracteres+=1
    return caracteres

def getLetraPrimeraPalabra(linea):
    ult_letra = ''
    for i in range(len(linea)):
        if linea[i] == ' ':
            ult_letra = linea[i-1]
            break
    return ult_letra

def checkLetraFinalPalabras(linea):
    arr_ult_letra = []
    for i in range(len(linea)):
        if linea[i] == ' ':
            arr_ult_letra.append(linea[i-1])
        elif linea [i] == '\n':
            arr_ult_letra.append(linea[i-1])
        elif linea [i] !='\n' and i == len(linea)-1:
            arr_ult_letra.append(linea[i])

    return arr_ult_letra

def storeLines(file):
    for line in file:
        arr_lineas.append(line)


arr_lineas = []
storeLines(file)
cont_linea = 0
tot_palabras = 0
tot_caracteres = 0
tot_espacios = 0

for i in arr_lineas:
    cont_linea += 1
    print('\nEn la línea número %s:\n' % cont_linea)
    print('Hay %s palabras' % getNumPalabras(i))
    tot_palabras += getNumPalabras(i)
    espacios = getNumPalabras(i)-1
    tot_espacios += espacios
    print('Hay %s caracteres' % getNumCaracteres(i))
    tot_caracteres += getNumCaracteres(i)
    print('La primera palabra termina en %s' % getLetraPrimeraPalabra(i))
    cont_palletra = 0
    for j in checkLetraFinalPalabras(i):
        if j == getLetraPrimeraPalabra(i):
            cont_palletra += 1
    print('%s palabras acaban en %s'% (cont_palletra, getLetraPrimeraPalabra(i)))

print('\nTOTAL:')
print('Palabras = %s' % tot_palabras)
print('Caracteres = %s' % tot_caracteres)
print('Líneas = %s' % cont_linea)
print('Longitud media de cada palabra = %s' % ((tot_caracteres-tot_espacios)/tot_palabras))

    
    
    
    
    
