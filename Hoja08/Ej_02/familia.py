class Family:

    def __init__(self, nombre):
        self.nombre = nombre
        self.generaciones = 0

    def addGeneracion(self):
        self.generaciones+=1

    def removeGeneracion(self):
        self.generaciones-=1

    