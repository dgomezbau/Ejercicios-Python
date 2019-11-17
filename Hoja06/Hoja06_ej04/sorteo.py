import random

#1544

class Sorteo:

    def __init__ (self, ruta):
        self.arr_prem = random.sample(range(99999), 1544)
        self.generarFichero(ruta)

    def getNumPremio1_1(self):
        return self.arr_prem[0]
    
    def getNumPremio2_1(self):
        return self.arr_prem[1]

    def getNumPremio3_1(self):
        return self.arr_prem[2]

    def getNumPremio4_2(self):
        num_premio4 = []
        for i in range(3, 5):
            num_premio4.append(self.arr_prem[i])
        return num_premio4

    def getNumPremio5_8(self):
        num_premio5 = []
        for i in range(6, 14):
            num_premio5.append(self.arr_prem[i])
        return num_premio5
        
    def getNumPremiop_1531(self):
        num_premiop = []
        for i in range(15, 1544):
            num_premiop.append(self.arr_prem[i])
        return num_premiop
        
    def getPremio(self, premio, apuesta):
        if premio == 1: #Premio1
            return apuesta*15000
        elif premio == 2: #Premio2
            return apuesta*5000
        elif premio == 3: #Premio3
            return apuesta*2500
        elif premio == 4: #Premio4
            return apuesta*1000
        elif premio == 5: #Premio5
            return apuesta*250
        elif premio == 6: #Pedrea
            return apuesta*5
        elif premio == 7: #numeros anterior y posterior al premio1
            return apuesta*100
        elif premio == 8: #numeros anterior y posterior al premio2
            return apuesta*60
        elif premio == 9: #numeros anterior y posterior al premio3
            return apuesta*48
        elif premio == 10: #numeros en la centena del premio1 o 2 o 3
            return apuesta*5
        elif premio == 11: #numeros dos ultimas cifras coinciden con premio 1 2 o 3
            return apuesta*5
        elif premio == 12: #numeros ultima cifra conincide premio1
            return apuesta*1
        else:
            return 0

    def getPremiosNext1(self):
        premios_next_1.append(self.getNumPremio1_1()-1)
        premios_next_1.append(self.getNumPremio1_1()+1)
        return premios_next_1

    def getPremiosNext2(self):
        premios_next_2.append(self.getNumPremio2_1()-1)
        premios_next_2.append(self.getNumPremio2_1()+1)
        return premios_next_2

    def getPremiosNext3(self):
        premios_next_3.append(self.getNumPremio3_1()-1)
        premios_next_3.append(self.getNumPremio3_1()+1)
        return premios_next_3

    def getPremiosCent(self, numero):
        arr_prem = []

        numup = numero + 100
        numdown = numero
        conv1 = ''
        conv2 = ''

        if len(str(numup))>=5:
            conv1 += str(numup)[0]
            conv1 += str(numup)[1]
            conv1 += str(numup)[2]
            conv1 += '0'
            conv1 += '0'

            conv2 += str(numdown)[0]
            conv2 += str(numdown)[1]
            conv2 += str(numdown)[2]
            conv2 += '0'
            conv2 += '0'

            numup = int(conv1)
            numdown = int(conv2)
            
        if len(str(numup))==4:
            conv1 += '0'
            conv1 += str(numup)[0]
            conv1 += str(numup)[1]
            conv1 += '0'
            conv1 += '0'

            conv2 += '0'
            conv2 += str(numdown)[0]
            conv2 += str(numdown)[1]
            conv2 += '0'
            conv2 += '0'

            numup = int(conv1)
            numdown = int(conv2)
        
        for i in range(numdown, numero-1):
            arr_prem.append(i)

        for i in range(numero-1, numup-1):
            arr_prem.append(i)

        return arr_prem

    def getPremiosDosUltimas(self, numero):
        arr_aux = []
        dos_ult = ''
        for i in reversed(str(numero)):
            arr_aux.append(i)

        dos_ult+=arr_aux[1]
        dos_ult+=arr_aux[0]
        
        return dos_ult #Devuelve un string con los dos últimos número

    def getPremiosReintegro(self, numero):
        arr_aux = []
        ult = ''
        for i in reversed(str(numero)):
            arr_aux.append(i)

        ult+=arr_aux[0]
        
        return ult #Devuelve un string con el último número

    def checkPremios(self, ruta, numboleto, cuantia):

        arr_aux = []
        for i in reversed(str(numboleto)):
            arr_aux.append(i)
        
        p4 = False
        p5 = False
        p6 = False
        p10 = False
        p11 = False
        p12 = False
        
        for i in self.getNumPremio4_2():
            if numboleto == i:
                p4 = True

        for i in self.getNumPremio5_8():
            if numboleto == i:
                p5 = True

        for i in self.getNumPremiop_1531():
            if numboleto == i:
                p6 = True

        for i in self.getPremiosCent(self.getNumPremio1_1()):
            if numboleto == i:
                p10 = True
                
        for i in self.getPremiosCent(self.getNumPremio2_1()):
            if numboleto == i:
                p10 = True
                
        for i in self.getPremiosCent(self.getNumPremio3_1()):
            if numboleto == i:
                p10 = True
        
                
        if numboleto == self.getNumPremio1_1():
            fichero = open(ruta, 'a')
            fichero.write('Te ha tocado el Primer Premio\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*15000) + ' €\n')
            fichero.close()
            return 1
        elif numboleto == self.getNumPremio2_1():
            fichero = open(ruta, 'a')
            fichero.write('Te ha tocado el Segundo Premio:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*5000) + ' €\n')
            fichero.close()
            return 2
        elif numboleto == self.getNumPremio3_1():
            fichero = open(ruta, 'a')
            fichero.write('Te ha tocado el Tercer Premio:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*1500) + ' €\n')
            fichero.close()
            return 3
        elif p4:
            fichero = open(ruta, 'a')
            fichero.write('Te ha tocado el Cuarto Premio:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*1000) + ' €\n')
            fichero.close()
            return 4
        elif p5:
            fichero = open(ruta, 'a')
            fichero.write('Te ha tocado el Quinto Premio:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*250) + ' €\n')
            fichero.close()
            return 5
        elif p6:
            fichero = open(ruta, 'a')
            fichero.write('Te ha tocado la pedrea:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*5) + ' €\n')
            fichero.close()
            return 6
        elif numboleto == self.getNumPremio1_1()-1 or numboleto == self.getNumPremio1_1()+1:
            fichero = open(ruta, 'a')
            fichero.write('Premio por ser un número anterior o posterior al primer premio en una unidad:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*100) + ' €\n')
            fichero.close()
            return 7
        elif numboleto == self.getNumPremio2_1()-1 or numboleto == self.getNumPremio2_1()+1:
            fichero = open(ruta, 'a')
            fichero.write('Premio por ser un número anterior o posterior al segundo premio en una unidad:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*60) + ' €\n')
            fichero.close()
            return 8
        elif numboleto == self.getNumPremio3_1()-1 or numboleto == self.getNumPremio3_1()+1:
            fichero = open(ruta, 'a')
            fichero.write('Premio por ser un número anterior o posterior al tercer premio en una unidad:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*48) + ' €\n')
            fichero.close()
            return 9
        elif p10:
            fichero = open(ruta, 'a')
            fichero.write('Premio por estar incluido en la centena de uno de los premios principales:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*5) + ' €\n')
            fichero.close()
            return 10
        elif arr_aux[0] == self.getPremiosDosUltimas(self.getNumPremio1_1())[1] and arr_aux[1] == self.getPremiosDosUltimas(self.getNumPremio1_1())[0]:
            fichero = open(ruta, 'a')
            fichero.write('Premio por coincidir las dos últimas cifras:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*5) + ' €\n')
            fichero.close()
            return 11
        elif arr_aux[0] == self.getPremiosDosUltimas(self.getNumPremio2_1())[1] and arr_aux[1] == self.getPremiosDosUltimas(self.getNumPremio2_1())[0]:
            fichero = open(ruta, 'a')
            fichero.write('Premio por coincidir las dos últimas cifras:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*5) + ' €\n')
            fichero.close()
            return 11
        elif arr_aux[0] == self.getPremiosDosUltimas(self.getNumPremio3_1())[1] and arr_aux[1] == self.getPremiosDosUltimas(self.getNumPremio3_1())[0]:
            fichero = open(ruta, 'a')
            fichero.write('Premio por coincidir las dos últimas cifras:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia*5) + ' €\n')
            fichero.close()
            return 11
        elif arr_aux[0] == self.getPremiosReintegro(self.getNumPremio1_1()):
            fichero = open(ruta, 'a')
            fichero.write('Reintegro:\n'
                + 'El número ' + str(numboleto) +  ' ha sido premiado con ' + str(cuantia) + ' €\n')
            fichero.close()
            return 12

    def generarFichero(self, ruta):
        fichero = open(ruta, 'w')

        fichero.write('Primer Premio = ' + str(self.getNumPremio1_1()) + '\n'
                   + 'Segundo Premio = ' + str(self.getNumPremio2_1()) + '\n'
                   + 'Tercer Premio = ' + str(self.getNumPremio3_1()) + '\n'
                   + 'Cuartos Premios = ' + str(self.getNumPremio4_2()) + '\n'
                   + 'Quintos Premios = ' + str(self.getNumPremio5_8()) + '\n'
                   + 'Pedrea = ' + str(self.getNumPremiop_1531()) + '\n'
                   + '==============================================\n')
        
        fichero.close()

    def anadirApuesta(self, numboleto, cuantia, ruta):
        fichero = open(ruta, 'a')
        fichero.write('Numero = ' + str(numboleto) +  '-->' 'Cuantia = ' + str(cuantia) + '\n')
        fichero.close()
        
        
        
            
