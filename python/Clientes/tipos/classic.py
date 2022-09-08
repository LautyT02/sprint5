from ..cliente import Cliente
from ...Direccion.direccion import Direccion

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