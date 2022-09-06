from ..cliente import Cliente

class Classic(Cliente):
    def __init__(self, nombre='', apellido='', numero=0, dni=11111111):
        super().__init__(nombre, apellido, numero, dni)
        self.habilitarTipoTarjeta('deb')
        self.habilitarTipoCuenta('CAP')
        self.comisionTransaccion=0.01
        self.limiteExtraccion=10000