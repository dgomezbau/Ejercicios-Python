class Coche():

    def __init__ (self, matricula:str, maxLitrosDeposito:float, velodidadMaxima:float, consumoMedio100km:float):
        self.matricula = matricula

        if maxLitrosDeposito>=0:
            self.maxLitrosDeposito = maxLitrosDeposito
        else:
            self.maxLitrosDeposito = 50
        
        if velodidadMaxima>=0:
            self.velocidadMaxima = velodidadMaxima
        else:
            self.velocidadMaxima = 180

        if consumoMedio100km>=0:
            self.consumoMedio100km = consumoMedio100km
        else:
            self.consumoMedio100km = 7.5

        self.maxLitrosReserva = maxLitrosDeposito*0.15
        self.consumoMedio100km = consumoMedio100km

        self.motorArrancado = False
        self.estaEnReserva = False
        self.numLitrosActual = 0.0
        self.velocidadActual = 0.0
        self.kilometraje = 0.0


    def setMatricula(self, nuevaMatricula:str):
        self.matricula = nuevaMatricula

    def getMatricula(self):
        return self.matricula

    def getMaxLitrosDeposito(self):
        return self.maxLitrosDeposito

    def getMaxLitrosReserva(self):
        return self.maxLitrosReserva

    def getVelocidadMaxima(self):
        return self.velocidadMaxima

    def getConsumoMedio100km(self):
        return self.consumoMedio100km
    
    def getMotorArrancado(self):
        return self.motorArrancado

    def getEstaEnReserva(self):
        return

    def getNumeroLitrosActual(self):
        return self.numLitrosActual

    def getVelocidadActual(self):
        return self.velocidadActual

    def getKilometraje(self):
        return self.kilometraje

    def arrancarMotor(self):
        if self.motorArrancado:
            print('El coche con matrícula %s ya está en marcha' % self.matricula)
        else:
            if self.numLitrosActual>0:
                self.motorArrancado = True
                print('El coche con matrícula %s ha arrancado' % self.matricula)
                if self.numLitrosActual<= self.maxLitrosReserva:
                    print('El coche con matrícula %s esta en reserva' % self.matricula)
            else:
                print('El coche con matrícula %s no se puede arrancar por falta de gasolina' % self.matricula)

    def pararMotor(self):
         if self.motorArrancado:
            self.motorArrancado = False
            print('El coche con matrícula %s se ha parado' % self.matricula)

    def repostar(self, litros:float):
        if litros+self.numLitrosActual>self.maxLitrosDeposito:
            self.numLitrosActual = self.maxLitrosDeposito
            print('El coche con matrícula %s ha rebosado el depósito' % self.matricula)
        elif litros+self.numLitrosActual>0 and litros+self.numLitrosActual <=self.maxLitrosDeposito:
            self.numLitrosActual = self.numLitrosActual+litros
            print('El coche con matrícula %s tiene %s litros de combustible' % (self.matricula, self.numLitrosActual))
        else:
            print('El coche con matrícula %s tiene %s litros de combustible' % (self.matricula, self.numLitrosActual))
        
    def fijarVelocidad(self, velocidad:float):
        if self.motorArrancado:
            if velocidad>self.velocidadMaxima:
                self.velocidadActual = self.velocidadMaxima
                print('El coche con matrícula %s va a una velocidad de %s km/h' % (self.matricula, self.velocidadActual))
            elif velocidad<0:
                self.velocidadActual = 0
                print('El coche con matrícula %s va a una velocidad de %s km/h' % (self.matricula, self.velocidadActual))
            else:
                self.velocidadActual = velocidad
                print('El coche con matrícula %s va a una velocidad de %s km/h' % (self.matricula, self.velocidadActual))
        else:
            print('El coche con matrícula %s está parado' % self.matricula)

    def recorrerDistancia(self, kilometros:float):
        if self.motorArrancado and self.velocidadActual>0:
            if kilometros <=0:
                print('Distancia no válida')
            else:
                consumoInstantaneo = self.consumoMedio100km*(1+(self.velocidadActual-100)/100)
                litrosNecesarios = kilometros*consumoInstantaneo/100
                if litrosNecesarios<self.numLitrosActual:
                    self.kilometraje+=kilometros
                    print('El coche con matrícula %s ha recorrido %s Km' % (self.matricula, kilometros))
                    self.numLitrosActual-=litrosNecesarios
                    if self.numLitrosActual<= self.maxLitrosReserva:
                        self.estaEnReserva = True
                else:
                    distanciaReal = 100*self.numLitrosActual/consumoInstantaneo
                    self.kilometraje+= distanciaReal
                    self.numLitrosActual = 0
                    self.estaEnReserva = True
                    print('El coche con matrícula %s ha recorrido %s Km' % (self.matricula, distanciaReal))
                    print('El coche con matrícula %s está sin combustible' % self.matricula)
                    print('El coche con matrícula %s está parado' % self.matricula)

        else:
            print('El coche con matrícula %s no se está moviendo' % self.matricula)
