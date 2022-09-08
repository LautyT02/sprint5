from python.Cuentas.cuenta import Cuenta
from python.Tarjetas.tarjeta import Tarjeta
from ..cliente import Cliente

class Classic(Cliente):
    def __init__(self, nombre='', apellido='', numero=0, dni=11111111,numeroCuenta=1,numeroTarjeta=2):
        super().__init__(nombre, apellido, numero, dni)
        self.habilitarTipoTarjeta('deb')
        self.habilitarTipoCuenta('CAP')
        self.comisionTransaccion=0.01
        self.limiteExtraccion=10000
        self.cuentas.append(Cuenta(numeroCuenta,'CAP'))
        self.tarjetas.append(Tarjeta(numeroTarjeta,'deb'))
        self.tipoCliente='CLASSIC'
        self.limiteExtraccion=150000.0
    