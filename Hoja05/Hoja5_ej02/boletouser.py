import random

class Boleto:

    def __init__(self):
        self.numeros = []
        self.reintegro = 0

    def getNumeros(self):
        return self.numeros

    def getReintegro(self):
        return self.reintegro

    def genBoleto(self):
        self.numeros = []
        num = random.randrange(1,49)
        self.numeros.append(num)
        while len(self.numeros)<6:
            num = random.randrange(1,49)
            ch = True
            for i in self.numeros:
                if i == num:
                    ch = False
                    break
            if ch:
                self.numeros.append(num)

        self.reintegro = random.randrange(0,9)
        
