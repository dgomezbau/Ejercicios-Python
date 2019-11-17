import random

class Boleto:
    def __init__(self, numero, cuantia):
        if numero >= 0 and numero < 100000:
            self.numero = numero
        else:
            raise Exception
        self.cuantia = cuantia

    def getNumero(self):
        return self.numero

    def elegirNumeroAleatorio(self):
        self.numero = random.randrange(100000)

    def getCuantia(self):
        return self.cuantia

    def anadirParticipacion(self, ruta):
        participacion = open(ruta, 'a')
        participacion.write(str(self.numero) + ' ' + str(self.cuantia) + '\n')
        participacion.close()
