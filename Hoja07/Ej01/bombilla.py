class Bombilla:
    def __init__ (self):
        self.status = False
        self.counterOnOff = 0
        self.broken = False
    
    def switchOn(self):
        if self.counterOnOff<1000:
            if self.status:
                print('La bombilla ya estaba encendidad')
            else:
                self.counterOnOff += 1
                self.status = True
        else:
            if self.broken:
                print('La bombilla está fundida')
            else:
                self.broken = True
                print('La bombilla se ha fundido!!!')
    
    def switchOff(self):
        if self.counterOnOff<1001:
            if self.status:
                self.status = False
            else:
                if self.broken:
                    print('La bombilla está fundida')
                else:
                    print('La bombilla ya estaba apagada')
        else:
            print('La bombilla está fundida')
           

class PruebaBombilla:

    bombilla = Bombilla()

    for i in range(1000):
        bombilla.switchOn()
        bombilla.switchOff()
    
    bombilla.switchOn()
    bombilla.switchOff()

    

