from .cliente import Cliente
from ..Direccion.direccion import Direccion

class Classic(Cliente):
    def __init__(self, nombre='', apellido='', numero=0, dni=11111111, direccion=Direccion(), numeroCuenta=1):
        #Datos Personales del Cliente y numeroCuenta
        super().__init__(nombre, apellido, numero, dni, direccion, numeroCuenta)
        #Cuentas
        self.cuentaAhorroPesos=True
        #Tarjetas
        self.cantTarjetasDebito=1
        #Transacciones
        self.setLimiteExtraccion(10000)
        self.setComisionTransferencia(0.01)
        self.setLimiteTransferenciaRecivida(150000)
        #Tipo de Cleinte
        self.tipoCliente='CLASSIC'

class Gold(Cliente):
    def __init__(self, nombre='', apellido='', numero=0, dni=11111111, direccion=Direccion(), numeroCuenta=1):
        #Datos Personales del Cliente y numeroCuenta
        super().__init__(nombre, apellido, numero, dni, direccion, numeroCuenta)
        #Cuentas
        self.cuentaAhorroDolares=True
        self.cuentaCorriente=True
        self.setDescubierto(10000)
        #Tarjetas
        self.cantTarjetasDebito=1
        self.maxTarjetasCredito=1
        #Chequeras
        self.maxChequeras=1
        #Transacciones
        self.setLimiteExtraccion(20000)
        self.setComisionTransferencia(0.005)
        self.setLimiteTransferenciaRecivida(500000)
        #Tipo de Cleinte
        self.tipoCliente='GOLD'    

class Black(Cliente):
    def __init__(self, nombre='', apellido='', numero=0, dni=11111111, direccion=Direccion(), numeroCuenta=1):
        #Datos Personales del Cliente y numeroCuenta
        super().__init__(nombre, apellido, numero, dni, direccion, numeroCuenta)
        #Cuentas
        self.cajaAhorroPesos=True
        self.cajaAhorroDolares=True
        self.cuentaCorriente=True
        self.setDescubierto(10000)
        #Tarjetas
        self.maxTarjetasCredito=5
        #Chequeras
        self.maxChequeras=2
        #Transacciones
        self.setLimiteExtraccion(100000)
        self.setComisionTransferencia(0.0)
        self.setLimiteTransferenciaRecivida(-1)#Para indicar que no hay
        #Tipo de Cleinte
        self.tipoCliente='BLACK'