def celsius_to_fahrenheit(grad_cels):
    grad_far = (9/5)*grad_cels + 32
    return grad_far

def fahrenheit_to_celsius(grad_far):
    grad_cels = (grad_far - 32)/(9/5)
    return grad_cels

tipo_conversion = int(input('Elige:\n1 - Celsius --> Fahrenheit\n2 - Fahrenheit --> Celsius\n'))

if tipo_conversion == 1:
    cels_in = float(input('Introduce un valor en grados celsius: '))
    print(str(celsius_to_fahrenheit(cels_in)) + ' F')

elif tipo_conversion == 2:
    far_in = float(input('Introduce un valor en grados fahrenheit: '))
    print(str(fahrenheit_to_celsius(far_in)) + ' ºC')
