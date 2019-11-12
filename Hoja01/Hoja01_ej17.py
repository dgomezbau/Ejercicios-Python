num1 = int(input('Introduce número del que calcular la tabla de multiplicar: '))
num2 = int(input('Introduce el número de multiplicaciones: '))

tabla_mult = []

for i in range(num2+1):
    tabla_mult.append(num1*i)
print(tabla_mult)
