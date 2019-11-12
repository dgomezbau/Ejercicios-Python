class Disco:

    def __init__(self, long):
        self.longitud = long

    def getLongitud(self):
        return self.longitud

    #Haciendolo con recursividad
    def printDisco(self, longitud):
        if longitud>1:
            return '**' + self.printDisco(longitud-1)
        else:
            return '*'
    @staticmethod
    def printDiscoAux(longitud):
        if longitud>1:
            return 2 + Disco.printDiscoAux(longitud-1)
        else:
            return 1    
        
    def printDiscoManual():
        if self.longitud == 1:
            print('*', end ='')
        elif self.longitud == 2:
            print('***', end ='')
        elif self.longitud == 3:
            print('*****', end ='')
        elif self.longitud == 4:
            print('*******', end ='')
        elif self.longitud == 5:
            print('*********', end ='')
        elif self.longitud == 6:
            print('***********', end ='')
