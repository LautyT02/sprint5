"""
En esta clase se establecen las caracteristicas de todo cliente.
En tipos se hereda de esta clase y se modifican y agregan las caracteristicas necesarias.
"""
#Imports
from .Transacciones.transaccion import Transaccion

class Cliente(object):
    

    def __init__(self,nombre:str,apellido:str, numero:int, dni:int,direccion:object,numeroCuenta:int):
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
        self.descubierto=0
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
        return self.cajaAhorroDolares

    #Setters
    def setDescubierto(self,descubierto):
        self.descubierto=descubierto

    def setLimiteExtraccion(self,limite):
        self.limiteExtraccion=float(limite)
    
    def setComisionTransferencia(self,comision):
        self.comisionTransaccion=float(comision)

    def setLimiteTransferenciaRecivida(self,limiteTransefrencia):
        self.limTransfRecivda=float(limiteTransefrencia)

    #Método Transacciones
    def agregarTransaccion(self,data):
        self.transacciones.append(Transaccion(self,data))

    #Métodos str
    def __str__(self):
        _str="{ \n"
        _str+=self.strDatosCliente()
        _str+=str(self.direccion) + ", \n"
        _str+=self.strTransacciones() + "\n "
        _str+="}"
        return _str

    def strDatosCliente(self):
        strDatosCliente="\t"+'"numero": ' + str(self.numero) + ", \n"
        strDatosCliente+="\t"+'"nombre": "' + self.nombre + '", \n'
        strDatosCliente+="\t"+'"apellido": "' + self.apellido + '", \n'
        strDatosCliente+="\t"+'"DNI": "' + str(self.dni) + '", \n'
        strDatosCliente+="\t"+'"tipo": "' + self.tipoCliente + '", \n'
        return strDatosCliente
    
    def strTransacciones(self):
        stringTransacciones='\t"transacciones": ['
        for i in range(len(self.transacciones)):
            stringTransacciones+=str(self.transacciones[i])+", \n\t"
            if i<(len(self.transacciones)-1):
                stringTransacciones+="\t"
        stringTransacciones+="]"
        return stringTransacciones

