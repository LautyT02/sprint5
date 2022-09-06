from python.Cuentas.cuenta import Cuenta
class Transaccion(object):
    def __init__(self,remitente=Cuenta(),destinatario=Cuenta(),monto=0.0,tipo='') -> None:
        self.remitente=remitente
        self.destinatario=destinatario
        self.monto=monto
        self.tipo=tipo