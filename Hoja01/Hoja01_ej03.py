num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))

if num1>num2:
    n = num1
    num1 = num2
    num2 = n
print(num2, num1)
