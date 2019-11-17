import sorteo
import boleto

sor = sorteo.Sorteo('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\Hoja06_ej04\\sorteo.txt')

#participacion1 = boleto.Boleto(436, 20)
#participacion1.anadirParticipacion('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\Hoja06_ej04\\boleto.txt')
#participacion2 = boleto.Boleto(89023, 10)
#participacion2.anadirParticipacion('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\Hoja06_ej04\\boleto.txt')

boletoarch = open('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\Hoja06_ej04\\boleto.txt', 'r')
lectura = boletoarch.read()
boletoarch.close()
arr_part = lectura.split()

balance = 0
for i in range(0, len(arr_part)-1, 2):
    sor.anadirApuesta(arr_part[i],arr_part[i+1],'D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\Hoja06_ej04\\sorteo.txt')
    balance-=int(arr_part[i+1])
    balance+=sor.getPremio(sor.checkPremios('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\Hoja06_ej04\\sorteo.txt',int(arr_part[i]), int(arr_part[i+1])), int(arr_part[i+1]))

sorteofin = open('D:\\Curso Python MC\\Ejercicios Python\\Hoja06\\Hoja06_ej04\\sorteo.txt', 'a')
sorteofin.write('\n ----------------------------------\n'
             + 'Balance total = ' + str(balance))

sorteofin.close()
print(balance)


        
        
            
        
                    

#premio = sor.getPremio(sor.checkPremios(participacion1.getNumero()), participacion1.getCuantia())

