"""
En esta clase se establecen las caracteristicas de todo cliente.
En tipos se hereda de esta clase y se modifican y agregan las caracteristicas necesarias.
"""
#Imports. Hay que arjetas y cuentas
from ..Tarjetas.tarjeta import Tarjeta
from ..Chequeras.chequera import Chequera 
from ..Cuentas.cuenta import Cuenta
from .direccion import Direccion
#self.chequeras=[] Poner solo en clientes que puedan tener chequera
class Cliente(object):
    

    def __init__(self,nombre='',apellido='', numero=0, dni=11111111,direccion=Direccion()):
        self.nombre=nombre
        self.apellido=apellido
        self.numero=numero
        self.dni=dni
        self.puedeTarjeta={'deb': False, 'cred': False}
        self.tarjetas=[]
        self.puedeCuenta={'CAP': False, 'CAD': False, 'CC': False}
        self.cuentas=[]
        self.transacciones=[]
        self.limiteExtraccion=0.0
        self.comisionTransaccion=1.0
        self.tipoCliente=''
        self.direccion=direccion
    
    def habilitarTipoCuenta(self,tipo):
        self.puedeCuenta[tipo]=True

    def habilitarCuenta(self,numero,tipo):
        if self.puedeCuenta[tipo]:
            self.cuentas.append(Cuenta(numero,tipo))
    

    def setLimiteExtraccion(self,limite):
        self.limiteExtraccion=float(limite)
    
    def setComisionTransaccion(self,comision):
        self.comisionTransaccion=float(comision)


    def habilitarTipoTarjeta(self,tipo):
        self.puedeTarjeta[tipo]=True

    def habilitarTarjeta(self,numero,tipo):
        if self.puedeTarjeta[tipo]:
            self.tarjetas.append(Tarjeta(numero,tipo))

    def __str__(self):
        return "{numero: "+str(self.numero)+",nombre: "+self.nombre+",apellido: "+self.apellido+",DNI: "+str(self.dni)
    
