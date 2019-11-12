base = float(input('Introduce logitud de la base: '))
altura = float(input('Introduce longitud de la altura: '))

def area_tri (base, altura):
    area = base*altura/2
    return area

print('Area del triangulo:' + str(area_tri(base, altura)))
