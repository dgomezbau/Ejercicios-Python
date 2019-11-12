def euro_to_dollar(cantidad_euro):
    factor_conv = 1.11 #1 € --> 1.11 $
    cantidad_dollar = cantidad_euro*factor_conv
    return cantidad_dollar

def dollar_to_euro(cantidad_dollar):
    factor_conv = 1.11 #1 € --> 1.11 $
    cantidad_euro = cantidad_dollar/factor_conv
    return cantidad_euro

tipo_conversion = int(input('Elige:\n1 - Euro --> Dollar\n2 - Dollar --> Euro\n'))

if tipo_conversion == 1:
    cant_eur = float(input('Introduce un valor en Euros: '))
    print(str(euro_to_dollar(cant_eur)) + ' $')
    
if tipo_conversion == 2:
    cant_doll = float(input('Introduce un valor en Dollar: '))
    print(str(dollar_to_euro(cant_doll)) + ' €')
