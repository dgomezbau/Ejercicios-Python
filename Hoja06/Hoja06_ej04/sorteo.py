import random

#1544

class Sorteo:

    def __init__ (self):
        self.arr_prem = random.sample(range(99999), 1544)

    def getNumPremio1_1(self):
        return self.arr_prem[0]
    
    def getNumPremio2_1(self):
        return self.arr_prem[1]

    def getNumPremio3_1(self):
        return self.arr_prem[2]

    def getNumPremio4_2(self):
        num_premio4
        for i in range(3, 4):
            num_premio4.append(self.arr_prem[i])
            return num_premio4

    def getNumPremio5_8(self):
        num_premio5
        for i in range(5, 12):
            num_premio5.append(self.arr_prem[i])
            return num_premio5
        
    def getNumPremiop_1531(self):
        num_premiop
        for i in range(13, 1544):
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
        elif premio == 7: #numeros anterior y posterior al primer premio1
            return apuesta*100
        elif premio == 8: #numeros anterior y posterior al primer premio2
            return apuesta*60
        elif premio == 9: #numeros anterior y posterior al primer premio3
            return apuesta*48
        elif premio == 10: #numeros en la centena del premio1 o 2 o 3
            return apuesta*5
        elif premio == 11: #numeros dos ultimas cifras coinciden con premio 1 2 o 3
            return apuesta*5
        elif premio == 12: #numeros anterior y posterior al primer premio1
            return apuesta*1

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

        print(numdown, numup)
        
        for i in range(numdown, numero-1):
            arr_prem.append(i)

        for i in range(numero-1, numup-1):
            arr_prem.append(i)

        return arr_prem

    def checkPremios(self, numboleto):
        p4 = False
        p5 = False
        p6 = False
        p7 = False
        
        for i in self.getNumPremio4_2():
            if numboleto == i:
                p4 = True

        for i in self.getNumPremio5_8():
            if numboleto == i:
                p5 = True

        for i in self.getNumPremiop_153():
            if numboleto == i:
                p6 = True
                
        if numboleto == self.getNumPremio1_1():
            return 1
        elif numboleto == self.getNumPremio2_1():
            return 2
        elif numboleto == self.getNumPremio3_1():
            return 3
        elif p4:
            return 4
        elif p5:
            return 5
        elif p6:
            return 6
        #elif numboleto == 
            
        
            
