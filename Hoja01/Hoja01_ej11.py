num1 = int(input('Introduce el primer número: '))
num2 = int(input('Introduce el segundo número: '))
num3 = int(input('Introduce el tercer número: '))

list_num = [num1, num2, num3]

if num1>num2 or num1>num3 or num2>num3:
    list_num.sort()
    num1=list_num[0]
    num2=list_num[1]
    num3=list_num[2]
    

print(list_num)
print(num1, num2, num3)
