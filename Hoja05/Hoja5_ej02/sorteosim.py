import random

class SorteoSim:

    def __init__(self):
        self.numeros = []
        self.complementario = 0
        self.reintegro = 0

    def getNumeros(self):
        return self.numeros
    
    def getComplementario(self):
        return self.complementario

    def getReintegro(self):
        return self.reintegro

    def sorteo(self):
        self.numeros = []
        num = random.randrange(1,49)
        self.numeros.append(num)
        while len(self.numeros)<7:
            num = random.randrange(1,49)
            ch = True
            for i in self.numeros:
                if i == num:
                    ch = False
                    break
            if ch:
                self.numeros.append(num)
                
        self.complementario = self.numeros[6]
        self.numeros.pop(6)

        self.reintegro = random.randrange(0,9)
            
    def comprobacion(self, boleto):
        acierto = 0
        comple = False
        reint = False
        
        for i in self.numeros:
            for j in boleto.getNumeros():
                if i == j:
                    acierto += 1
        if acierto == 5:
            for i in boleto.getNumeros():
                if i == self.complementario:
                    comple = True
                    acierto +=1
        if self.reintegro == boleto.reintegro:
            reint = True

        if acierto == 6:
            return self.premios('pre1')
            
        elif acierto == 5 and comple:
            return self.premios('pre2')
            
        elif acierto == 5:
            return self.premios('pre3')
            
        elif acierto == 4:
            return self.premios('pre4')
            
        elif acierto == 3:
            return self.premios('pre5')
            
        elif acierto <3 and reint :
            return self.premios('pre6')
            
        else:
            return 0

    def premios(self, premio):
        #Acierta 6
        if premio == 'pre1':
            return 1727262
        #Acierta 5 + complementario
        elif premio == 'pre2':
            return 43181
        #Acierta 5
        elif premio == 'pre3':
            return 2227
        #Acierta 4
        elif premio == 'pre4':
            return 67
        #Acierta 3
        elif premio == 'pre5':
            return 8
        #Acierta reintegro
        elif premio == 'pre6':
            return 1
            
         
