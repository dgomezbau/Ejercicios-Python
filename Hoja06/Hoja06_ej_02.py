file = open('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\passwords.txt', 'r')

#print(file.readline())
#print(file.readline())
#file.close()

#Variables:

num_caract_linea = 0
letra_prim_palabra = ''
num_palabras_empiezan_con_letra = 0

linea=file.readline()

while linea != '':
    
