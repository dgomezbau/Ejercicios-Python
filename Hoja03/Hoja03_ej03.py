def crea_lista(longitud):
    lista = []
    for i in range(longitud):
        lista.append(0)
    return lista

def mod_lista(lista, posicion, nuevo_entero):
    for i in range(len(lista)):
        if i == posicion-1:
            lista[i] = nuevo_entero
    return lista

input_menu = -1
lista_user = []

while input_menu !=0:
    input_menu = int(input('Introduce:\n 1 - Crear nueva lista (La anterior será eliminada)\n 2 - Rellenar valores de lista\n 3 - Imprimir lista\n 0 - Exit\n'))
    
    if input_menu == 1:
        long = int(input('Introduce tamaño de lista: '))
        lista_user = crea_lista(long)
        print('[+] La lista ha sido creada')
        print(lista_user)
    elif input_menu == 2:
        if len(lista_user)>0:
            new_pos = int(input('Introduce la posición a rellenar: '))
            if new_pos > len(lista_user):
                print('[-] La lista solo dispone de: ' + str(len(lista_user)) + ' posiciones')
            else:
                new_val = int(input('Introduce el valor: '))
                lista_user = mod_lista(lista_user, new_pos, new_val)
                print('[+] El valor ha sido introducido')
        else:
            print('[-] Aún no has creado ninguna lista')
    elif input_menu == 3:
        print(lista_user)
        
print('Has avandonado el programa')       

