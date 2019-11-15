import random

class Boleto:

    def __init__(self, cuantia):
        self.numero = random.randrange(100000)
        self.cuantia = cuantia

    def __init__(self, numero, cuantia):
        self.numero = numero
        self.cuantia = cuantia

    def getNumero(self):
        return self.numero

    def getCuantia:
        return self.cuantia
