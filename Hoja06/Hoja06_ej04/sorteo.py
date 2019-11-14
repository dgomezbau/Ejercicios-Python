import random

#1544

class Sorteo:

    def __init__ (self):
        self.arr_prem = random.sample(range(99999), 1544)
        #self.num_premio1
        #self.num_premio2
        #self.num_premio3
        #self.num_premio4
        #self.num_premio5
        #self.num_premiop

    def getNumPremio1_1(self):
        return self.num_premio1 = arr_prem[0]
    
    def getNumPremio2_1(self):
        return self.num_premio2 = arr_prem[1]

    def getNumPremio3_1(self):
        return self.num_premio3 = arr_prem[2]

    def getNumPremio4_2(self):
        for i in range(3, 4):
            return self.num_premio4.append = arr_prem[i]

    def getNumPremio5_8(self):
        for i in range(5, 12):
            return self.num_premio5.append = arr_prem[i]
        
    def getNumPremiop_1531(self):
        for i in range(13, 1544):
            return self.num_premio4.append = arr_prem[i]
        
    def getPremio(self, premio, apuesta):
        if premio == 1:    
            return apuesta*15000
        elif premio == 2:
            return apuesta*5000
        elif premio == 3:
            return apuesta*2500
        elif premio == 4:
            return apuesta*1000
        elif premio == 5:
            return apuesta*250
        elif premio == 6:
            return apuesta*5

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
#Trabajar aquí:    
    def getCent(self, numero):
        if len(str(numero))>=3:
            return reversed(str(numero))[2]+reversed(str(numero))[1]+reversed(str(numero))[0]
        else:
            return '000'

    def getPremiosCent1(self):



        
