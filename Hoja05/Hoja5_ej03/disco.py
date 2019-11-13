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
