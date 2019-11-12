# 1 metro = 39.27"
# 12 pulgdas = 1 pie

def metro_to_pie(metros):
    pulgadas = metros*39.27
    pie = pulgadas/12
    return pie

metros_in = float(input('Introduce distancia en metros: '))

print(str(metro_to_pie(metros_in)) + ' pies')
