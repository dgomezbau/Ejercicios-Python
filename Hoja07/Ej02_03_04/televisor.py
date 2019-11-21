class FueraDeRango(Exception):
    pass


class Televisor:

    def __init__(self, marcaIni:str, modeloIni:str, anioIni:int):
        self.marca = marcaIni
        self.modelo = modeloIni

        if anioIni>1950 and anioIni <=2200:
            self.anio = anioIni
        else:
            self.anio = 2000
            print('El año está fuera del rango y será fijado en 2000')

        self.panoramica = False
        self.stereo = False
        self.encendida = False
        self.volumen = 0
        self.canal = 0
    
    def encender(self):
        if self.encendida:
            pass
        else:
            self.encendida = True
            print('Se ha encendido el televisor')

    def apagar(self):
        if self.encendida:
            self.encendida = False
            print('Se ha apagado el televisor')
        else:
            pass

    def seleccionarCanal(self, nuevoCanal: int):
        if self.encendida:
            try:
                if nuevoCanal>=0 and nuevoCanal<100:
                    self.canal = nuevoCanal
                    print('Canal seleccionado %s' % self.canal)
                else:
                    raise FueraDeRango('Valores fuera de rango')
            except FueraDeRango:
                print('Se ha producido un error:', FueraDeRango)
        else:
            print('Televisor apagado')



    def obtenerCanal(self):
        if self.encendida:
            return self.canal
        else:
            print('Televisor apagado')

    def subirCanal(self):
        if self.encendida:
            nuevoCanal = self.canal+1
            try:
                if nuevoCanal>=0 and nuevoCanal<100:
                    self.canal = nuevoCanal
                    print('Canal seleccionado %s' % self.canal)
                else:
                    raise FueraDeRango('Valores fuera de rango')
            except FueraDeRango:
                print('Se ha producido un error:', FueraDeRango)
        else:
            print('Televisor apagado')

    def bajarCanal(self):
        if self.encendida:
            nuevoCanal = self.canal-1
            try:
                if nuevoCanal>=0 and nuevoCanal<100:
                    self.canal = nuevoCanal
                    print('Canal seleccionado %s' % self.canal)
                else:
                    raise FueraDeRango('Valores fuera de rango')
            except FueraDeRango:
                print('Se ha producido un error:', FueraDeRango)
        else:
            print('Televisor apagado')

    def cambiarVolumen(self, nuevoVolumen: int):
        if self.encendida:
            try:
                if nuevoVolumen>=0 and nuevoVolumen<=100:
                    self.volumen = nuevoVolumen
                    print('Volumen seleccionado %s' % self.volumen)
                else:
                    raise FueraDeRango('Valores fuera de rango')
            except FueraDeRango:
                print('Se ha producido un error:', FueraDeRango)
        else:
            print('Televisor apagado')
    
    def imprimirCaracteristicas(self):
        print(self.marca + '\n'
        + self.modelo + '\n'
        + str(self.anio) + '\n'
        + str(self.panoramica) + '\n'
        + str(self.stereo) + '\n'
        + str(self.encendida) + '\n'
        + str(self.volumen) + '\n'
        + str(self.canal) + '\n')




class PruebaTelevisor:

    tele = Televisor('Sony', 'Trinitron 4', 2003)

    tele.imprimirCaracteristicas()
    tele.encender()
    print('Canal actual:', tele.obtenerCanal())
    tele.bajarCanal()
    tele.seleccionarCanal(23)
    tele.subirCanal()
    tele.cambiarVolumen(300)
    tele.cambiarVolumen(50)
    tele.imprimirCaracteristicas()
    tele.apagar()
    tele.seleccionarCanal(60)
    tele.apagar()

