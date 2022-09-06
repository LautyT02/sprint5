from python.Cuentas.cuenta import Cuenta


class Cheque(object):
    def __init__(self,remitente=Cuenta(),destinatario=Cuenta(),monto=0.0) -> None:
        self.remitente=remitente
        self.destinatario=destinatario
        self.monto=monto