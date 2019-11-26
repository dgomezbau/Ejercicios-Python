import coche

class PruebaCoche:

    coche = coche.Coche('5466-FNZ', 60, 200, 7.1)

    coche.repostar(15)
    coche.arrancarMotor()
    coche.fijarVelocidad(80)
    coche.recorrerDistancia(10)
    coche.fijarVelocidad(120)
    coche.recorrerDistancia(300)