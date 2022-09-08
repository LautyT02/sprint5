from ..cliente import Cliente
from ...Direccion.direccion import Direccion

class Gold(Cliente):
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