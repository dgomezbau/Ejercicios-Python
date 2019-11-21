class SaldoInsuficiente(Exception):
    pass

class CuentaBanco():

    def __init__(self, numero:str, titular:str):
        self.numero = numero
        self.titular = titular
        self.saldo = 0
        self.bloqueada = False

    def consultarSaldo(self):
        return self.saldo
    
    def ingresarDinero(self, cantidad:float):
        if self.bloqueada:
            print('No se puede ingresar, la cuenta está bloqueada')
        else:
            self.saldo = self.saldo+cantidad

    def retirarDinero(self, cantidad:float):
        if self.bloqueada:
            try:
                if cantidad<=self.saldo:
                    self.saldo = self.saldo-cantidad
                else:
                    raise SaldoInsuficiente('No hay suficiente saldo en la cuenta')
            except SaldoInsuficiente:
                print('Error:', SaldoInsuficiente)
        else:
            print('No se puede retirar, la cuenta está bloqueada')

    def cambioTitular(self, nuevoTit:str):
        if self.bloqueada:
            print('No se puede cambiar el titular, la cuenta está bloqueada')
        else:
            if nuevoTit=='':
                print('El nombre no es válido')
            else:
                self.titular = nuevoTit

    def bloquear(self):
        if self.bloqueada:
            print('No se puede bloquear, la cuenta ya está bloqueada')
        else:
            self.bloqueada = True

    def desbloquear(self):
        self.bloqueada = False

    def imprimirDatos(self):
        print('Nº de cuenta:', self.numero
        + '\n Titular:', self.titular
        + '\n Saldo:', str(self.saldo)
        + '\n Bloqueo:', str(self.bloqueada))

class PruebaCoche():

    cuentaAhorro = CuentaBanco('ES5865632015478965412300', 'Daniel Gómez')
    cuentaAhorro.imprimirDatos()
    cuentaAhorro.ingresarDinero(1500)
    print(cuentaAhorro.consultarSaldo())
    cuentaAhorro.retirarDinero(3000)
    cuentaAhorro.bloquear()
    cuentaAhorro.retirarDinero(500)
    cuentaAhorro.imprimirDatos()
    cuentaAhorro.desbloquear()
    cuentaAhorro.cambioTitular('Paco')
    cuentaAhorro.imprimirDatos()


