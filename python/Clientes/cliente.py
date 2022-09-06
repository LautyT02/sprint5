"""
En esta clase se establecen las caracteristicas de todo cliente.
En tipos se hereda de esta clase y se modifican y agregan las caracteristicas necesarias.
"""
#self.chequeras=[] Poner solo en clientes que puedan tener chequera
class Cliente(object):
    

    def __init__(self,nombre='',apellido=''):
        self.nombre=nombre
        self.apellido=apellidoTarjeta={'deb': False, 'cred': False}
        self.tarjetas=[]
        self.puedeCuenta={'CAP': False, 'CAD': False, 'CC': False}
        self.cuentas=[]
        self.limiteExtraccion=0.0
        self.comisionTransaccion=0.0

        