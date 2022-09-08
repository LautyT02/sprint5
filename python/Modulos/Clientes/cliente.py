"""
En esta clase se establecen las caracteristicas de todo cliente.
En tipos se hereda de esta clase y se modifican y agregan las caracteristicas necesarias.
"""
#Imports
from ..Direccion.direccion import Direccion
from ..Transacciones.transaccion import Transaccion

class Cliente(object):
    

    def __init__(self,nombre='',apellido='', numero=0, dni=11111111,direccion=Direccion(),numeroCuenta=190):
        #Datos Personales del cliente
        self.nombre=nombre
        self.apellido=apellido
        self.numero=numero
        self.dni=dni
        self.direccion=direccion
        #Cuentas
        self.numeroCuenta=numeroCuenta
        self.cajaAhorroPesos=False
        self.cajaAhorroDolares=False
        self.cuentaCorriente=False
        self.descurbierto=0
        #Tarjetas
        self.cantTarjetasDebito=0
        self.maxTarjetasCredito=0
        self.cantTarjetasCredito=0
        #Chequeras
        self.maxChequeras=0
        self.cantChequeras=0
        #Transacciones
        self.transacciones=[]
        self.limiteExtraccion=0.0
        self.comisionTransaccion=1.0
        self.limTransfRecivda=0
        #Tipo de Cleinte
        self.tipoCliente=''        
    
    #Métodos puedeX
    def puedeCrearChequera(self):
        return (self.maxChequeras>0)

    def puedeCrearTarjetaCredito(self):
        return (self.maxTarjetasCredito)
        
    def puedeComprarDolares(self):
        return self.cuentaAhorroDolares

    #Setters
    def setDescubierto(self,descubierto):
        self.descurbierto=descubierto

    def setLimiteExtraccion(self,limite):
        self.limiteExtraccion=float(limite)
    
    def setComisionTransferencia(self,comision):
        self.comisionTransaccion=float(comision)

    def setLimiteTransferenciaRecivida(self,limiteTransefrencia):
        self.limTransfRecivda=float(limiteTransefrencia)

    #Método Transacciones
    def agregarTransaccion(self,data):
        self.transacciones[data["numero"]]=Transaccion(self,data)

    #Métodos str
    def __str__(self):
        _str="{ \n"
        _str+=self.strDatosCliente() + ", \n"
        _str+=str(self.direccion) + ", \n"
        _str+=self.strTransacciones() + "\n "
        _str+="}"
        return 

    def strDatosCliente(self):
        strDatosCliente='"numero": ' + str(self.numero) + ", \n"
        strDatosCliente+='"nombre": ' + self.nombre + ", \n"
        strDatosCliente+='"apellido": ' + self.apellido + ", \n"
        strDatosCliente+='"DNI": ' + str(self.dni) + ", \n"
        strDatosCliente+='"tipo". ' + self.tipoCliente + ", \n"
        return strDatosCliente

    def strTransacciones(self):
        stringTransacciones='"transacciones": [ \n'
        for i in range(len(self.transacciones)):
            stringTransacciones+=str(self.transacciones[i])+", \n"
        stringTransacciones+="]"
        return stringTransacciones

