from ..cliente import Cliente
from ..cliente import Cliente
from python.Cuentas.cuenta import Cuenta
from python.Tarjetas.tarjeta import Tarjeta
from python.Chequeras.chequera import Chequera

class Gold(Cliente):
    def __init__(self, nombre='', apellido='', numero=0, dni=11111111,numeroCuenta=1,numeroTarjeta=2):
        super().__init__(nombre, apellido, numero, dni)
        self.habilitarTipoTarjeta('deb')
        self.habilitarTipoTarjeta('cred')
        self.habilitarTipoCuenta('CAP')
        self.habilitarTipoCuenta('CC')
        self.habilitarTipoCuenta('CAD')
        self.comisionTransaccion=0.0
        self.limiteExtraccion=100000
        self.cantTarjetasCredito=5
        self.descurbierto=10000
        self.cuentas.append(Cuenta(numeroCuenta,'CAP'))
        self.cuentas.append(Cuenta(numeroCuenta,'CC'))
        self.cuentas.append(Cuenta(numeroCuenta,'CAD'))
        self.tarjetas.append(Tarjeta(numeroTarjeta,'deb'))
        self.tipoCliente='GOLD'
        self.chequeras=[]

    def agregarChequera(self,chequera=Chequera()):
        if (len(self.chequeras)<2):
            self.chequeras.append(chequera)